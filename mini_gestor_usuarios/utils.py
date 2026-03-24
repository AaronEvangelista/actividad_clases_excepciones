def pedir_nombre():
    while True:
        nombre = input("Ingrese el nombre del usuario:")  
        if nombre_valido(nombre):
            return nombre
        print("Nombre no es valido")
        
def pedir_edad():
    while True:
        try:
            edad = int(input("Ingrese la edad del usuario:"))
            if edad > 0:
                return edad
            print("La edad debe ser un numero entero mayor que 0.")
        except ValueError:
            print("edad no valida")


def pedir_email():
    while True:
        email = input("Ingrese el email del usuario:")
        if email_valido(email):
            return email
        print("Email no valido")





