from utils import cargar_datos, guardar_datos
import usuarios

def menu():
    """
    Muestra el menú principal por consola y solicita una opción al usuario.

    Returns:
        str: Opción ingresada por el usuario.
    """
    print("\n--- Gestor de Usuarios ---")
    print("1. Agregar")
    print("2. Ver")
    print("3. Editar edad")
    print("4. Eliminar")
    print("5. Guardar y salir")
    return input("Opción: ")

def main():
    """
    Ejecuta el bucle principal del programa.
    Maneja el flujo entre menú, funciones del usuario y guardado de datos.
    """
    data = cargar_datos()
    while True:
        op = menu()
        if op == "1":
            usuarios.agregar(data)
        elif op == "2":
            usuarios.ver(data)
        elif op == "3":
            usuarios.editar(data)
        elif op == "4":
            usuarios.eliminar(data)
        elif op == "5":
            guardar_datos(data)
            print("Cambios guardados. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()