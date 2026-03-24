
class Usuario:

    def __init__(self, nombre, edad, email):
        self.__nombre = None
        self.__edad = None
        self.__email = None

        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_email(email)

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_email(self):
        return self.__email

    def set_nombre(self, nombre):

        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio.")

        self.__nombre = nombre

    def set_edad(self, edad):

        if not isinstance(edad, int) or edad <= 0:
            raise ValueError("La edad tiene que ser mayor que 0")

        self.__edad = edad

    def set_email(self, email):

        if "@" not in email or "." not in email:
            raise ValueError("No tiene @")

        self.__email = email

    def __str__(self):
        return f"Usuario: {self.__nombre} | Edad: {self.__edad} | Email: {self.__email}"
    
