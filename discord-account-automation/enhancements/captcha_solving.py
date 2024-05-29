import requests
from PIL import Image
from io import BytesIO
import pytesseract
from pytesseract import Output

def solve_captcha(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    captcha_text = pytesseract.image_to_string(img, config='--psm 6', output_type=Output.STRING)
    return captcha_text

# Example Usage:
# captcha_image_url = 'https://example.com/captcha_image.png'
# captcha_text = solve_captcha(captcha_image_url)
# print(captcha_text)