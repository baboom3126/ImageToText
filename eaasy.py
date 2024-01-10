from PIL import Image
import pytesseract

tesseract_path = "C:/Program Files/Tesseract-OCR/tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = tesseract_path
# Load the image from file
img_path = 'essay1.jpg'
img = Image.open(img_path)

# Use tesseract to do OCR on the image
text = pytesseract.image_to_string(img,lang="chi_tra+eng")


print(text)