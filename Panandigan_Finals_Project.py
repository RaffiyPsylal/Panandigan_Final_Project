import random
import string


def generate_random_chars(char_set, count):
    return ''.join(random.choice(char_set) for _ in range(count))


class PasswordGenerator:
    def __init__(self, pw_len, min_upper, min_lower, min_digits, min_spec):
        self.pw_len = pw_len
        self.min_upper = min_upper
        self.min_lower = min_lower
        self.min_digits = min_digits
        self.min_spec = min_spec
        self.all_chars = string.ascii_letters + string.digits + string.punctuation
        self.password = []

    def validate_input(self):
        total_requirements = self.min_upper + self.min_lower + self.min_digits + self.min_spec
        if total_requirements > self.pw_len:
            print("Error: The sum of minimum requirements exceeds the specified password length.")
            exit()

    def generate_password(self):
        self.validate_input()

        self.password.extend(generate_random_chars(string.ascii_uppercase, self.min_upper))
        self.password.extend(generate_random_chars(string.ascii_lowercase, self.min_lower))
        self.password.extend(generate_random_chars(string.digits, self.min_digits))
        self.password.extend(generate_random_chars(string.punctuation, self.min_spec))

        remaining = self.pw_len - self.min_lower - self.min_upper - self.min_digits - self.min_spec
        self.password.extend(generate_random_chars(self.all_chars, remaining))
        random.shuffle(self.password)

        # Trim the password if it exceeds the specified length
        self.password = self.password[:self.pw_len]

    def get_password(self):
        return ''.join(self.password)


# User choice
print("Choose an option:")
print("1. Generate a random password")
print("2. Define password requirements")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    pw_len = int(input("How long should the password be? "))
    # Create PasswordGenerator object
    password_generator = PasswordGenerator(pw_len, 0, 0, 0, 0)
    # Generate and print the random password
    password_generator.generate_password()
    print("Generated Password:", password_generator.get_password())
elif choice == "2":
    # User input with validation for minimum requirements
    pw_len = int(input("How long should the password be? "))
    min_upper = int(input("Minimum Upper Case: "))
    min_lower = int(input("Minimum Lower Case: "))
    min_digits = int(input("Minimum Numbers: "))
    min_spec = int(input("Minimum Special: "))

    # Create PasswordGenerator object
    password_generator = PasswordGenerator(pw_len, min_upper, min_lower, min_digits, min_spec)
    # Generate and print the password
    password_generator.generate_password()
    print("Generated Password:", password_generator.get_password())
else:
    print("Invalid choice. Please enter either '1' or '2'.")
