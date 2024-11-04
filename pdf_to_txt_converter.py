import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file, text_file):
    reader = PdfReader(pdf_file)
    with open(text_file, 'w', encoding='utf-8') as f:
        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            if text:
                f.write(f"--- Page {page_number} ---\n")
                f.write(text)
                f.write("\n\n")

def main():
    input_folder = 'input_pdfs'         # Folder containing PDFs
    output_text_folder = 'output_texts' # Folder for text files

    # Create output folder if it doesn't exist
    os.makedirs(output_text_folder, exist_ok=True)

    # List all PDF files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            text_filename = os.path.splitext(filename)[0] + '.txt'
            text_path = os.path.join(output_text_folder, text_filename)

            print(f'Extracting text from {filename}...')
            extract_text_from_pdf(pdf_path, text_path)

    print('Done!')

if __name__ == '__main__':
    main()
