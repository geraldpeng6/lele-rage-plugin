#!/usr/bin/env python3
"""
Generate an HTML file filled with 💩 emoji - the ultimate expression of Lele's rage.
Creates a visually chaotic poop emoji explosion in HTML format.
"""

import os
from pathlib import Path

def generate_shit_html():
    """Generate HTML filled with poop emoji in a chaotic pattern."""

    # Get current directory
    output_path = Path.cwd() / "RAGE_💩.html"

    # Generate the HTML content
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LELE'S RAGE MODE 💩💩💩</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Comic Sans MS', 'Chalkboard SE', sans-serif;
            background: linear-gradient(45deg, #1a1a1a, #2d2d2d, #1a1a1a);
            min-height: 100vh;
            overflow: hidden;
            position: relative;
        }

        .container {
            position: relative;
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            gap: 20px;
            padding: 20px;
        }

        .shit {
            font-size: clamp(2rem, 8vw, 6rem);
            animation: float 3s ease-in-out infinite;
            cursor: pointer;
            transition: transform 0.2s;
            user-select: none;
        }

        .shit:hover {
            transform: scale(1.5) rotate(20deg);
        }

        .shit:nth-child(odd) {
            animation-delay: -1.5s;
        }

        .shit:nth-child(3n) {
            animation-delay: -0.75s;
        }

        @keyframes float {
            0%, 100% {
                transform: translateY(0) rotate(0deg);
            }
            25% {
                transform: translateY(-20px) rotate(-10deg);
            }
            50% {
                transform: translateY(-40px) rotate(0deg);
            }
            75% {
                transform: translateY(-20px) rotate(10deg);
            }
        }

        @keyframes explode {
            0% {
                transform: scale(0) rotate(0deg);
                opacity: 0;
            }
            50% {
                transform: scale(1.5) rotate(180deg);
                opacity: 1;
            }
            100% {
                transform: scale(1) rotate(360deg);
                opacity: 1;
            }
        }

        .explode {
            animation: explode 0.5s ease-out forwards;
        }

        .title {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: clamp(3rem, 15vw, 10rem);
            color: #ff6b35;
            text-shadow:
                0 0 10px #ff6b35,
                0 0 20px #ff6b35,
                0 0 30px #ff6b35,
                0 0 40px #ff0000;
            z-index: 1000;
            pointer-events: none;
            white-space: nowrap;
        }

        .background-shit {
            position: fixed;
            font-size: clamp(1rem, 4vw, 3rem);
            opacity: 0.3;
            animation: drift 20s linear infinite;
            pointer-events: none;
        }

        @keyframes drift {
            from {
                transform: translateY(-100vh) rotate(0deg);
            }
            to {
                transform: translateY(100vh) rotate(360deg);
            }
        }
    </style>
</head>
<body>
    <div class="title">💩 暴躁乐乐 💩</div>
"""

    # Add floating background emojis
    for i in range(30):
        left = (i * 3.33) % 100
        delay = -(i * 0.5)
        duration = 15 + (i % 10)
        html_content += f'    <div class="background-shit" style="left: {left}%; animation-delay: {delay}s; animation-duration: {duration}s;">💩</div>\n'

    # Add main container emojis
    html_content += '    <div class="container">\n'
    for i in range(100):
        delay = -(i * 0.1)
        html_content += f'        <div class="shit" style="animation-delay: {delay}s;" onclick="this.classList.add(\'explode\')">💩</div>\n'
    html_content += '    </div>\n'

    # Add JavaScript for interactivity
    html_content += """
    <script>
        // Add more chaos on click
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('shit')) {
                // Create explosion effect
                for (let i = 0; i < 5; i++) {
                    const newShit = document.createElement('div');
                    newShit.className = 'shit';
                    newShit.textContent = '💩';
                    newShit.style.position = 'fixed';
                    newShit.style.left = e.clientX + 'px';
                    newShit.style.top = e.clientY + 'px';
                    newShit.style.transform = `translate(${(Math.random() - 0.5) * 200}px, ${(Math.random() - 0.5) * 200}px)`;
                    document.body.appendChild(newShit);
                    setTimeout(() => newShit.remove(), 2000);
                }
            }
        });

        // Random explosions
        setInterval(() => {
            const shits = document.querySelectorAll('.shit:not(.background-shit)');
            if (shits.length > 0) {
                const randomShit = shits[Math.floor(Math.random() * shits.length)];
                randomShit.classList.add('explode');
                setTimeout(() => randomShit.classList.remove('explode'), 500);
            }
        }, 500);
    </script>
</body>
</html>
"""

    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"💩 RAGE HTML generated: {output_path}")
    print(f"💩 Open it in your browser to witness Lele's rage!")

if __name__ == "__main__":
    generate_shit_html()
