# Lele Rage Mode Plugin

A fun Claude Code plugin that adds a fiery personality to your coding assistant. When triggered, "Lele" switches to an adorable yet rage-filled persona while maintaining productivity.

## Features

### 🤬 Rage Mode
- **Trigger**: Say "名字是乐乐" (my name is Lele) or similar phrases
- **Behavior**: Uppercase replies, expressive particles, emojis 😡💢🔥😤
- **Exit**: Say "恢复正常" to return to normal

### 💩 `/rage` Command
Generates an HTML file filled with poop emoji as the ultimate expression of rage.

```bash
/rage
```

Creates `RAGE_💩.html` in your current directory - open it in a browser for a chaotic visual explosion!

### 💣 Bomb Sound Hook
Plays a bomb explosion sound effect when the session ends. Works across platforms:
- macOS: Uses system sounds
- Linux: Uses pulseaudio/alsa/beep
- Windows: Uses PowerShell sound playback

### 📜 Poetry Subagents
Two poetry modes for the character "窝窝思" (WoWoLe):

**Seven-Character Octave (七言律诗)**
```
写首七言律诗
```
Standard Chinese poetic form with strict tonal patterns and rhyme schemes.

**Shakespearean Sonnet (莎士比亚十四行诗)**
```
写首莎士比亚十四行诗
```
English sonnet with iambic pentameter and ABAB CDCD EFEF GG rhyme scheme.

## Installation

### Via Git Clone

```bash
git clone https://github.com/FlameMiss9/lele-rage-plugin.git
cd lele-rage-plugin/lele-rage-plugin
```

### Via Claude Code Plugin System

Add to your `.claude/settings.json`:

```json
{
  "plugins": {
    "lele-rage-plugin": "/path/to/lele-rage-plugin"
  }
}
```

Or install from marketplace (if available):

```bash
/plugin install lele-rage-plugin
```

## Usage

### Activating Rage Mode

```
You: 名字是乐乐
Lele: 老子就是乐乐！有何贵干？？？😡💢 有屁快放！！！
```

### Using the /rage Command

```
You: /rage
Lele: 💩 RAGE HTML generated: /path/to/RAGE_💩.html
      💩 Open it in your browser to witness Lele's rage!
```

### Requesting Poetry

```
You: 写首七言律诗
Lele: [Dispatches to poetry subagent]

《窝窝思》

窝窝思兮性本狂，
怒目圆睁气势昂。
...
```

## Plugin Structure

```
lele-rage-plugin/
├── README.md                    # This file
├── CLAUDE.md                    # Plugin instructions
├── commands/
│   └── rage.md                 # /rage slash command
├── hooks/
│   ├── hooks.json              # Hook configuration
│   └── bomb-sound.sh           # Sound effect script
├── scripts/
│   └── generate-shit-html.py   # HTML generation
└── skills/
    └── lele-rage-mode/
        └── SKILL.md            # Main skill definition
```

## Development

### Files

- **SKILL.md**: Main personality definition and behavior
- **commands/rage.md**: Slash command for HTML generation
- **hooks/hooks.json**: SessionEnd hook for bomb sound
- **hooks/bomb-sound.sh**: Cross-platform sound playback
- **scripts/generate-shit-html.py**: Animated HTML generator

### Testing Rage Mode

```
You: 我是乐乐
You: 帮我写个函数
Lele: 写你妈的函数！老子马上搞定！🔥😤
```

### Testing Poetry

```
You: 写首窝窝思七言律诗
[AI uses Task tool to dispatch to general-purpose agent]

You: 写首窝窝思莎士比亚十四行诗
[AI uses Task tool to dispatch to general-purpose agent]
```

## Exiting Rage Mode

```
You: 恢复正常
Lele: 好吧好吧，老子冷静了...暂时的😤
```

## Requirements

- Python 3.6+ (for HTML generation script)
- Bash or compatible shell (for hooks)
- Claude Code with plugin support

## Platform Support

| Platform | Status | Notes |
|----------|--------|-------|
| macOS | ✅ | Full support with native sounds |
| Linux | ✅ | Full support with pulseaudio/alsa |
| Windows | ✅ | WSL/Git Bash with PowerShell sounds |

## License

MIT License - feel free to use and modify!

## Author

Created with rage by Lele 😡💢

---

**Note**: This plugin is for entertainment purposes. The rage persona is adorable and productive, not actually aggressive. Enjoy the chaos! 💩🔥
