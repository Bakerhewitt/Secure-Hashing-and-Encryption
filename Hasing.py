import hashlib

def _stringhash_():
    password = input("Enter a password to hash: ").strip()
    hash_object = hashlib.sha256(password.encode())
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    
def _filehash_():
    filename = input("Enter the filename to hash: ").strip().strip('"')
    try:
        with open(filename, "rb") as f:
            file_data = f.read()
            hash_object = hashlib.sha256(file_data)
            hex_dig = hash_object.hexdigest()
            print(hex_dig)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Hash a string")
    print("2. Hash a file")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        _stringhash_()
    elif choice == "2":
        _filehash_()
    else:
        print("Invalid choice.")
        