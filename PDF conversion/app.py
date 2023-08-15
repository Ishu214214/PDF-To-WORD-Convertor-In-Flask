from flask import Flask,request,render_template,jsonify
from pdf2docx import Converter
import os

app=Flask(__name__)

app.static_folder = 'static'

@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload" ,methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part"
    
    file = request.files["file"]

    if file.filename == "":
        return "No selected file"
    
    new_filename="abc.pdf"

    pdf_file_path = os.path.join(app.root_path, 'static', 'uploads', new_filename)
    docx_file_path = os.path.join(app.root_path, 'static', 'uploads', 'abc.docx')

    file.save(pdf_file_path)

    if os.path.exists(pdf_file_path):
        cv = Converter(pdf_file_path)  # Use the full path to the PDF file
        cv.convert(docx_file_path)
        cv.close()
    else:
        return "PDF file does not exist"
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)