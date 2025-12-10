
# Public Payroll Data Extraction Pipeline

## 📋 Overview

This project implements an automated **ETL pipeline** designed to process semi-structured public sector payroll data. It converts legacy PDF reports into clean, analytical Excel datasets, facilitating financial auditing and resource management.

The system utilizes **Python** to extract raw text, sanitize encoding artifacts (fixing UTF-8 issues), parse hierarchical employee records, and export structured data for analysis.

## 🚀 Key Features

  * **PDF Text Extraction:** leverages `PyMuPDF` (Fitz) to scrape high-fidelity text data from PDF documents.
  * **Data Sanitization:** Automatically cleans character encoding errors (e.g., correcting `MatrÃ­cula` to `Matricula`) and strips irrelevant headers/footers to prepare data for parsing.
  * **Structured Parsing:** Uses positional logic to identify and associate multi-line employee records, extracting fields such as **Name**, **Role (Cargo)**, **CPF**, and **Admission Date**.
  * **Excel Export:** Transforms parsed data into a `pandas` DataFrame and exports a formatted `.xlsx` file using `openpyxl`.

## 🛠️ Tech Stack

  * **Language:** Python 3.x
  * **Libraries:**
      * `pandas` (Data manipulation)
      * `pymupdf` (PDF processing)
      * `openpyxl` (Excel I/O)
      * `re` (Regular Expressions)

## 📂 Project Structure

The pipeline is divided into four modular scripts to ensure separation of concerns:

| Script | Description |
| :--- | :--- |
| **`1-create_txt.py`** | **Extract:** Reads the source PDF and dumps raw content into a text file. |
| **`2-treat-data.py`** | **Transform (Stage 1):** Cleans the raw text, fixing specific UTF-8 encoding issues and removing pagination noise. |
| **`3-create-table.py`** | **Transform (Stage 2):** Parses the cleaned text stream to identify worker entities and map attributes (Matricula, CPF, etc.). |
| **`4-create_excel.py`** | **Load:** Compiles the structured data into a Pandas DataFrame and saves it as `output.xlsx`. |

## ⚙️ Installation & Usage

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/payroll-etl-pipeline.git
    ```

2.  **Install dependencies:**

    ```bash
    pip install pandas openpyxl pymupdf
    ```

3.  **Run the Pipeline:**
    Execute the scripts in sequential order to process the file:

    ```bash
    python 1-create_txt.py
    python 2-treat-data.py
    python 3-create-table.py
    python 4-create_excel.py
    ```

