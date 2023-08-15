from pdf2docx import Converter
import os

pdf_file = os.path.abspath('c:\\Users\\ishuk\\Desktop\\PDF conversion\\static\\uploads\\abc.pdf')
docx_file = os.path.abspath('c:\\Users\\ishuk\\Desktop\\PDF conversion\\static\\uploads\\abc.docx')

cv=Converter(pdf_file)
cv.convert(docx_file)
cv.close()