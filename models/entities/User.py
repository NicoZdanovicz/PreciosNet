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
    
        def __init__(self, producto, marca, local, peso, precio, descripcion) -> None:
            self.producto = producto
            self.marca = marca
            self.local = local
            self.peso = peso
            self.precio = precio
            self.descripcion = descripcion