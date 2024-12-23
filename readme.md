# Pic to text
Script analyses the clipboard buffer, if there's an image in buffer, 
script tries to convert image to text and saves it in clipboard if succeeded.
works with english and russian languages
## Libraries
Based on tesseract OCR: https://github.com/UB-Mannheim/tesseract/wiki

Also uses pillow and clipboard libs
## Binaries
In Windows, you can simply download .exe from Releases, there's no need to install tesseract.
## How to use
In Windows, run pix2text.exe.
Then, use "Scissors" app (Win + Shift + s) and select area with text.

Text is now copied in clipboard, just paste it.
