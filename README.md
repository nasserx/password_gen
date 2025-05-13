# Password Generator

A simple Python project to generate secure passwords with customizable length and character composition (letters, digits, punctuation).

## Features

- Specify password length.
- Control the percentage of letters, digits, and punctuation.
- Generate and print a single password.
- Save multiple passwords to a file (`passwords.txt`).

## Usage

Example from `main.py`:

```python
from password_generator import GeneratePassword

password = GeneratePassword(length=8, letters_p=50, digits_p=30, punctuation_p=20)
print(password.generate())
password.save_to_file(lines_num=100)
