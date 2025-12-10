
# 📄 Payroll Data Extraction & Processing Pipeline

This project automates the extraction, cleaning, and structuring of payroll data originally stored in PDF documents.
It converts raw payroll PDFs into a clean, standardized Excel spreadsheet with key fields such as **Registration Number**, **Name**, **Position**, **CPF**, **Admission Date**, and **Admission Type**.

The pipeline was designed to support:

* financial impact assessments
* HR audits and compliance
* public-sector payroll analytics
* modeling and decision-support workflows
* structured data generation from unstructured documents

---

## 🚀 Features

✔ Extracts text from payroll PDFs
✔ Cleans and normalizes broken encodings and system lines
✔ Removes headers, footers, and non-relevant metadata
✔ Structures employee records automatically
✔ Converts the final dataset into Excel (`.xlsx`)
✔ End-to-end automated workflow in Python

---

## 🧩 Project Structure

### **1. `#1create_txt.py` – PDF Text Extraction**

Extracts full text from the payroll PDF using **PyMuPDF (fitz)** and outputs a raw `.txt` file.

### **2. `#2treat-data.py` – Cleaning & Normalization**

Cleans the extracted text by:

* removing system-generated lines (headers, timestamps, resource codes, etc.)
* fixing broken characters (e.g., `MatrÃ­cula` → `Matricula`)
* standardizing field names
* removing suffixes such as `| 082020 | 700 | EN`

### **3. `#3create-table.py` – Structured Record Builder**

Parses the cleaned text and organizes each employee’s data into a structured block containing:

* Registration Number
* Name
* Position
* CPF
* Admission Date
* Admission Type

### **4. `#4create_excel.py` – Excel Generator**

Reads all structured records and exports them into a clean **Excel spreadsheet** using pandas and openpyxl.

---

## 🔁 Processing Pipeline

### **Step 1: PDF → Raw Text**

A `.txt` file is generated containing all text extracted from the PDF.

### **Step 2: Raw Text → Cleaned Text**

Unnecessary lines are removed, encodings are fixed, and fields are standardized.

### **Step 3: Cleaned Text → Structured Records**

The script detects each employee entry and organizes it into a consistent “key: value” format, for example:

```
Matricula: 0105994.05
Name: EMPLOYEE NAME
Cargo: AGENTE ADMINISTRATIVO
CPF: 027.773.893-81
Admissao: 14/01/2011
Forma de Admissao: EFETIVO
```

### **Step 4: Structured Records → Excel**

The data is converted into a spreadsheet suitable for analysis.

---

## 🛠 Requirements

* Python **3.8+**
* Libraries:

  * `pymupdf` (fitz)
  * `pandas`
  * `openpyxl`

Install dependencies:

```bash
pip install pymupdf pandas openpyxl
```

---

## ▶️ How to Run

### **1. Extract text from PDF**

Edit the paths in `#1create_txt.py`:

```python
pdf_path = "path/to/your_file.pdf"
output_file_path = "1-ass-social.txt"
```

Run:

```bash
python #1create_txt.py
```

---

### **2. Clean the text**

```bash
python #2treat-data.py
```

This updates the `.txt` file with cleaned and normalized content.

---

### **3. Build structured employee records**

```bash
python #3create-table.py
```

---

### **4. Generate the Excel spreadsheet**

Edit the output path in `#4create_excel.py` if needed:

```python
output_file_path = "payroll_employees.xlsx"
```

Run:

```bash
python #4create_excel.py
```

---

## 📈 Future Improvements

* Support for multiple PDFs in batch
* Detection of additional payroll fields
* Automatic validation and error checking
* Dashboard integration (Power BI, Streamlit, etc.)
* Merge datasets from different periods

---

## 🎯 Purpose

This project transforms unstructured payroll documents into clean, analysis-ready datasets using automation and Python.
It demonstrates practical experience in:

* text processing and PDF extraction
* data cleaning and normalization
* data structuring and parsing logic
* automation for finance and HR workflows
* dataset preparation for financial modeling

