# Password Strength Analyzer

A Python tool that analyzes password strength using the zxcvbn library, calculating entropy (randomness) and displaying a color-coded ASCII bar. Achieved up to 62 bits of entropy with a custom 48-character password.

## Features
- Rates password strength from 0/5 (weak) to 5/5 (strong)
- Shows entropy in bits
- Provides security warnings (e.g., common passwords)
- Color-coded output using colorama

## Installation
1. Ensure Python 3.x is installed.
2. Create a virtual environment: python3 -m venv myenv
3. Activate it: source myenv/bin/activate
4. Install dependencies: pip install zxcvbn colorama

## Usage
Run the script: python3 password_analyzer.py
Enter a password when prompted to see the analysis.

## Screenshots
See attached files (weak.png, medium.png, strong.png) for weak, medium, and 62-bit strong password results.

## License
MIT License - free to use and modify!
