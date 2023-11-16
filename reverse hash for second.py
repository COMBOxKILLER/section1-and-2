import hashlib
import random

def read_hash_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()

def modify_password(password, modifications):
    # Apply the recorded modifications
    modified_password = password

    for modification in modifications:
        index, char = modification
        modified_password = modified_password[:index] + char + modified_password[index:]

    # Return the modified password
    return modified_password

def find_password(dictionary, hash_to_crack, modifications):
    for original_password in dictionary:
        # Apply the recorded modifications
        modified_password = modify_password(original_password, modifications)

        m = hashlib.sha256()
        m.update(bytes(modified_password, "utf-8"))
        if m.hexdigest() == hash_to_crack:
            return original_password

    return None

# Read the dictionary
with open("dictionary.txt", "r") as f:
    dictionary = [line.strip() for line in f]

# Crack hash_to_crack1
hash_to_crack1 = read_hash_from_file("Hash1_Mostafa_ElSherif.txt")
modifications1 = [(0, '1'), (5, '$')]  # Example modifications
password1 = find_password(dictionary, hash_to_crack1, modifications1)

# Crack hash_to_crack2
hash_to_crack2 = read_hash_from_file("hash2_Mostafa_ElSherif.txt")
modifications2 = [(2, '&'), (7, '!')]  # Example modifications
password2 = find_password(dictionary, hash_to_crack2, modifications2)

# Print the results
print("Password for hash_to_crack1:", password1)
print("Password for hash_to_crack2:", password2)