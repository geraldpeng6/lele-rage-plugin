#!/bin/bash
# bomb.sh - 乐乐炸弹音效脚本 (macOS/Linux版)
# 💥 每次 Claude Code 停止时播放音效
# 使用方法: chmod +x bomb.sh

case "$(uname -s)" in
    Darwin)  # macOS
        if command -v afplay &> /dev/null; then
            afplay /System/Library/Sounds/Glass.aiff 2>/dev/null ||
            afplay /System/Library/Sounds/Blow.aiff 2>/dev/null
        elif command -v say &> /dev/null; then
            say -v Fred "BOOM" 2>/dev/null
        else
            echo -e "\a"
        fi
        ;;
    Linux)  # Linux
        if command -v paplay &> /dev/null; then
            paplay /usr/share/sounds/freedesktop/stereo/complete.oga 2>/dev/null ||
            paplay /usr/share/sounds/alsa/Front_Center.wav 2>/dev/null
        elif command -v aplay &> /dev/null; then
            aplay /usr/share/sounds/alsa/Front_Center.wav 2>/dev/null
        else
            echo -e "\a"
        fi
        ;;
    CYGWIN*|MINGW*|MSYS*)  # Windows Git Bash
        powershell.exe -c "(New-Object Media.SoundPlayer 'C:\Windows\Media\ding.wav').PlaySync()" 2>/dev/null ||
        echo -e "\a"
        ;;
    *)
        echo -e "\a"  # 终端铃声后备
        ;;
esac

echo "💥 乐乐炸弹音效完成！💢" >&2
