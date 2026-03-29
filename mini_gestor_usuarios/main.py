#aaron evangelista - daw
from usuario import Usuario
import utils

usuarios = []

def menu():
    print("\n--- Gestor de Usuarios ---")
    print("1. Crear usuario")
    print("2. Mostrar usuarios")
    print("3. Modificar email de un usuario")
    print("4. Salir")

while True:
    menu()
    opcion = input("Selecciona una opcion: ")
    
    if opcion == "1":
        # else se ejecuta si todo sale bien y finally se ejecuta siempre al terminar y
        # try/except para validar que el indice sea correcto
        try:
            nombre = utils.pedir_nombre()
            edad = utils.pedir_edad()
            email = utils.pedir_email()
            
            # para hacer validacion del nuevo usuario
            nuevo_user = Usuario(nombre, edad, email)
            
        except ValueError as e:
            print(f"\nError de datos: {e}")
        except Exception as e:
            print(f"\nError inesperado: {e}")
        else:
            usuarios.append(nuevo_user)
            print("\nUsuario creado con exito")
            
    elif opcion == "2":
        if len(usuarios) == 0:
            print("\nNo hay usuarios en la lista")
        else:
            print("\nLista de Usuarios")
            for i, u in enumerate(usuarios):
                print(f"[{i}] {u}")
                
    elif opcion == "3":
        if len(usuarios) == 0:
            print("\nNo hay usuarios para modificar.")
            continue
            
        for i, u in enumerate(usuarios):
            print(f"[{i}] {u}")
            
        try:
            indice = int(input("\nIngresa el numero del usuario a modificar: "))
            
            if indice < 0 or indice >= len(usuarios):
                print("Error Ese numero de usuario no existe")
                continue
                
            nuevo_email = utils.pedir_email()
            usuarios[indice].set_email(nuevo_email)
            
        except ValueError as e:
            print(f"\nError de datos: {e}")
        except Exception as e:
            print(f"\nError inesperado: {e}")
        else:
            print("\nEmail actualizado con exito")
        finally:
            print("Fin de la modificacion de email")
            
    elif opcion == "4":
        print("\nSaliendo del programa")
        break
        
    else:
        print("\nOpcion no valida")