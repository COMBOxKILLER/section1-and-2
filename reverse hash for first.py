import hashlib

def read_hash_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()

def find_password(dictionary, hash_to_crack):
    for password in dictionary:
        m = hashlib.sha256()
        m.update(bytes(password, 'utf-8'))
        if m.hexdigest() == hash_to_crack:
            return password
    return None

# Read the dictionary
with open("dictionary.txt", "r") as f:
    dictionary = [line.strip() for line in f]

# Read hash_to_crack1 and find the corresponding password
hash_to_crack1 = read_hash_from_file("Hash1_Mostafa_ElSherif.txt")
password1 = find_password(dictionary, hash_to_crack1)

# Read hash_to_crack2 and find the corresponding password
hash_to_crack2 = read_hash_from_file("hash2_Mostafa_ElSherif.txt")
password2 = find_password(dictionary, hash_to_crack2)

# Print the results
print("Password for hash_to_crack1:", password1)
print("Password for hash_to_crack2:", password2)