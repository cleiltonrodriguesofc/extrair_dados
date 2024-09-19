'''Import especific lines from a file'''
'''
AGENTE ADMINISTRATIVO | 082020 | 700 | EN
Matrícula
CPF
Admissão
Forma de Admissão
Turno
Situação
0105994.05
027.773.893-81
14/01/2011
EFETIVO
40 Horas Semanais
ATIVO'''

# create a function to extract text from a file and create a new text file
def extract_text_from_file(file_path: str, output_file_path: str) -> None:
    """
    Extracts all text from the given file and writes it to a new file.

    :param file_path: The path to the file to extract text from.
    :param output_file_path: The path to the new file to write the text to.
    :return: None
    """
    # list to lines
    lines = []
    
    with open(file_path, 'r') as file:
        lines = file.read()
    with open(output_file_path, 'w', encoding='utf-8') as file:
        # remove especific lines
        remove_lines = ['PerÃ­odo AGOSTO/2020 | Folha 700 - SEMED_MDE0',
                        'Secretaria Municipal de EducaÃ§Ã£o',
                        'Secretaria Municipal de EducaÃ§Ã£o',
                        'Data: 01/09/2020 | 12:46:17',
                        'PerÃ­odo AGOSTO/2020 | Folha 700 - SEMED_MDE',
                        'Rua SÃ£o Raimundo, 1',
                        'FAC001',
                        'Buriticupu/MA',
                        'Periodo Logado: AGOSTO/2020:100',
                        '01.612.525/0001-40',
                        'UsuÃ¡rio Logado: [18]. VIVIANE',
                        'Folha AnalÃ­tica ContÃ¡bil | NSA 2315',
                        'Grupo de Recursos: 700 - SEMED_MDE',
                        'Fonte de Recursos: O95 - MDE_OP. CONCURSADOS (5832-7)'
                        ]


        # replace specific words with other words
        for line in lines.splitlines():
            if 'MatrÃ­cula' in line:
                line = line.replace('MatrÃ­cula', 'Matricula', 1)
            elif 'AdmissÃ£' in line:
                line = line.replace('AdmissÃ£o', 'Admissao', 1)
            elif 'Forma de AdmissÃ£o' in line:
                line = line.replace('Forma de AdmissÃ£o', 'Forma de Admissao', 1)
            elif 'SituaÃ§Ã£o' in line:
                line = line.replace('SituaÃ§Ã£o', 'Situacao', 1)

            # identify function and remove suffix
           
            elif '| 082020 | 700 | EN' or '| 082020 | 400 | EN' or '| 082020 | 200 | EN' or '| 082020 | 300 | EN' or '| 082020 | 100 | EN' in line:
                line = line.removesuffix('| 082020 | 700 | EN') and line.removesuffix('| 082020 | 400 | EN') and line.removesuffix('| 082020 | 200 | EN') and line.removesuffix('| 082020 | 300 | EN') and line.removesuffix('| 082020 | 100 | EN')
                
            # remove lines
            elif line  in remove_lines:
                continue
        
            file.write(line + '\n')
               
# call the function
file_path = '3-fundeb.txt'
output_file_path = file_path

extract_text_from_file(file_path, output_file_path)

