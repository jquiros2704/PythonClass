
class Factura:
    def __init__(self):
        self.compras = []

    def agregar_compra(self, producto, cantidad, total):
        self.compras.append((producto, cantidad, total))

    def generar_factura(self):
        print("="*40)
        print(" " * 12 + "FACTURA FINAL")
        print("="*40)
        print("{:<20} {:<10} {:<10}".format("Producto", "Cantidad", "Total"))
        print("-"*40)
        
        total_final = 0
        for compra in self.compras:
            producto, cantidad, total = compra
            print("{:<20} {:<10} {:<10}".format(producto, cantidad, total))
            total_final += total
        
        print("-"*40)
        print("{:<20} {:<10} {:<10}".format("", "Total a pagar:", total_final))
        print("="*40)

