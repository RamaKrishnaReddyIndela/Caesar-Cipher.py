def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift uppercase and lowercase letters separately
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            # Non-alphabet characters remain unchanged
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption Program")
    while True:
        choice = input("Do you want to (E)ncrypt, (D)ecrypt or (Q)uit? ").strip().upper()

        if choice == 'E':
            message = input("Enter the message to encrypt: ")
            while True:
                try:
                    shift = int(input("Enter the shift value (integer): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer for shift value.")
            encrypted_message = encrypt(message, shift)
            print("Encrypted message:", encrypted_message)

        elif choice == 'D':
            message = input("Enter the message to decrypt: ")
            while True:
                try:
                    shift = int(input("Enter the shift value (integer): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer for shift value.")
            decrypted_message = decrypt(message, shift)
            print("Decrypted message:", decrypted_message)

        elif choice == 'Q':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter E, D, or Q.")

if __name__ == "__main__":
    main()
