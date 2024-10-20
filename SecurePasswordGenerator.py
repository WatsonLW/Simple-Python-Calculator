# Secure password generator by Watson!

import random
import string

def generate_password(length, uppercase, special_characters, digits):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if special_characters:
        characters += string.punctuation
    if digits:
        characters += string.digits
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Welcome to the random password generator!")

length = int(input("How long should the password be? (Number only): "))  # Convert input to integer
uppercase = input("Should uppercase letters be included? (y/n): ")
if uppercase.lower() == "y":
    uppercase = True
else:
    uppercase = False

special_characters = input("Should special characters be included? (y/n): ")
if special_characters.lower() == "y":
    special_characters = True
else:
    special_characters = False

digits = input("Should numbers be included? (y/n): ")
if digits.lower() == "y":
    digits = True
else:
    digits = False

password = generate_password(length, uppercase, special_characters, digits)
print("Your secure password is:", password)
