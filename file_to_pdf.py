import pdfkit
file="recieve.log"
file_path="recieve.pdf"
pdfkit.from_file(file, file_path)