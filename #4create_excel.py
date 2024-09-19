import pandas as pd
import re

# create a empty dict to store data
data = dict()

# def function to treat table
def create_table(file_path):
    """
    Read a text file and create an Excel file based on it, with six columns: Matricula, Name, Cargo, CPF, Admissao, Forma de Admissao.
    
    Parameters
    ----------
    file_path : str
        The full path to the text file to be read.
    
    Returns
    -------
    None
    """
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.match(r'^(Matricula|Name|Cargo|CPF|Admissao|Forma de Admissao): (.*)$', line)
            if match:
                key = match.group(1)
                value = match.group(2).strip()
                if key not in data:
                    data[key] = []
                data[key].append(value)
    
    df = pd.DataFrame(data)
    df.to_excel(output_file_path, engine='openpyxl', index=False, header=True)
    print('File created successfully!')

          
    
file_path = '3-fundeb.txt'
output_file_path = '3-fundeb.xlsx'
create_table(file_path)
