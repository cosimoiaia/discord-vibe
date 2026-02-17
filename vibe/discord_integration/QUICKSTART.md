# Quick Start Guide for Discord Integration

## 🚀 Get Started in 5 Minutes

### 1. Install Discord.py
```bash
pip install discord.py>=2.3.2
```

### 2. Create Discord Bot
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create new application → Add Bot → Copy token
3. Invite bot to server with `Send Messages` permission

### 3. Get Channel ID
- Enable Developer Mode in Discord settings
- Right-click channel → Copy Channel ID

### 4. Run Vibe with Discord
```bash
vibe --discord-token "YOUR_BOT_TOKEN" --discord-channel CHANNEL_ID
```

### 5. Chat with Vibe!
```
You: "Hello Vibe, help me with Python code?"
Vibe: "Hello! I'm your coding assistant..."
```

## 📋 Common Commands

```bash
# Check setup
vibe --setup

# Run with debug logging
VIBE_DEBUG=1 vibe --discord-token "$TOKEN" --discord-channel "$CHANNEL"

# Use environment variables
export DISCORD_BOT_TOKEN="your_token"
export DISCORD_CHANNEL_ID="channel_id"
vibe --discord-token "$DISCORD_BOT_TOKEN" --discord-channel "$DISCORD_CHANNEL_ID"
```

## 🔧 Troubleshooting

**Bot not responding?**
- ✅ Check bot token
- ✅ Verify channel ID  
- ✅ Ensure bot has permissions
- ✅ Confirm bot is online

**Need help?**
```bash
vibe --help
```