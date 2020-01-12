import ocrmypdf

def ocr():
    ocrmypdf.ocr(input_file="C:\\D_Drive\scansmpl.pdf",
             output_file="C:\\D_Drive\scansmpl_ocr.pdf",
             force_ocr=True)

if __name__ == "__main__":
    ocr()