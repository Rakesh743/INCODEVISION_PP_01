import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter password length: "))
    
    if length < 4:
        print("Password too weak! Use minimum 4 characters.")
    else:
        password = generate_password(length)
        print("Your Strong Password:", password)

except ValueError:
    print("Error: Please enter only numbers!")