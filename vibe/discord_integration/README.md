# Discord Integration for Mistral Vibe

This module enables interaction with the Mistral Vibe coding assistant directly through Discord channels.

## 🎯 Features

- **Real-time Coding Assistance**: Get help with code analysis, writing, debugging, and more
- **Channel-Specific**: Configure Vibe to respond only in specific Discord channels
- **Conversation Context**: Maintains conversation history between messages
- **Automatic Response Formatting**: Handles long responses by splitting them into multiple messages
- **Error Handling**: Provides user-friendly error messages

## 📋 Prerequisites

Before you begin, ensure you have:

1. **Python 3.12+** installed
2. **Discord Bot Token**: Create a bot on the [Discord Developer Portal](https://discord.com/developers/applications)
3. **Discord Server**: A server where you have permission to add bots
4. **Mistral API Key**: Configured in your Vibe setup

## 🛠️ Installation

### 1. Install Required Dependencies

```bash
pip install discord.py>=2.3.2
```

### 2. Set Up Your Discord Bot

1. **Create a Discord Application**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application" and give it a name (e.g., "Vibe Assistant")

2. **Create a Bot**:
   - In your application, go to the "Bot" tab
   - Click "Add Bot" and confirm
   - Copy your **Bot Token** (keep this secret!)

3. **Invite the Bot to Your Server**:
   - Go to the "OAuth2" tab, then "URL Generator"
   - Select "bot" scope
   - Under "Bot Permissions", select:
     - `Send Messages`
     - `Read Message History`
   - Copy the generated URL and open it in your browser
   - Select the server where you want to add the bot

4. **Get Your Channel ID**:
   - In Discord, enable Developer Mode in User Settings > Advanced
   - Right-click on the channel where you want Vibe to respond
   - Click "Copy Channel ID"

## 🚀 Usage

### Basic Usage

```bash
# Start Vibe in Discord mode
vibe --discord-token YOUR_BOT_TOKEN --discord-channel CHANNEL_ID
```

Replace:
- `YOUR_BOT_TOKEN`: Your Discord bot token from the Developer Portal
- `CHANNEL_ID`: The ID of the Discord channel where Vibe should respond

### Example

```bash
vibe --discord-token "OTIzNDU2Nzg5MDEyMzQ1Njc4.YmFhYg.ABCDEF1234567890" --discord-channel 123456789012345678
```

### Environment Variables (Recommended)

For better security, use environment variables:

```bash
export DISCORD_BOT_TOKEN="your_bot_token_here"
export DISCORD_CHANNEL_ID="your_channel_id_here"

vibe --discord-token "$DISCORD_BOT_TOKEN" --discord-channel "$DISCORD_CHANNEL_ID"
```

## 💬 Interacting with Vibe on Discord

Once the bot is running and connected to your channel:

### Basic Commands

```
You: "Hello Vibe, can you help me with Python code?"
Vibe: "Hello! I'm Vibe, your coding assistant. I can help with Python code analysis, writing, debugging, and more!"

You: "How do I sort a list in Python?"
Vibe: "You can sort a list in Python using the `sorted()` function or the `list.sort()` method. Here's an example..."
```

### Code Assistance

```
You: "Can you write a function to calculate factorial?"
Vibe: "Certainly! Here's a Python function to calculate factorial..."
```

### File Operations (if enabled)

```
You: "Can you read the requirements.txt file?"
Vibe: "I can help with that. Here's the content of requirements.txt..."
```

## ⚙️ Configuration

### Vibe Configuration

Ensure your Vibe configuration is set up properly:

```bash
# Check your Vibe configuration
vibe --setup
```

### Agent Selection

The Discord integration uses the `auto-approve` agent by default for seamless interaction. This agent automatically approves tool usage for convenience.

## 🔒 Security Best Practices

1. **Keep Your Bot Token Secret**: Never share your bot token or commit it to version control
2. **Use Environment Variables**: Store sensitive information in environment variables
3. **Limit Bot Permissions**: Only give the bot the minimum permissions it needs
4. **Monitor Bot Activity**: Keep an eye on what your bot is doing
5. **Rate Limiting**: Be aware of Discord's rate limits

## 🐛 Troubleshooting

### Common Issues

**Bot doesn't respond:**
- Check that the bot token is correct
- Verify the channel ID is correct
- Ensure the bot has been invited to your server
- Check that the bot has the correct permissions

**Connection errors:**
- Verify your internet connection
- Check Discord's status at [status.discord.com](https://status.discord.com)
- Ensure your bot token hasn't been revoked

**Permission errors:**
- Make sure the bot has "Send Messages" permission in the channel
- Check that you've invited the bot with the correct OAuth2 scope

### Debugging

Run with additional logging:

```bash
VIBE_DEBUG=1 vibe --discord-token YOUR_TOKEN --discord-channel CHANNEL_ID
```

## 📚 Technical Details

### Architecture

```
Discord User → Discord Channel → Vibe Bot → Vibe Agent → Vibe Bot → Discord Channel → Discord User
```

### Key Components

1. **DiscordBot**: Manages Discord connection and message routing
2. **DiscordHandler**: Bridges Discord messages to Vibe's AgentLoop
3. **AgentLoop**: Maintains conversation context and processes messages
4. **Event System**: Handles different types of events (messages, tool calls, etc.)

### Message Flow

1. User sends message in Discord channel
2. DiscordBot receives and filters the message
3. DiscordHandler passes message to AgentLoop
4. AgentLoop processes message and generates response
5. DiscordHandler formats the response
6. DiscordBot sends response back to Discord channel

## 🎓 Examples

### Setting Up a Development Environment

```bash
# Create a virtual environment
python -m venv vibe-env
source vibe-env/bin/activate

# Install dependencies
pip install mistral-vibe discord.py

# Run Vibe with Discord integration
vibe --discord-token "$DISCORD_BOT_TOKEN" --discord-channel "$DISCORD_CHANNEL_ID"
```

### Using with Different Channels

```bash
# Run multiple instances for different channels
vibe --discord-token "$TOKEN" --discord-channel 123456789012345678 &
vibe --discord-token "$TOKEN" --discord-channel 876543210987654321 &
```

## 📖 License

This Discord integration is part of Mistral Vibe and is licensed under the Apache 2.0 License.

## 🤝 Contributing

Contributions are welcome! Please follow the main Vibe project's contribution guidelines.

## 📬 Support

For issues or questions:
- Check the [Vibe GitHub Issues](https://github.com/mistralai/mistral-vibe/issues)
- Join the Mistral community for discussions

---

**Enjoy using Vibe on Discord!** 🚀 Your coding assistant is now available in your favorite chat platform.