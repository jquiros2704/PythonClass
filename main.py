"""
Link del video
https://ufidelitas-my.sharepoint.com/:v:/g/personal/jquiros30250_ufide_ac_cr/EZYzLXUdMaxMoZAhi9k49r0Bt25RS8BOU8WaW6tbW7orYA?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=Wj2qs9
"""
# Pin necesario para crear una cuenta administrador: 79743
from utils import cargar_usuarios, registrar_usuario, verificar_usuario
from usuario import Administrador, Comprador
from factura import Factura  # Importar la clase Factura

inventario = {
    "Balones de fútbol": {"costo": 30000, "cantidad": 50},
    "Raquetas de tenis": {"costo": 55000, "cantidad": 30},
    "Mancuernas": {"costo": 15000, "cantidad": 100},
    "Bicicletas": {"costo": 150000, "cantidad": 10},
    "Guantes de boxeo": {"costo": 40000, "cantidad": 40}
}

def mostrar_inventario():
    print("---------------------------")
    print("Inventario:")
    for idx, (producto, detalles) in enumerate(inventario.items(), 1):
        print(f'{idx}. {producto} (costo: {detalles["costo"]} colones, cantidad: {detalles["cantidad"]})')
    print()

def seleccionar_producto():
    while True:
        seleccion = input("Selecciona el número del producto: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(inventario):
            return list(inventario.keys())[int(seleccion) - 1]
        else:
            print("Selección no válida. Por favor, intenta de nuevo.")

def main():
    cargar_usuarios()
    factura = Factura()
    while True:
        print("---------------------------")
        opcion = input("¿Deseas (1) Iniciar sesión, (2) Registrarte o (3) Salir del programa? Ingresa el número correspondiente: ")
        if opcion == '1':
            usuario = verificar_usuario()
            if usuario:
                while True:
                    print("---------------------------")
                    if usuario.rol == 'Administrador':
                        print("1. Ver inventario")
                        print("2. Editar inventario")
                    else:
                        print("1. Ver inventario")
                        print("2. Comprar producto")
                    print("3. Regresar al menú principal")
                    
                    opcion_usuario = input("Selecciona una opción: ")
                    
                    if opcion_usuario == '1':
                        mostrar_inventario()
                        input("Presiona Enter para regresar al menú...")
                    elif opcion_usuario == '2':
                        mostrar_inventario()
                        producto = seleccionar_producto()
                        if usuario.rol == 'Administrador':
                            while True:
                                cantidad = input(f'Ingresa la nueva cantidad para {producto}: ')
                                if cantidad.isdigit():
                                    inventario[producto]["cantidad"] = int(cantidad)
                                    print(f'Cantidad actualizada: {producto} ahora tiene {cantidad} unidades.')
                                    break
                                else:
                                    print("Entrada inválida. Por favor, ingresa un número válido.")
                        else:
                            while True:
                                cantidad = input(f'Ingresa la cantidad de {producto} que deseas comprar: ')
                                if cantidad.isdigit():
                                    cantidad = int(cantidad)
                                    if cantidad <= inventario[producto]["cantidad"]:
                                        total = cantidad * inventario[producto]["costo"]
                                        inventario[producto]["cantidad"] -= cantidad
                                        print(f'Compra exitosa! Total a pagar: {total} colones.')
                                        factura.agregar_compra(producto, cantidad, total)
                                        break
                                    else:
                                        print("Cantidad no disponible en el inventario.")
                                else:
                                    print("Entrada inválida. Por favor, ingresa un número válido.")
                        input("Presiona Enter para regresar al menú...")
                    elif opcion_usuario == '3':
                        break
                    else:
                        print("Opción no válida.")
        elif opcion == '2':
            registrar_usuario()
        elif opcion == '3':
            if factura.compras:
                factura.generar_factura()
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
