# Image Encryption Tool

Imaginator is a simple Python tool that allows you to encrypt and decrypt image files using the Fernet symmetric encryption algorithm from Python's cryptography library.

## Features

- **Encryption:** Securely encrypts image files to protect their content.
- **Decryption:** Restores encrypted images to their original state.
- **Key Management:** Automatically generates and handles encryption keys.

## How to Use

1. **Prerequisites:**

   - Ensure you have Python installed.
   - Install the cryptography library:
     ```bash
     pip install cryptography
     ```

2. **Clone the Repository:**

   ```bash
   git clone https://github.com/Kinzi-c/imaginator.git

   ```

3. **Navigate to the Project Directory:**

   ```bash
   cd imaginator
   ```

4. **Run the Script:**

   ```bash
   python script.py
   ```

   Follow the on-screen instructions:

   Choose whether to "encrypt" or "decrypt".
   Provide the image file name (with the correct path if needed).

## How It Works

- **Key Generation:** Upon first run, the key.key file should be missing. The script will generate a unique Fernet encryption key and store it in the key.key file.
- **Encryption:** The chosen image file is read in binary mode. The Fernet algorithm encrypts the image data using the key. The encrypted data overwrites the original image file.
- **Decryption:** The script reads the encrypted image file, decrypts it using the stored key, and restores the original image data.

## Security Notice

- **Key Protection:** The key.key file is critical for decrypting images. Store it securely and do not share it. If lost, your images cannot be recovered.
- **Not for High-Security Environments:** This tool is designed for personal use and may not be suitable for highly sensitive data or professional security needs.
