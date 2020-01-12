# ocrmyPDF_Windows
I had some issues while using ocrmypdf on windows, it didn't worked at all. So, I just tried to resolve the issues by myself. Made some changes in the ocrmypdf and pikepdf's code. At last I was successful in making it work. I thought by sharing this repo might help someone, so cheers!

## Requirements
- Tesseract v4 (provided in repo) (leptonica is installed by default)
- qpdf (provided)
- ghostscript (provided)
- jbig2enc (provided)
- Imagemagick (provided)
- python 3.6 or above
- ocrmypdf (library)

## Steps for installation

**You can try to use the *ocr_env* (virtual env) provided by me. It already has the changes done to the code by me. If it works kindly tell me on my e-mail *lakshay1296@gmail.com*.**

- Install tesseract (need to add in environment variables)
- You don't need to install qpdf, ghostscript, jbig2enc, imagemagick, however you need to mention their path in environment variables.
- **QPDF:**    *your_path\ocrmyPDF_Windows\qpdf-9.1.0\bin*
- **ghostscript:**    *your_path\ocrmyPDF_Windows\gs\gs9.27\bin*
- **jbig2enc:**    *your_path\ocrmyPDF_Windows\agl-jbig2enc-0.27-14-gc709efe-leptonlib-1.66-win32-bin*
- **imagemagick:**    *your_path\ocrmyPDF_Windows\ImageMagick-7.0.8-Q16*
- python 3.6 or above (I'm using 3.8.1)
- pip install ocrmypdf
- pip install pikepdf==1.7.0 (newer versions doesn't seem to work)

