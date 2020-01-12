import ocrmypdf

def ocr():

    '''
    inputFile: full path for scanned pdf
    outputFile: full path for ocr'd file (can be same as inputfile but will replaced the scanned file)
    textFile: full path for creating text file

    input_file, output_file: self explanatory
    force_ocr: if the file is already OCR'd, it ocr's it again by removing previous text layer
    deskew: Analyses the rotation of page
    tesseract_pagesegmode: psm mode (0-13)
    sidecar: arg for creating text file on the provided location
    rotate_pages: Further increases the accuracy of rotated scanned PDF's, also gives output pdf after
    rotating the pages in right direction

    :return:
    '''

    inputFile = "C:\\D_Drive\wordpress-pdf-invoice-plugin-sample.pdf"
    outputFile = "C:\\D_Drive\wordpress-pdf-invoice-plugin-sample_ocr.pdf"
    textFile = "C:\\D_Drive\wordpress-pdf-invoice-plugin-sample.txt"

    psm = None

    ocrmypdf.ocr(input_file=inputFile, output_file=outputFile, force_ocr=True, deskew=True, tesseract_pagesegmode=psm, sidecar=textFile,
                 rotate_pages=True)

if __name__ == "__main__":
    ocr()