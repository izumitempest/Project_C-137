import pytesseract
import re
from PIL import Image
import io
import base64

# Define regex pattern for GOU reg numbers
# Format: GOU/2023/CSC/0001
REGEX_PATTERN = r"GOU/\d{2}/[A-Z]{3}/\d{1,4}"

def extract_text_from_image(image_bytes):
    """
    Accepts raw image bytes and returns OCR extracted text.
    """
    try:
        image = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"Error processing image: {e}"

def find_valid_reg_numbers(text):
    """
    Finds all valid registration numbers using regex from OCR text.
    """
    matches = re.findall(REGEX_PATTERN, text)
    return matches
