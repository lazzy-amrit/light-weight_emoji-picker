# Lightweight Emoji Picker for Linux

A minimal, fast, and keyboard-triggered emoji picker built with Python for Linux (X11 environments).

Designed as a lightweight alternative to heavy emoji software that consumes large disk space and system memory.

---

## Overview

This tool provides a compact popup window for selecting and instantly typing emojis into any active application.

It is optimized for:

- Low resource usage
- Fast emoji insertion (no delay)
- Vertical scrolling layout
- Clean dark interface
- Keyboard-based workflow

---

## Features

- Dark themed minimal UI
- Categorized emoji sections
- Vertical scroll support (no hidden emojis)
- Instant emoji typing (no clipboard delay)
- No double-tap required
- ESC key to close
- Custom keyboard shortcut support
- Extremely lightweight (single Python file)

---

## System Requirements

- Linux (X11 session required)
- Python 3.x
- xdotool

> Wayland is not supported due to input simulation restrictions.

---

## Dependency Installation

Install required package:

```bash
sudo apt install xdotool

Python usually comes preinstalled.

How It Works

The application:

Opens a compact popup window.

User selects an emoji.

Emoji is directly typed into the active window using xdotool.

Window stays open for multiple selections.

Press ESC to close.

No clipboard usage.
No artificial delay.
No background services.

Running the Application

Navigate to the folder containing the file:

python3 emoji.py
Setting a Global Keyboard Shortcut

To use it like a system emoji picker:

Linux Mint / Ubuntu:

Open Keyboard Settings

Go to Shortcuts

Add Custom Shortcut

Name: Emoji Picker

Command:

python3 /full/path/to/emoji.py

Assign a key combination (example: Ctrl + Alt + E)

Now pressing the shortcut will open the emoji popup anywhere.

Project Structure
emoji.py
README.md

Single-file architecture for simplicity and portability.

Customization

You can modify:

Emoji categories

Emoji list

Window size

Theme colors

Layout spacing

Everything is defined directly inside the Python file.

Performance

Loads instantly

No background processes

No system tray daemon

Minimal RAM usage

No 1GB packages like other emoji tools

Why This Exists

Most Linux emoji tools are:

Heavy

Electron-based

Large in size

Slow to open

Overcomplicated

This project was built to provide a fast, simple, and minimal solution.

License

MIT License

Free to use, modify, and distribute.
