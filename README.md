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

## PikePDF Problem

### v1.8.3

The latest version is throwing problem in importing some module. I don't know what exactly. When I navigate the error, it's showing that there's a problem in importing _qpdf.
Due to this code does not produce any output.

### v1.7.0
By installing this version we can get rid of the v1.8.3 import error. However, it is also not perfect. When we run the code we get ***AttributeError: 'pikepdf._qpdf.Pdf' object has no attribute 'check'*** error. To solve that add following code in _methods.py present in **"your location\ocrmyPDF_Windows\ocr_env\Lib\site-packages\pikepdf"**.

Add this after **def encryption()** method.

```python
def check(self):
        """
        Check if PDF is well-formed.  Similar to ``qpdf --check``.
        Returns:
            list of strings describing errors of warnings in the PDF
        """

        class DiscardingParser(StreamParser):
            def __init__(self):  # pylint: disable=useless-super-delegation
                super().__init__()  # required for C++

            def handle_object(self, obj):
                pass

            def handle_eof(self):
                pass

        problems = []

        try:
            self._decode_all_streams_and_discard()
        except PdfError as e:
            problems.append(str(e))

        discarding_parser = DiscardingParser()

        for basic_page in self.pages:
            page = Page(basic_page)
            try:
                page.parse_contents(discarding_parser)
            except PdfError as e:
                problems.append(str(e))

        for warning in self.get_warnings():
            problems.append("WARNING: " + warning)

        return problems
```

This solves the previously mentioned error. **This does produce output but also gives one more error**

For now, I can live with "streamparser" error, however, I'm still trying to figure this error out.

## Licensing
You can use this repository in anyway you need. Kindly make any changes in a different branch.
