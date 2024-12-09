#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Ensuring pip is installed..."
python3.9 -m ensurepip --upgrade

echo "Upgrading pip..."
python3.9 -m pip install --upgrade pip

echo "Installing project dependencies..."
python3.9 -m pip install -r requirements.txt

echo "Making migrations..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput --clear

echo "Build process completed!"
