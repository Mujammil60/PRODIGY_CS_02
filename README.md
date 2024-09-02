# PRODIGY_CS_02
This project demonstrates a simple method for encrypting and decrypting images using Python's PIL (Pillow) library and NumPy. The encryption is performed by inverting the pixel values of the image, which is then reversed during the decryption process.

Features
Load Image: Load an image from a specified file path.
Encrypt Image: Apply a simple encryption by inverting the pixel values.
Decrypt Image: Reverse the encryption by inverting the pixel values again.
Save Image: Save the encrypted or decrypted image to a specified file path.
How It Works
The encryption process involves inverting the pixel values of the image. In other words, each pixel value is subtracted from 255 (the maximum value for a pixel in an 8-bit image). This simple operation effectively "encrypts" the image. The decryption process is the reverse, where the pixel values are again inverted to recover the original image.

Requirements
Python 3.x
Pillow (PIL Fork)
NumPy
You can install the required libraries using pip:

bash
Copy code
pip install Pillow numpy
How to Use
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/image-encryption-decryption.git
cd image-encryption-decryption
Set the paths:

In the script, update the following paths with your file locations:

python
Copy code
input_image_path = r'C:\path\to\your\input_image.jpg'
encrypted_image_path = r'C:\path\to\save\encrypted_image.jpg'
decrypted_image_path = r'C:\path\to\save\decrypted_image.jpg'
Run the script:

bash
Copy code
python image_encryption.py
The script will load the image, encrypt it, and save the encrypted image. It will then decrypt the encrypted image and save the decrypted version.

Output:

The encrypted image will be saved at the specified encrypted_image_path.
The decrypted image will be saved at the specified decrypted_image_path.
Code Overview
load_image(image_path): Loads an image from the given file path.
save_image(image, image_path): Saves an image to the specified file path.
encrypt_image(image): Encrypts the image by inverting its pixel values.
decrypt_image(encrypted_image): Decrypts the image by reversing the inversion process.
