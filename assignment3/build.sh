#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Verifying Python version..."
python3 --version

echo "Ensuring pip is installed..."
python3 -m ensurepip --upgrade

echo "Upgrading pip..."
python3 -m pip install --upgrade pip

echo "Installing project dependencies..."
python3 -m pip install -r requirements.txt

echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

echo "Build process completed!"
