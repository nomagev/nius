#!/bin/bash

# Nius Setup Script
echo "─── Preparing Nius Terminal Browser ───"

# 1. Create Virtual Environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# 2. Activate the environment
echo "Adapting environment..."
source venv/bin/activate

# 3. Upgrade pip and install requirements
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "──────────────────────────────────────"
echo "Setup complete!"
echo "To start Nius, run:"
echo "source venv/bin/activate && python nius.py"
echo "──────────────────────────────────────"