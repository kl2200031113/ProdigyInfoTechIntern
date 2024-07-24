from PIL import Image
import numpy as np
def encrypt_image(image_path, key):
    # Open  required image you want to encrypt
    img = Image.open(image_path)
    # Convert image to numpy array for faster pixel manipulation
    img_array = np.array(img)
    # Get dimensions of the image
    height, width, channels = img_array.shape
    # Generate a permutation of indices based on the key
    np.random.seed(key)  # Ensure same key gives same permutation
    indices = np.random.permutation(height * width * channels)
    # Encrypt the image by swapping pixels based on the permutation
    img_array_flat = img_array.flatten()
    img_array_flat[indices] = img_array_flat
    # Reshape back to original shape
    img_encrypted = img_array_flat.reshape(height, width, channels)
    # Create Image object from numpy array
    img_encrypted = Image.fromarray(img_encrypted.astype('uint8'))
    # Save encrypted image
    encrypted_path = f"encrypted_{key}.png"
    img_encrypted.save(encrypted_path)
    print(f"Image encrypted and saved as {encrypted_path}")
def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    img_encrypted = Image.open(encrypted_image_path)
    # Convert image to numpy array for faster pixel manipulation
    img_array = np.array(img_encrypted)
    # Get dimensions of the image
    height, width, channels = img_array.shape
    # Generate the same permutation of indices based on the key
    np.random.seed(key)  # Ensure same key gives same permutation
    indices = np.random.permutation(height * width * channels)
    # Decrypt the image by reversing the permutation
    img_array_flat = img_array.flatten()
    img_array_flat[indices] = img_array_flat
    # Reshape back to original shape
    img_decrypted = img_array_flat.reshape(height, width, channels)
    # Create Image object from numpy array
    img_decrypted = Image.fromarray(img_decrypted.astype('uint8'))
    # Save decrypted image
    decrypted_path = f"decrypted_{key}.png"
    img_decrypted.save(decrypted_path)
    print(f"Image decrypted and saved as {decrypted_path}")
def main():
    # Example usage
    image_path = "example_image.png"
    key = 123456  # Replace with your encryption key
    # Encrypt the image
    encrypt_image(image_path, key)
    # Decrypt the encrypted image
    encrypted_image_path = f"encrypted_{key}.png"
    decrypt_image(encrypted_image_path, key)
if name == "main":
    main()