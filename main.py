import time
from PIL import ImageGrab, Image
import clipboard
import pytesseract  # for OCR
import threading
import os
import sys

def get_tesseract_path():
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, "tesseractlib", "tesseract.exe")
    else:
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "tesseractlib", "tesseract.exe")

tesseract_path = get_tesseract_path()
pytesseract.pytesseract.tesseract_cmd = tesseract_path

print(f"Tesseract path: {pytesseract.pytesseract.tesseract_cmd}")

def process_image(img):
    # process image
    text = pytesseract.image_to_string(img, lang="rus+eng")
    clipboard.copy(text.strip())
    print("Text copied to clipboard.")


def monitor_clipboard():
    last_image = None
    while True:
        try:
            img = ImageGrab.grabclipboard()  # get clipboard
            if isinstance(img, Image.Image):
                # img = img.resize((img.width // 2, img.height // 2))  # compress if necessary
                # img = img.convert("L")  # convert to gray if necessary
                if img != last_image and img is not None:
                    last_image = img
                    threading.Thread(target=process_image, args=(img,)).start()
        except Exception:
            pass
        time.sleep(0.1)



if __name__ == "__main__":
    monitor_clipboard()
