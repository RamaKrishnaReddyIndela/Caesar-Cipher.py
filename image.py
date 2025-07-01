from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    # Open image
    img = Image.open(input_path)
    img = img.convert('RGB')  # Ensure image is in RGB mode
    pixels = img.load()

    # Encrypt each pixel
    for i in range(img.size[0]):  # Width
        for j in range(img.size[1]):  # Height
            r, g, b = pixels[i, j]
            r_encrypted = (r + key) % 256
            g_encrypted = (g + key) % 256
            b_encrypted = (b + key) % 256
            pixels[i, j] = (r_encrypted, g_encrypted, b_encrypted)

    img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    # Open image
    img = Image.open(input_path)
    img = img.convert('RGB')
    pixels = img.load()

    # Decrypt each pixel
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            r_decrypted = (r - key) % 256
            g_decrypted = (g - key) % 256
            b_decrypted = (b - key) % 256
            pixels[i, j] = (r_decrypted, g_decrypted, b_decrypted)

    img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    while True:
        choice = input("Do you want to (E)ncrypt, (D)ecrypt, or (Q)uit? ").strip().upper()

        if choice in ['E', 'D']:
            input_path = input("Enter the input image path: ").strip()
            if not os.path.exists(input_path):
                print("File not found!")
                continue
            output_path = input("Enter the output image path: ").strip()

            try:
                key = int(input("Enter the numeric key (integer between 1-255): "))
                if not (1 <= key <= 255):
                    raise ValueError
            except ValueError:
                print("Invalid key. Please enter an integer between 1 and 255.")
                continue

            if choice == 'E':
                encrypt_image(input_path, output_path, key)
            else:
                decrypt_image(input_path, output_path, key)

        elif choice == 'Q':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option. Please select E, D, or Q.")

if __name__ == "__main__":
    main()
