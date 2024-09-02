from PIL import Image
import numpy as np


def load_image(image_path):
    """Load an image from a file."""
    image = Image.open(image_path)
    return image

def save_image(image, image_path):
    """Save an image to a file."""
    image.save(image_path)

def encrypt_image(image):
    """Encrypt the image by applying a basic mathematical operation to each pixel."""
    np_image = np.array(image)
    # Simple encryption: invert the pixel values
    encrypted_image = 255 - np_image
    return Image.fromarray(encrypted_image)

def decrypt_image(encrypted_image):
    """Decrypt the image by reversing the encryption operation."""
    np_encrypted_image = np.array(encrypted_image)
    # Simple decryption: invert the pixel values back
    decrypted_image = 255 - np_encrypted_image
    return Image.fromarray(decrypted_image)

# Example usage

# Provide the path to your input image here
input_image_path = r'C:\Users\kanis\OneDrive\Desktop\Anas.jpg'  

# Provide the path where you want to save the encrypted image
encrypted_image_path = r'C:\Users\kanis\OneDrive\Desktop\encrypted_image.jpg'  

# Provide the path where you want to save the decrypted image
decrypted_image_path = r'C:\Users\kanis\OneDrive\Desktop\decrypted_image.jpg' 

# Load the original image
image = load_image(input_image_path)

# Encrypt the image
encrypted_image = encrypt_image(image)
save_image(encrypted_image, encrypted_image_path)
print(f'Encrypted image saved to {encrypted_image_path}')

# Decrypt the image
decrypted_image = decrypt_image(encrypted_image)
save_image(decrypted_image, decrypted_image_path)
print(f'Decrypted image saved to {decrypted_image_path}')
