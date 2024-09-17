class Usuario:
    def __init__(self, nombre, apellido, correo, contraseña, rol):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña
        self.rol = rol
    
    def atributos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'Correo: {self.correo}')
        print(f'Contraseña: {self.contraseña}')
        print(f'Rol: {self.rol}')

    def to_string(self):
        return f'{self.nombre},{self.apellido},{self.correo},{self.contraseña},{self.rol}'

    @staticmethod
    def from_string(data):
        nombre, apellido, correo, contraseña, rol = data.split(',')
        return Usuario(nombre, apellido, correo, contraseña, rol)

class Administrador(Usuario):
    def __init__(self, nombre, apellido, correo, contraseña):
        super().__init__(nombre, apellido, correo, contraseña, rol='Administrador')

    def editar_inventario(self, inventario):
        print("Editar Inventario:")
        for producto, detalles in inventario.items():
            print(f'{producto} (costo: {detalles["costo"]} colones, cantidad: {detalles["cantidad"]})')
        producto = input("Ingresa el nombre del producto que deseas editar: ")
        if producto in inventario:
            while True:
                cantidad = input(f'Ingresa la nueva cantidad para {producto}: ')
                if cantidad.isdigit():
                    inventario[producto]["cantidad"] = int(cantidad)
                    print(f'Cantidad actualizada: {producto} ahora tiene {cantidad} unidades.')
                    break
                else:
                    print("Entrada inválida. Por favor, ingresa un número válido.")
        else:
            print("Producto no encontrado en el inventario.")

class Comprador(Usuario):
    def __init__(self, nombre, apellido, correo, contraseña):
        super().__init__(nombre, apellido, correo, contraseña, rol='Comprador')

    def comprar(self, inventario):
        print("Productos disponibles:")
        for producto, detalles in inventario.items():
            print(f'{producto} (costo: {detalles["costo"]} colones, cantidad: {detalles["cantidad"]})')
        
        producto = input("Ingresa el nombre del producto que deseas comprar: ")
        if producto in inventario:
            while True:
                cantidad = input(f'Ingresa la cantidad de {producto} que deseas comprar: ')
                if cantidad.isdigit():
                    cantidad = int(cantidad)
                    if cantidad <= inventario[producto]["cantidad"]:
                        total = cantidad * inventario[producto]["costo"]
                        inventario[producto]["cantidad"] -= cantidad
                        print(f'Compra exitosa! Total a pagar: {total} colones.')
                        print(f'Factura: {cantidad}x {producto} = {total} colones')
                        break
                    else:
                        print("Cantidad no disponible en el inventario.")
                else:
                    print("Entrada inválida. Por favor, ingresa un número válido.")
        else:
            print("Producto no encontrado en el inventario.")
