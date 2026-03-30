# aaron evangelista - daw
class Usuario:
    # datos no se modifiquen desde fuera Solo se cambian usando Getters y Setters.
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
            raise ValueError("El nombre no puede estar vacio")
        self.__nombre = nombre

    def set_edad(self, edad):
        try:
            edad_int = int(edad)  # Convertimos el texto del input a numero entero
        except ValueError:
            # Si escriben letras lanzamos nuestro propio mensaje de error
            raise ValueError("La edad debe ser un numero entero")
            
        if edad_int <= 0:
            raise ValueError("La edad tiene que ser mayor que 0")
            
        self.__edad = edad_int

    def set_email(self, email):
        if "@" not in email or "." not in email:
            raise ValueError("Error el email debe contener @ y .")
        self.__email = email

    # Este metodo __str__ sirve para que cuando imprimamos al usuario con print()

    def __str__(self):
        return f"Usuario: {self.__nombre} | Edad: {self.__edad} | Email: {self.__email}"
