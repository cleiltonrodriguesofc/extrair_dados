# Payroll Data Extraction and Processing Pipeline

This project automates the extraction, cleaning, and structuring of payroll data originally stored in PDF documents.  
The system converts raw payroll PDFs into a clean, standardized Excel spreadsheet containing fields such as **Registration Number**, **Name**, **Position**, **CPF**, **Admission Date**, and **Admission Type**.

It was created for analytical use cases such as:

- financial impact assessments;
- HR audits;
- payroll consolidation;
- public-sector financial analysis;
- modeling and decision-support workflows.

---

## 📂 Project Structure

### `#1create_txt.py`
Extracts all text from a payroll PDF using **PyMuPDF (fitz)** and saves it into a raw `.txt` file.  
:contentReference[oaicite:0]{index=0}

### `#2treat-data.py`
Cleans and normalizes the text file by removing headers/footers, system metadata, and fixing encoding issues (broken accents, inconsistent field names, etc.).  
Also removes suffixes like `| 082020 | 700 | EN` commonly attached to job titles.  
:contentReference[oaicite:1]{index=1}

### `#3create-table.py`
Parses the cleaned text and extracts structured information for each employee, identifying and grouping fields such as Registration Number, Name, Position, CPF, Admission Date, and Admission Type.  
Output is a structured `.txt` with consistent “key: value” formatting.  
:contentReference[oaicite:2]{index=2}

### `#4create_excel.py`
Reads the structured `.txt` file and converts it into an Excel spreadsheet using **pandas** + **openpyxl**, generating a clean table ready for financial or HR analysis.  
:contentReference[oaicite:3]{index=3}

---

## 🔁 Processing Pipeline

### 1. **PDF → Raw Text**
- Extracts full text from the payroll PDF.
- Produces an intermediate file such as `1-ass-social.txt`.  
:contentReference[oaicite:4]{index=4}

### 2. **Raw Text → Cleaned Text**
- Removes irrelevant lines (headers, timestamps, resource codes, logged user data).  
- Fixes encoding errors (`MatrÃ­cula` → `Matricula`, `AdmissÃ£o` → `Admissao`, etc.).  
- Removes suffixes and standardizes field names.  
:contentReference[oaicite:5]{index=5}

### 3. **Cleaned Text → Structured Employee Records**
- Searches for the `Matricula` keyword to identify employee blocks.
- Collects related fields using positional rules.  
- Produces structured lines such as:  
```text
Matricula: 0105994.05
Name: EMPLOYEE NAME
Cargo: AGENTE ADMINISTRATIVO
CPF: 027.773.893-81
Admissao: 14/01/2011
Forma de Admissao: EFETIVO
