import ocrmypdf

def ocr():
    ocrmypdf.ocr(input_file="C:\\D_Drive\Software_Developer_Resume_Lakshay.pdf",
             output_file="C:\\D_Drive\Software_Developer_Resume_Lakshay_ocr.pdf",
             force_ocr=True)

if __name__ == "__main__":
    ocr()