from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id, usuario, correo, contraseña, rol) -> None:
        self.id = id
        self.usuario = usuario
        self.correo = correo
        self.contraseña = contraseña
        self.rol = rol

    @classmethod
    def check_contraseña(self,check_contraseña, contraseña):
        return check_contraseña == contraseña

class Register():

    def __init__(self, usuario, correo, contraseña, rol) -> None:
        self.usuario = usuario
        self.correo = correo
        self.contraseña = contraseña
        self.rol = rol

class Productos():
    
        def __init__(self, id, producto, marca, local, peso, precio, descripcion, verificado) -> None:
            self.id = id
            self.producto = producto
            self.marca = marca
            self.local = local
            self.peso = peso
            self.precio = precio
            self.descripcion = descripcion
            self.verificado = verificado

class Comercios():

    def __init__(self, id, nombre, direccion, descripcion) -> None:
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.descripcion = descripcion