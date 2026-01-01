# Lele Rage Mode Plugin

This plugin adds a fiery personality to Claude Code. The main behavior is defined in the `lele-rage-mode` skill.

## Quick Start

1. **Activate Rage Mode**: Say "名字是乐乐" (my name is Lele)
2. **Use /rage Command**: Generate a chaotic HTML file filled with 💩
3. **Request Poetry**: Ask for "七言律诗" or "莎士比亚十四行诗" about "窝窝思"
4. **Session End**: Hear a bomb explosion sound effect

## Components

- **Skill**: `skills/lele-rage-mode/SKILL.md` - Main personality and behavior
- **Command**: `commands/rage.md` - Slash command for HTML generation
- **Hook**: `hooks/hooks.json` + `bomb-sound.sh` - SessionEnd bomb sound
- **Script**: `scripts/generate-shit-html.py` - HTML generator

All detailed instructions are in the SKILL.md file. The skill will be automatically loaded when relevant.

Enjoy the chaos! 😡💢🔥💩
