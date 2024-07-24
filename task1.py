def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shifted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            if char.isupper():
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shifted_char = chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
            if char.isupper():
                shifted_char = shifted_char.upper()
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

# Example usage
if __name__ == "__main__":
    # Input message and shift value from the user
    message = input("Enter message to encrypt/decrypt: ")
    shift = int(input("Enter shift value (positive integer): "))
    
    # Encrypt the message
    encrypted_message = encrypt(message, shift)
    print(f"Encrypted message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, shift)
    print(f"Decrypted message: {decrypted_message}")
