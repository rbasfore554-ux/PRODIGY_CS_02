
from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert("RGB")
    data = np.array(img)

    encrypted_data = (data + key) % 256
    encrypted_img = Image.fromarray(encrypted_data.astype('uint8'), 'RGB')
    encrypted_img.save("encrypted_image.png")
    print("🔐 Encrypted image saved as 'encrypted_image.png'")

def decrypt_image(encrypted_path, key):
    img = Image.open(encrypted_path)
    img = img.convert("RGB")
    data = np.array(img)

    decrypted_data = (data - key) % 256
    decrypted_img = Image.fromarray(decrypted_data.astype('uint8'), 'RGB')
    decrypted_img.save("decrypted_image.png")
    print("🔓 Decrypted image saved as 'decrypted_image.png'")

def main():
    print("🖼️ Image Encryption using Pixel Manipulation")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Use 'e' or 'd'.")
        return

    path = input("Enter image file path: ")
    try:
        key = int(input("Enter encryption key (e.g., 10): "))
    except ValueError:
        print("Key must be a number.")
        return

    if choice == 'e':
        encrypt_image(path, key)
    else:
        decrypt_image(path, key)

if __name__ == "__main__":
    main()
