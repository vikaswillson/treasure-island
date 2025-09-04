# Password Generator Project in Python

import random
import string

def generate_password():
    print("Welcome to the Password Generator!")

    # Asking user for input
    num_letters = int(input("How many letters would you like in your password? "))
    num_symbols = int(input("How many symbols would you like? "))
    num_numbers = int(input("How many numbers would you like? "))

    # Character sets
    letters = string.ascii_letters   # a-z, A-Z
    numbers = string.digits          # 0-9
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/|"

    # Random selection
    password_chars = []
    password_chars += random.choices(letters, k=num_letters)
    password_chars += random.choices(symbols, k=num_symbols)
    password_chars += random.choices(numbers, k=num_numbers)

    # Shuffle to avoid predictable pattern
    random.shuffle(password_chars)

    # Join into a final password string
    password = "".join(password_chars)

    print(f"\nYour generated password is: {password}")


# Run the project
if __name__ == "__main__":
    generate_password()
