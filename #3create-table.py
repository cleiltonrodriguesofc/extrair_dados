# def function to extract text from a file and create a new text file

def workers_list(path_file: str, path_output_file: str) -> list:
    """
    Extract text from a file and create a new text file with the workers list.

    Args:
        path_file (str): The path to the input file.
        path_output_file (str): The path to the output file.

    Returns:
        list: A list with the workers information.
    """
    with open(path_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        workers = []
        for index, line in enumerate(lines):
            if 'Matricula' in line:
                worker = {}
                # put matricula
                target_index = index + 6
                if target_index < len(lines):
                    worker['matricula'] = lines[target_index].strip()
                else:
                    print("Target line is out of range")
                
                # put name 
                target_index = index - 2
                if target_index >= 0:
                    worker['name'] = lines[target_index].strip()
                workers.append(worker)

                # put cargo
                target_index = index - 1
                if target_index >= 0:
                    worker['cargo'] = lines[target_index].strip()
                else:
                    print("Target line is out of range")
            
            
            elif 'CPF' in line:
                target_index = index + 6
                if target_index < len(lines):
                    if workers:  # check if workers list is not empty
                        workers[-1]['cpf'] = lines[target_index].strip()
                    else:
                        print("No worker found to add CPF")
                else:
                    print("Target line is out of range")

            elif 'Admissao' in line:
                target_index = index + 5
                if target_index < len(lines):
                    worker['admissao'] = lines[target_index].strip()
                else:
                    print("Target line is out of range")
                
                # put forma de admissão
                target_index = index + 6
                if target_index < len(lines):
                    worker['forma de admissao'] = lines[target_index].strip()
                else:
                    print("Target line is out of range")

    # write workers list to output file
    with open(path_output_file, 'w', encoding='utf-8') as file:
        try:
            for worker in workers:
                
                file.write(f"Matricula: {worker['matricula']}\n")
                file.write(f"Name: {worker['name']}\n")
                file.write(f"Cargo: {worker['cargo']}\n")
                file.write(f"CPF: {worker['cpf']}\n")
                file.write(f"Admissao: {worker['admissao']}\n")
                file.write(f"Forma de Admissao: {worker['forma de admissao']}\n")
                file.write("\n")
        except Exception as e:
            print(f"Error: {e}")
    
# call the function
file_path = '3-fundeb.txt'
output_file_path = file_path


workers_list(file_path, output_file_path)

