import fitz
# def function to extract text
def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts all text from the given PDF file.

    :param pdf_path: The path to the PDF file to extract text from.
    :return: The extracted text.
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

# create txt file function
def create_txt_file(pdf_path: str, output_file_path: str):
    # create txt file
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(extract_text_from_pdf(pdf_path) + '\n')
        print("File created successfully!")

# call the function
pdf_path = "D:/#ESTUDO PLANO/EXTRAIR_DADOS/2022/EDITAL_001_2023_0000001.pdf"
output_file_path = "01-2022.txt"

create_txt_file(pdf_path, output_file_path)