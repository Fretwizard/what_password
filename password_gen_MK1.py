# First attempt at a password creator.
import random
import string

def generate_password(length=12):
    """Generates a random password of the specified length."""

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = lowercase + uppercase + digits + symbols

    # Ensure at least one of each type
    temp_password = random.choice(lowercase) + random.choice(uppercase) + random.choice(digits) + random.choice(symbols)

    # Fill remaining length with random characters
    for _ in range(length - 4):
        temp_password += random.choice(all_chars)

    # Shuffle the password to make it stronger
    password_list = list(temp_password)
    random.shuffle(password_list)
    password = "".join(password_list)

    return password

# Get desired password length from user
length = int(input("Enter the desired password length: "))

# Generate and print the password
password = generate_password(length)
print("Your generated password is:", password)
