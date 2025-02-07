#!/bin/bash

# Create a new virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install all dependencies
pip install -r requirements.txt

echo "✅ Virtual environment setup complete!"

