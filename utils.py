import os
from usuario import Usuario

# Archivo donde se guardarán los usuarios
archivo_usuarios = 'usuarios.txt'

# Lista para almacenar los usuarios registrados
usuarios_registrados = []

def cargar_usuarios():
    if os.path.exists(archivo_usuarios):
        with open(archivo_usuarios, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    usuarios_registrados.append(Usuario.from_string(line))

def guardar_usuario(usuario):
    with open(archivo_usuarios, 'a') as file:
        file.write(usuario.to_string() + '\n')

def registrar_usuario():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    
    while True:
        correo = input("Ingresa tu correo: ")
        if "@" not in correo:
            print("Correo inválido. Por favor, ingresa un correo válido.")
        elif any(usuario.correo == correo for usuario in usuarios_registrados):
            print("Este correo ya está registrado. Por favor, ingresa un correo diferente.")
        else:
            break
    
    contraseña = input("Ingresa tu contraseña: ")
    
    print("Selecciona el rol del usuario:")
    print("1. Administrador")
    print("2. Comprador")
    rol = input("Ingresa el número correspondiente: ")
    
    if rol == '1':
        pin = input("Ingresa el pin para crear una cuenta Administrador: ")
        if pin == '79743':
            rol = 'Administrador'
        else:
            print("Pin incorrecto. No puedes crear una cuenta Administrador.")
            return
    elif rol == '2':
        rol = 'Comprador'
    else:
        print("Opción no válida. Registrando como Comprador por defecto.")
        rol = 'Comprador'
    
    nuevo_usuario = Usuario(nombre, apellido, correo, contraseña, rol)
    usuarios_registrados.append(nuevo_usuario)
    guardar_usuario(nuevo_usuario)
    print(f"Usuario registrado exitosamente como {rol}!")

def verificar_usuario():
    correo = input("Ingresa tu correo para verificar: ")
    contraseña = input("Ingresa tu contraseña para verificar: ")
    
    for usuario in usuarios_registrados:
        if usuario.correo == correo and usuario.contraseña == contraseña:
            print(f"Bienvenido de nuevo {usuario.nombre}!")
            usuario.atributos()
            return usuario  # Devolver el objeto Usuario
    print("Usuario no encontrado. Por favor, regístrate.")
    return None  # Devolver None si no se encuentra el usuario
