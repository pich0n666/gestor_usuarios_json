import json
import os

ARCHIVO = "usuarios.json"

def cargar_datos():
    """
    Carga los datos del archivo JSON. 
    Si el archivo no existe o está dañado, devuelve una lista vacía.
    
    Returns:
        list: Lista de usuarios (cada uno es un diccionario).
    """
    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def guardar_datos(usuarios):
    """
    Guarda la lista de usuarios en un archivo JSON con formato legible.

    Args:
        usuarios (list): Lista de diccionarios que representan los usuarios.
    """
    with open(ARCHIVO, "w") as f:
        json.dump(usuarios, f, indent=2)