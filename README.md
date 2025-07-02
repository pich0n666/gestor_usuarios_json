# Gestor de Usuarios (Python + JSON)

Este es un proyecto simple en Python que permite gestionar una lista de usuarios utilizando un archivo JSON como base de datos.

## Funcionalidades

- Agregar usuarios con nombre, edad y email
- Ver todos los usuarios y su historial
- Editar la edad de un usuario
- Eliminar usuarios
- Guardado automático en archivo JSON
- Modularizado: código separado en varios archivos

## Estructura del proyecto
gestor_usuarios_json/
├── main.py # Menú y programa principal
├── usuarios.py # Funciones de lógica del usuario
├── utils.py # Lectura y escritura de JSON
├── usuarios.json # Archivo con los datos (se genera en ejecución)
└── README.md # Esta descripción
## Cómo ejecutar

1. Instalá Python 3 desde [python.org](https://www.python.org/)
2. Abrí una terminal y ejecutá:

```bash
python main.py
