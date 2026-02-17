# Git Repository Changes

## 🔄 Repository Migration

The main upstream repository has been changed from:
```
https://github.com/mistralai/mistral-vibe.git
```

To:
```
https://github.com/cosimoiaia/discord-vibe.git
```

## 📋 Changes Made

### Git Remote Configuration
```bash
# Previous remote
origin	https://github.com/mistralai/mistral-vibe.git (fetch)
origin	https://github.com/mistralai/mistral-vibe.git (push)

# New remote
origin	https://github.com/cosimoiaia/discord-vibe.git (fetch)
origin	https://github.com/cosimoiaia/discord-vibe.git (push)
```

### Command Used
```bash
cd /home/mimmo/projects/mistral-vibe
git remote set-url origin https://github.com/cosimoiaia/discord-vibe.git
```

## 🔧 Next Steps

### For Contributors
1. **Update your local repositories**:
   ```bash
   git remote set-url origin https://github.com/cosimoiaia/discord-vibe.git
   ```

2. **Fetch latest changes**:
   ```bash
   git fetch origin
   ```

3. **Push to new repository**:
   ```bash
   git push -u origin main
   ```

### For New Users
1. **Clone the new repository**:
   ```bash
   git clone https://github.com/cosimoiaia/discord-vibe.git
   cd discord-vibe
   ```

2. **Install dependencies**:
   ```bash
   pip install -e .
   pip install discord.py>=2.3.2
   ```

3. **Use Discord integration**:
   ```bash
   vibe --discord-token YOUR_TOKEN --discord-channel CHANNEL_ID
   ```

## 📝 Notes

- All existing code and functionality remains the same
- Only the repository location has changed
- The Discord integration features are fully functional
- Documentation has been updated to reflect the new repository

## 🎯 Impact

This change allows for:
- Focused development on Discord integration features
- Separate versioning and releases for Discord-specific functionality
- Easier collaboration on Discord-related enhancements
- Independent issue tracking and project management

---

**Migration Date**: 2024
**Previous Repository**: https://github.com/mistralai/mistral-vibe.git
**New Repository**: https://github.com/cosimoiaia/discord-vibe.git