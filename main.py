import hashlib
import itertools
import string

try:
    target_hash = input("Enter the target MD5 hash: ")

    characters = ""
    if input("Use lowercase letters? (y/n): ").lower() == 'y':
        characters += string.ascii_lowercase
    if input("Use uppercase letters? (y/n): ").lower() == 'y':
        characters += string.ascii_uppercase
    if input("Use numbers? (y/n): ").lower() == 'y':
        characters += string.digits
    if input("Use symbols? (y/n): ").lower() == 'y':
        characters += string.punctuation

    min_length = int(input("Enter the minimum password length: "))
    max_length = int(input("Enter the maximum password length: "))

    found_password = False
    for length in range(min_length, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            password = ''.join(combination)
            hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
            if hashed_password == target_hash:
                print(f"Password found: {password}")
                found_password = True
                break
        if found_password:
            break

    if not found_password:
        print("Password not found.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number for the password length.")
except KeyboardInterrupt:
    print("\nOperation aborted by user.")
  
