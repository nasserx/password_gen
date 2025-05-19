from password_generator import GeneratePassword


def generate_one():
    """
    Generate and display a single password.
    """
    length = int(input("Enter password length: "))
    lowercase_p, uppercase_p, digits_p = input(
        "Enter percentages for lowercase, uppercase, and digits (e.g., 50 30 20): "
    ).split()

    password = GeneratePassword(length, int(lowercase_p), int(uppercase_p), int(digits_p))
    print("\nGenerated password:")
    print(password.generate_single())


def generate_many():
    """
    Generate multiple passwords and save them to a file.
    """
    length = int(input("Enter password length: "))
    lowercase_p, uppercase_p, digits_p = input(
        "Enter percentages for lowercase, uppercase, and digits (e.g., 50 30 20): "
    ).split()
    count = int(input("Enter number of passwords to generate: "))

    password = GeneratePassword(length, int(lowercase_p), int(uppercase_p), int(digits_p))
    password.generate_multiple(count)
    print(f"\nDone. {count} passwords saved to 'passwords.txt'.")


print("""
==============================
 Password Generator
==============================
1. Generate a single password
2. Generate multiple passwords and save to file
""")

choice = input("Select an option (1 or 2): ")

if choice == "1":
    generate_one()
elif choice == "2":
    generate_many()
else:
    print("Invalid choice. Please enter 1 or 2.")
