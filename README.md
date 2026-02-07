[![License: GPL v2](https://img.shields.io/badge/License-GPL_v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Platform](https://img.shields.io/badge/platform-macOS%20|%20Linux-lightgrey.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
[![Nius.py Tests](https://github.com/nomagev/nius/actions/workflows/python-tests.yml/badge.svg)](https://github.com/nomagev/nius/actions/workflows/python-tests.yml)

# NIUS.py
> A minimalist, terminal-based Hacker News browser for the distraction-free developer.

Nius.py (pronounced "News PY") is a lightweight Python utility designed to browse Hacker News headers and comments directly from your terminal. No heavy UX, no tracking—just the data.

![Nius Terminal Screenshot](img/nius-screenshot.jpeg)

## Quick Start

Ensure you are on a Unix-based system (macOS/Linux).

1. **Clone and Enter:**
   ```bash
   git clone [https://github.com/nomagev/nius.git](https://github.com/nomagev/nius.git)
   cd nius

2. **Run Setup: This script creates a virtual environment and installs all dependencies.**
    ```bash
    chmod +x setup.sh
    ./setup.sh

3. **Launch:**
    ./run.sh

## Features
- **Cinematic Rendering:** Text is written in real-time with a "typewriter" effect.
- **Keyboard Driven:** Use `ESC` for next comment and `B` for back.
- **Single-Key Navigation:** Use `ESC` for next and `B` for back.
- **Markdown-Lite:** Cleans HN HTML into terminal text.

## Controls
- `[Number]`: Select story
- `[ESC]`: Next comment
- `[B]`: Back to feed
- `[Q]`: Quit

## License
GNU GPL v2.0