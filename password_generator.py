import random


class GeneratePassword:
    def __init__(self, length, lowercase_percent, uppercase_percent, digits_percent):
        """
        Initialize the password generator with desired length and character type percentages.
        """
        self.length = length
        self.percentages = (lowercase_percent, uppercase_percent, digits_percent)
        self.uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
        self.digits = "0123456789"

    @staticmethod
    def get_counts_from_percentages(length, percentages):
        """
        Convert percentage values to actual counts while distributing remainders fairly.
        """
        raw_counts = [p * length / 100 for p in percentages]
        counts = [int(c) for c in raw_counts]
        remainder = length - sum(counts)

        # Distribute remaining characters to highest decimal values
        for i, _ in sorted(enumerate(raw_counts), key=lambda x: x[1] - int(x[1]), reverse=True)[:remainder]:
            counts[i] += 1

        return counts

    def generate_single(self):
        """
        Generate a single password based on initialized settings.
        """
        if len(self.percentages) != 3 or sum(self.percentages) != 100:
            raise ValueError("Percentages must contain exactly 3 values that sum to 100 (e.g., 50, 30, 20)")

        lowercase_count, uppercase_count, digit_count = self.get_counts_from_percentages(
            self.length, self.percentages
        )

        password_chars = (
            random.choices(self.lowercase_letters, k=lowercase_count) +
            random.choices(self.uppercase_letters, k=uppercase_count) +
            random.choices(self.digits, k=digit_count)
        )
        random.shuffle(password_chars)
        return "".join(password_chars)

    def generate_multiple(self, count):
        """
        Generate multiple passwords and write them to 'passwords.txt'.
        """
        with open("passwords.txt", "a") as file:
            for _ in range(count):
                file.write(f"{self.generate_single()}\n")
