import random

class GeneratePassword:
    def __init__(self, length, letters_p, digits_p, punctuation_p):
        """
        Initialize the password generator with the total length and character type percentages.

        Parameters:
        - length (int): Total length of the generated password.
        - letters_p (int): Percentage of letters in the password.
        - digits_p (int): Percentage of digits in the password.
        - punctuation_p (int): Percentage of punctuation characters in the password.

        Raises:
        - ValueError: If the sum of percentages is not 100 (checked later during generation).
        """
        self.length = length
        self.percentages = (letters_p, digits_p, punctuation_p)
        self.letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.digits = "0123456789"
        self.punctuation = "!@#$%^&*"

    @staticmethod
    def get_percentages(length, values):
        """
        Convert percentages into exact integer counts for each character type.

        Parameters:
        - length (int): The total desired length of the password.
        - values (list or tuple): A list of three percentages (letters, digits, punctuation).

        Returns:
        - list[int]: A list of three integers representing the character counts that sum up to `length`.
        """
        values = [p * length / 100 for p in values]
        floors = [int(v) for v in values]
        diff = length - sum(floors)

        # Distribute the remaining characters based on highest decimal part
        for i, _ in sorted(enumerate(values), key=lambda x: x[1] - int(x[1]), reverse=True)[:diff]:
            floors[i] += 1

        return floors

    def generate(self):
        """
        Generate a single password based on the provided percentages.

        Returns:
        - str: The generated password string.

        Raises:
        - ValueError: If percentages are not exactly three values or their sum is not 100.
        """
        if len(self.percentages) != 3 or sum(self.percentages) != 100:
            raise ValueError("Please enter three percentages that add up to 100 (e.g., 50, 30, 20)")

        letters_p, digits_p, punctuation_p = self.get_percentages(self.length, self.percentages)

        letters = random.choices(self.letters, k=letters_p)
        digits = random.choices(self.digits, k=digits_p)
        punct = random.choices(self.punctuation, k=punctuation_p)

        password_chars = letters + digits + punct
        random.shuffle(password_chars)

        return "".join(password_chars)

    def save_to_file(self, lines_num):
        """
        Generate multiple passwords and save them to a file named 'passwords.txt'.

        Parameters:
        - lines_num (int): The number of passwords to generate and save.
        """
        file_path = "passwords.txt"
        with open(file_path, "a") as file:
            for _ in range(lines_num):
                file.write(f"{self.generate()}\n")



if __name__ == "__main__":
    import time

    password = GeneratePassword(
        length=8, letters_p=50, digits_p=30, punctuation_p=20
    )
    while True:
        p = password.generate()
        print(f"password: {p} length: {len(p)}")
        time.sleep(0.5)
