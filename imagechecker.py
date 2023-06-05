import cv2
import pytesseract

# Specify the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def extract_text(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Preprocess the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply image enhancement techniques if required
    # For example, you can apply thresholding, denoising, or other filters

    # Perform OCR to extract text
    text = pytesseract.image_to_string(gray)

    return text

def find_common_text(image1_path, image2_path):
    # Extract text from the first image
    text1 = extract_text(image1_path)

    # Extract text from the second image
    text2 = extract_text(image2_path)

    # Output the common text content
    print("Common Text Content:")
    print(text1)


# Usage example
image1_path = './img1.PNG'
image2_path = './img2.PNG'

find_common_text(image1_path, image2_path)
