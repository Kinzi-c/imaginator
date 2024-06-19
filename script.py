from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"

def generate_key():
    "Generates a Fernet key and saves it to a file."
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    "Loads the key from the specified file."
    if not os.path.exists(KEY_FILE):
        generate_key()  # Generate a key if it doe not exist
    with open(KEY_FILE, "rb") as key_file:
        key = key_file.read()
    return key

def encrypt_message(message, key):
    "Encrypts the given message."
    f = Fernet(key)
    encrypted = f.encrypt(message)
    return encrypted

def decrypt_message(token, key):
    "Decrypts the given token."
    f = Fernet(key)
    return f.decrypt(token)

def encrypt_image(filename, key):
    "Encrypts the given image file."
    with open(filename, "rb") as file:
        original = file.read()
        encrypted = encrypt_message(original, key)
    with open(filename, "wb") as file:
        file.write(encrypted)

def decrypt_image(filename, key):
    "Decrypts the given image file."
    with open(filename, "rb") as file:
        token = file.read()
        decrypted = decrypt_message(token, key)
    with open(filename, "wb") as file:
        file.write(decrypted)

if __name__ == "__main__":
    key = load_key()  # Load the key at the start

    while True:
        action = input("Do you want to encrypt or decrypt the image? (encrypt/decrypt/quit): ")

        if action == "quit":
            break

        image_file = input("Enter the image file name: ")

        if action == "encrypt":
            encrypt_image(image_file, key)
            print("Image encrypted successfully!")
        elif action == "decrypt":
            decrypt_image(image_file, key)
            print("Image decrypted successfully!")
        else:
            print("Invalid input. Please enter 'encrypt', 'decrypt', or 'quit'.")
