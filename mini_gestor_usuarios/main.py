from usuario import Usuario
import utils


Usuario = []

def menu():
    print("\ Gestor de Usuarios")
    print("1. Crear usuario")
    print("2. Mostrar usuarios")
    print("3. Modificar email de un usuario")
    print("4. Salir")

try:
    while True:
        menu()
        opcion = input("Selecciona una opcion:")
        if opcion == "1":

