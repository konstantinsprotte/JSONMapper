#!/bin/bash

# Set the name of your virtual environment
venv_name="myflaskenv"

# Set the directory for the virtual environment
venv_dir="/Users/antonburckhardt/PycharmProjects/pythonProject/$venv_name"

# Create a virtual environment using Python 3
python3 -m venv "$venv_dir"

# Upgrade pip and install dependencies (e.g., Flask)
"$venv_dir/bin/pip" install --upgrade pip
"$venv_dir/bin/pip" install Flask

# Print instructions
echo "Virtual environment '$venv_name' created in '$venv_dir'."
echo "To activate the virtual environment, run:"
echo "source '$venv_dir/bin/activate'"



#ACTIVATION CODE:
#
# source /Users/antonburckhardt/PycharmProjects/pythonProject/venv_JSONMapper/bin/activate

