# Nius.py Terminal Browser
# Copyright (C) 2026  Nomagev
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License.

import os
import sys
import tty
import termios
import time
import html
import requests

import art  # Local import for ASCII assets

# --- CONFIGURATION ---
BASE_URL = "https://hacker-news.firebaseio.com/v0"
DEFAULT_STORY_LIMIT = 10
DELAY_NORMAL = 0.017
DELAY_FAST = 0.010

# --- UI UTILITIES ---

def slow_print(text, delay=DELAY_NORMAL):
    """Prints text with a typewriter effect for retro aesthetics."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def get_char():
    """Reads a single keypress instantly without requiring the Enter key."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return char

def clear_screen():
    """Clears the terminal console based on the Operating System."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- DATA FETCHING ---

def fetch_top_stories(limit=DEFAULT_STORY_LIMIT):
    """Retrieves the top story IDs from Hacker News."""
    try:
        response = requests.get(f"{BASE_URL}/topstories.json", timeout=5)
        return response.json()[:limit]
    except Exception as error:
        print(f"\n[!] Connection Error: {error}")
        return []

def fetch_item(item_id):
    """Retrieves details for a specific item (story or comment) by ID."""
    try:
        response = requests.get(f"{BASE_URL}/item/{item_id}.json", timeout=5)
        return response.json()
    except Exception:
        return {}

def format_hn_text(raw_html):
    """Converts Hacker News HTML tags into terminal-friendly Markdown."""
    if not raw_html:
        return ""
    
    # Replacement map for basic formatting
    conversions = {
        '<p>': '\n\n',
        '<i>': '*',
        '</i>': '*',
        '<pre><code>': '\n\n[CODE]\n',
        '</code></pre>': '\n[END CODE]\n'
    }
    
    text = raw_html
    for tag, replacement in conversions.items():
        text = text.replace(tag, replacement)
        
    return html.unescape(text)

# --- VIEW LAYOUTS ---

def display_comments(comment_ids):
    """Renders comments with ESC/B navigation and Q to Quit."""
    if not comment_ids:
        print("No comments found.")
        return 

    for c_id in comment_ids:
        comment = fetch_item(c_id)
        
        # Skip invalid or empty comments
        if any([comment.get('deleted'), comment.get('dead'), not comment.get('text')]):
            continue
            
        author = comment.get('by', 'anonymous')
        body = format_hn_text(comment.get('text'))
        
        print(f"\n┌── {author}:")
        for line in body.split('\n'):
            if line.strip():
                sys.stdout.write("│ ")
                slow_print(line, delay=DELAY_NORMAL)
        
        print(f"\n{'='*30}")
        print("[ESC] Next | [B] Back to Feed | [Q] Quit")
        print(f"{'='*30}")

        # Input loop for comment navigation
        while True:
            cmd = get_char().lower() # Normalize to lowercase
            if cmd == '\x1b':  # ESC
                break
            elif cmd == 'b':   # Back to Feed
                return 
            elif cmd == 'q':   # Global Quit
                print("\nStay curious. Goodbye!")
                sys.exit(0) # Immediately stops the script 
    
    input("\n--- End of thread. Press Enter to return ---")

def show_main_feed():
    """Displays the list of top stories and returns the data for selection."""
    clear_screen()
    art.print_logo()
    
    print(f"{'ID' :<3} | {'SCORE' :<5} | {'TITLE'}")
    print("-" * 60)
    
    story_ids = fetch_top_stories()
    stories_data = []

    for index, s_id in enumerate(story_ids, 1):
        story = fetch_item(s_id)
        stories_data.append(story)
        
        row = f"{index:<3} | {story.get('score', 0):<5} | {story.get('title')}"
        slow_print(row, delay=DELAY_FAST)
    
    return stories_data

# --- CORE EXECUTION ---

def main():
    """Main application loop."""
    while True:
        current_stories = show_main_feed()
        
        print("\n" + "="*60)
        user_input = input("Select #, [R]efresh, or [Q]uit: ").lower()
        
        if user_input == 'q':
            print("Stay curious. Goodbye!")
            break
        elif user_input == 'r':
            continue
        
        try:
            selection_index = int(user_input) - 1
            if 0 <= selection_index < len(current_stories):
                selected_story = current_stories[selection_index]
                
                clear_screen()
                art.print_logo()
                print(f"STORY: {selected_story.get('title')}")
                print(f"URL:   {selected_story.get('url', 'No external link')}")
                print("-" * 60)
                
                comment_ids = selected_story.get('kids', [])
                display_comments(comment_ids)
        except (ValueError, IndexError):
            # Ignore invalid inputs and restart loop
            continue

if __name__ == "__main__":
    main()