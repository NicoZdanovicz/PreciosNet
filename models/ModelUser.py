from .entities.User import User, Productos, Comercios

class ModelUser():

    @classmethod
    def login(self,db,user):
        try:
            cursor= db.connection.cursor()
            sql="""SELECT id, usuario, correo, contraseña, rol FROM usuarios
                    WHERE usuario = '{}' """.format(user.usuario)
            cursor.execute(sql)
            row=cursor.fetchone()
            
            if row != None:
                user= User(row[0],row[1],row[2],User.check_contraseña(row[3], user.contraseña),row[4])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_by_id(self,db,id):
        try:
            cursor= db.connection.cursor()
            sql="""SELECT id, usuario, correo, rol FROM usuarios
                    WHERE id = '{}' """.format(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            
            if row != None:
                return User(row[0],row[1],row[2],None,row[3])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def registro(self,db,user):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO usuarios (usuario, correo, contraseña, rol) 
                     VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql, (user.usuario, user.correo, user.contraseña, user.rol))
            db.connection.commit()
            return user
            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def producto(self,db,productos):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO productos (producto, marca, local, peso, precio, descripcion, verificado) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            
            cursor.execute(sql, (productos.producto, productos.marca, productos.local, productos.peso, productos.precio, productos.descripcion, productos.verificado))
            db.connection.commit()
            return productos
            
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def get_productos(self,db):
        try:
            cursor= db.connection.cursor()
            sql="""SELECT id, producto, marca, local, peso, precio, descripcion, verificado FROM productos WHERE verificado = 0"""
            cursor.execute(sql)
            rows=cursor.fetchall()
            producto = []

            for row in rows:
                producto.append(Productos(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
            return producto
            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod   
    def del_producto(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM productos WHERE id = %s"
            cursor.execute(sql, (id,))  # Asegúrate de que el id se pase como una tupla
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def confirmar_producto(self, db, producto):
        try:
            cursor = db.connection.cursor()
            sql = """UPDATE productos SET producto = %s, marca = %s, local = %s, peso = %s, precio = %s, descripcion = %s, verificado = %s WHERE id = %s"""
            cursor.execute(sql, (producto.producto, producto.marca, producto.local, producto.peso, producto.precio, producto.descripcion, producto.verificado, producto.id))
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def comercio(self,db,comercios):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO comercios (nombre, direccion, descripcion) 
                    VALUES (%s, %s, %s)"""
            
            cursor.execute(sql, (comercios.nombre, comercios.direccion, comercios.descripcion))
            db.connection.commit()
            return comercios
            
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_comercios(self,db):
        try:
            cursor= db.connection.cursor()
            sql="""SELECT id, nombre, direccion, descripcion FROM comercios"""
            cursor.execute(sql)
            rows=cursor.fetchall()
            comercio = []

            for row in rows:
                comercio.append(Comercios(row[0], row[1], row[2], row[3]))
            return comercio
            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod   
    def del_comercio(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM comercios WHERE id = %s"
            cursor.execute(sql, (id,))  # Asegúrate de que el id se pase como una tupla
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)