import pytesseract
from PIL import Image

# 列出支持的语言
print(pytesseract.get_languages(config=''))
print(pytesseract.image_to_string(Image.open(F"../data/test2/time2.png"), lang='chi_sim+eng'))
