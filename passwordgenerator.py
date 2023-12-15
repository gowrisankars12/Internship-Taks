import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True,
                       num_uppercase=1, num_lowercase=1, num_digits=1, num_special_chars=1, exclude_ambiguous=True,
                       exclude_similar_chars=True, exclude_repeating_chars=True, custom_characters=None,
                       num_passwords=1, exclude_characters=None):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase * num_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase * num_lowercase
    if use_digits:
        characters += string.digits * num_digits
    if use_special_chars:
        characters += string.punctuation * num_special_chars

    if custom_characters:
        characters += custom_characters

    if exclude_characters:
        characters = ''.join(char for char in characters if char not in exclude_characters)

    if not characters:
        print("Error: Please enable at least one character set.")
        return None

    if exclude_ambiguous:
        ambiguous_chars = 'B8G6I1l0OQDS5Z2'
        characters = ''.join(char for char in characters if char not in ambiguous_chars)

    if exclude_similar_chars:
        similar_chars = '1l0O'
        characters = ''.join(char for char in characters if char not in similar_chars)

    if exclude_repeating_chars:
        characters = ''.join(sorted(set(characters), key=characters.index))

    passwords = [''.join(random.choice(characters) for _ in range(length)) for _ in range(num_passwords)]
    return passwords

def get_yes_or_no_input(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input in ['y', 'n']:
            return user_input
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    print("Welcome to the Ultimate Password Generator!")

    password_length = get_integer_input("Enter the length of the password: ")

    include_uppercase = get_yes_or_no_input("Include uppercase letters? (y/n): ") == 'y'
    num_uppercase = get_integer_input("Enter the number of uppercase letters: ")

    include_lowercase = get_yes_or_no_input("Include lowercase letters? (y/n): ") == 'y'
    num_lowercase = get_integer_input("Enter the number of lowercase letters: ")

    include_digits = get_yes_or_no_input("Include digits? (y/n): ") == 'y'
    num_digits = get_integer_input("Enter the number of digits: ")

    include_special_chars = get_yes_or_no_input("Include special characters? (y/n): ") == 'y'
    num_special_chars = get_integer_input("Enter the number of special characters: ")

    exclude_ambiguous = get_yes_or_no_input("Exclude ambiguous characters? (y/n): ") == 'y'
    exclude_similar_chars = get_yes_or_no_input("Exclude similar characters? (y/n): ") == 'y'
    exclude_repeating_chars = get_yes_or_no_input("Exclude repeating characters? (y/n): ") == 'y'

    custom_characters = input("Enter any additional characters you want to include (or press Enter to skip): ")

    num_passwords = get_integer_input("Enter the number of passwords to generate: ")

    exclude_characters = input("Enter any characters you want to exclude (or press Enter to skip): ")

    generated_passwords = generate_password(
        password_length, include_uppercase, include_lowercase, include_digits, include_special_chars,
        num_uppercase, num_lowercase, num_digits, num_special_chars, exclude_ambiguous,
        exclude_similar_chars, exclude_repeating_chars, custom_characters, num_passwords, exclude_characters
    )

    if generated_passwords:
        print("\nGenerated Passwords:")
        for idx, password in enumerate(generated_passwords, start=1):
            print(f"Password {idx}: {password}")
