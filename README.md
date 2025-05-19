# Password Generator

A simple Python project to generate secure passwords with customizable length and character composition (lowercase letters, uppercase letters, and digits).

## Features

- Specify total password length.
- Control the percentage of lowercase letters, uppercase letters, and digits.
- Generate and display a single password.
- Generate and save multiple passwords to a file (`passwords.txt`).

## Usage

Example from `main.py`:

```python
from password_generator import GeneratePassword

# Create a password generator with desired settings
password = GeneratePassword(length=12, lowercase_percent=50, uppercase_percent=30, digits_percent=20)

# Generate a single password
print(password.generate_single())

# Generate and save 100 passwords to a file
password.generate_multiple(count=100)
