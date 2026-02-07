#!/bin/bash
# Nius Launcher

# Get the directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# Check if venv exists, activate it, and run
if [ -d "venv" ]; then
    source venv/bin/activate
    python3 nius.py
else
    echo "Error: Virtual environment (venv) not found."
    echo "Please run: python3 -m venv venv && pip install -r requirements.txt"
fi