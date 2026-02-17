"""Discord bot for Vibe agent integration."""

import asyncio
import logging
from typing import Callable, Coroutine

from discord import Intents, Client, Message

from vibe.core.config import VibeConfig

logger = logging.getLogger(__name__)

# Lazy import to avoid circular dependencies
AgentLoop = None


class DiscordBot:
    """Discord bot that connects Vibe agent to Discord channels."""

    def __init__(
        self,
        token: str,
        channel_id: int,
        message_handler: Callable[[str], Coroutine[None, None, str]],
    ) -> None:
        """
        Initialize Discord bot.
        
        Args:
            token: Discord bot token
            channel_id: ID of the channel to monitor
            message_handler: Async function to handle messages and return responses
        """
        self.token = token
        self.channel_id = channel_id
        self.message_handler = message_handler
        
        # Set up Discord client
        intents = Intents.default()
        intents.messages = True
        intents.message_content = True
        
        self.client = Client(intents=intents)
        
        # Event handlers
        self.client.event(self._on_ready)
        self.client.event(self._on_message)

    async def _on_ready(self) -> None:
        """Called when the bot is ready."""
        logger.info(f"Logged in as {self.client.user} (ID: {self.client.user.id})")
        logger.info(f"Monitoring channel {self.channel_id}")

    async def _on_message(self, message: Message) -> None:
        """Called when a message is received."""
        # Ignore messages from the bot itself
        if message.author == self.client.user:
            return
            
        # Only respond to messages in the configured channel
        if message.channel.id != self.channel_id:
            return
            
        # Ignore empty messages
        if not message.content.strip():
            return
            
        logger.info(f"Received message from {message.author}: {message.content}")
        
        # Process the message with the Vibe agent
        try:
            response = await self.message_handler(message.content)
            if response:
                # Split response into chunks if it's too long
                chunks = [response[i:i+2000] for i in range(0, len(response), 2000)]
                for chunk in chunks:
                    await message.channel.send(chunk)
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            await message.channel.send(f"❌ Error: {str(e)}")

    async def start(self) -> None:
        """Start the Discord bot."""
        await self.client.start(self.token)

    async def stop(self) -> None:
        """Stop the Discord bot."""
        await self.client.close()


class DiscordHandler:
    """Handler that bridges Discord messages to Vibe agent."""

    def __init__(self, config: VibeConfig) -> None:
        """
        Initialize Discord handler.
        
        Args:
            config: Vibe configuration
        """
        self.config = config
        # Lazy initialization of agent loop to avoid import issues
        self._agent_loop = None

    @property
    def agent_loop(self):
        """Lazy load the agent loop."""
        if self._agent_loop is None:
            global AgentLoop
            if AgentLoop is None:
                from vibe.core.agent_loop import AgentLoop as AL
                AgentLoop = AL
            self._agent_loop = AgentLoop(
                config=self.config,
                agent_name="auto-approve",  # Use auto-approve for Discord
                enable_streaming=False,
            )
        return self._agent_loop

    async def handle_message(self, message: str) -> str:
        """
        Handle a Discord message by passing it to the Vibe agent.
        
        Args:
            message: The message from Discord
            
        Returns:
            The agent's response
        """
        from vibe.core.types import AssistantEvent, UserMessageEvent, ToolResultEvent, ReasoningEvent
        
        # Collect response from agent
        response_parts = []
        
        try:
            async for event in self.agent_loop.act(message):
                # Handle specific event types that contain content
                if isinstance(event, (AssistantEvent, UserMessageEvent, ToolResultEvent, ReasoningEvent)):
                    if hasattr(event, 'content') and event.content:
                        response_parts.append(event.content)
                
                # Add error handling for tool failures
                if isinstance(event, ToolResultEvent) and event.error:
                    response_parts.append(f"⚠️ Tool error: {event.error}")
                    
        except Exception as e:
            logger.error(f"Agent processing error: {e}")
            return f"❌ Sorry, I encountered an error: {str(e)}"
        
        if not response_parts:
            return "🤔 I'm thinking..."
            
        return "".join(response_parts)[:1800]  # Limit to fit in Discord message