def agregar(usuarios):
    """
    Solicita datos al usuario por consola y agrega un nuevo usuario a la lista.
    
    Args:
        usuarios (list): Lista actual de usuarios.
    """
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    email = input("Email: ")
    nuevo = {
        "nombre": nombre,
        "edad": edad,
        "email": email,
        "historial": ["Usuario creado"]
    }
    usuarios.append(nuevo)

def ver(usuarios):
    """
    Muestra todos los usuarios registrados y sus historiales.

    Args:
        usuarios (list): Lista actual de usuarios.
    """
    if not usuarios:
        print("No hay usuarios.")
        return
    for i, u in enumerate(usuarios, 1):
        print(f"{i}. {u['nombre']} - {u['edad']} años - {u['email']}")
        for h in u["historial"]:
            print(f"   • {h}")

def editar(usuarios):
    """
    Permite modificar la edad de un usuario existente.
    
    Args:
        usuarios (list): Lista actual de usuarios.
    """
    nombre = input("Nombre a editar: ")
    for u in usuarios:
        if u["nombre"] == nombre:
            nueva = int(input("Nueva edad: "))
            u["edad"] = nueva
            u["historial"].append(f"Edad cambiada a {nueva}")
            return
    print("Usuario no encontrado.")

def eliminar(usuarios):
    """
    Elimina un usuario de la lista según su nombre.
    
    Args:
        usuarios (list): Lista actual de usuarios.
    """
    nombre = input("Nombre a eliminar: ")
    for u in usuarios:
        if u["nombre"] == nombre:
            usuarios.remove(u)
            return
    print("Usuario no encontrado.")