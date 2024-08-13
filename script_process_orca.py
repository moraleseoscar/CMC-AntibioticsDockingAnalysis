import os
import subprocess
import sys

def create_smiles_and_run_orca(name, sequence):
    # Crear la carpeta con el nombre especificado
    os.makedirs(name, exist_ok=True)
    
    # Crear el archivo .smiles y escribir la secuencia
    smiles_file_path = os.path.join(name, f"{name}.smiles")
    with open(smiles_file_path, 'w') as smiles_file:
        smiles_file.write(sequence)
    
    # Comando para convertir el archivo .smiles a .orcainp usando Open Babel
    orcainp_file_path = os.path.join(name, f"{name}.orcainp")
    command = f"obabel {smiles_file_path} -O {orcainp_file_path} -xk \"!B3LYP def2-SVP Opt\" --gen3d"
    
    # Ejecutar el comando para generar el archivo .orcainp
    subprocess.run(command, shell=True, check=True)
    
    print(f"Archivo {name}.orcainp creado en la carpeta {name}.")
    
    # Crear la carpeta para los archivos de salida de ORCA
    orca_output_dir = os.path.join(name, f"{name}_orca_files")
    os.makedirs(orca_output_dir, exist_ok=True)
    
    # Comando para correr ORCA y redirigir la salida a la carpeta correspondiente
    orca_command = f"orca {orcainp_file_path} > {os.path.join(orca_output_dir, f'{name}.out')}"
    
    print(f"Ejecutando optimización con ORCA...")
    
    # Ejecutar el comando ORCA
    subprocess.run(orca_command, shell=True, check=True)
    
    print(f"Cálculo de ORCA completado. Archivos generados en la carpeta {orca_output_dir}.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script_process_orca.py <nombre> <secuencia>")
        sys.exit(1)
    
    nombre = sys.argv[1]
    secuencia = sys.argv[2]
    
    create_smiles_and_run_orca(nombre, secuencia)
