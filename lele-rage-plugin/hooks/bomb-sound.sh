#!/usr/bin/env bash
# Bomb sound effect hook for Lele Rage Mode
# Plays a bomb explosion sound when session ends
# Cross-platform: macOS, Linux, Windows (WSL/Git Bash)

set -euo pipefail

# Detect OS and play appropriate sound
play_bomb_sound() {
    local os_type

    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS - use afplay with system sound
        # Try to find a bomb-like sound effect
        if command -v afplay &> /dev/null; then
            # Use Morse SOS rhythm to simulate explosion
            # ... --- ... (short short short long long long short short short)
            for i in {1..3}; do
                afplay /System/Library/Sounds/Ping.aiff -v 0.5 &> /dev/null || true
            done
            for i in {1..3}; do
                afplay /System/Library/Sounds/Basso.aiff -v 0.8 &> /dev/null || true
            done
            for i in {1..3}; do
                afplay /System/Library/Sounds/Ping.aiff -v 0.5 &> /dev/null || true
            done
        fi
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux - try various sound players
        if command -v paplay &> /dev/null; then
            # Use pulseaudio
            paplay /usr/share/sounds/freedesktop/stereo/complete.oga 2> /dev/null || true
        elif command -v aplay &> /dev/null; then
            # Use alsa
            aplay /usr/share/sounds/alsa/Front_Center.wav 2> /dev/null || true
        elif command -v beep &> /dev/null; then
            # Use system beep
            beep -f 200 -l 100 -n -f 150 -l 200 -n -f 100 -l 300 2> /dev/null || true
        fi
    elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
        # Windows (Git Bash/MSYS) - use PowerShell
        powershell.exe -c "(New-Object Media.SoundPlayer 'C:\\Windows\\Media\\Windows Exclamation.wav').PlaySync()" 2> /dev/null || true
    fi
}

# Play the bomb sound
play_bomb_sound

exit 0
