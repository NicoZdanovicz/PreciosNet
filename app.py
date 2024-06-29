from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

from models.ModelUser import ModelUser
from models.entities.User import User, Register, Productos, Comercios

from flask_mysqldb import MySQL

app = Flask(__name__)

db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)



@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0,request.form['usuario'],0,request.form['contraseña'],0)
        logged_user = ModelUser.login(db,user)
        
        if logged_user != None:
            if logged_user.contraseña:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña incorrecta")
        else:
            flash("Usuario no encontrado")
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():

    

    return render_template('home.html')



@app.route('/productos', methods=['GET', 'POST'])
def productos():

    if request.method == 'POST':
        producto = request.form['producto']
        marca = request.form['marca']
        local = request.form['local']
        peso = request.form['peso']
        precio = request.form['precio']
        descripcion = request.form['descripcion']
        
        productos = Productos(0, producto, marca, local, peso, precio, descripcion, 0)

        try:
            ModelUser.producto(db, productos)
            flash("Producto Cargado con Exito")

            return redirect('productos')
        except Exception as ex:
            flash("Error al cargar el Producto")
            return redirect('productos')
        
   
    comercios = ModelUser.get_comercios(db)
    return render_template('productos.html', comercios=comercios)

@app.route('/comercios', methods=['GET', 'POST'])
def comercios():   
    comercios = ModelUser.get_comercios(db)
    if request.method == 'POST':
        if 'delete_id_com' in request.form: # Detecta si es una solicitud de borrar
            id = request.form['delete_id_com']
            ModelUser.del_comercio(db, id)
            return redirect('comercios')
        else:
            comercio = request.form['nombre']
            direccion = request.form['direccion']
            descripcion = request.form['descripcion']
            comercios = Comercios(0, comercio, direccion, descripcion)
            ModelUser.comercio(db, comercios)
            return redirect('comercios')
    else:

        return render_template('comercios.html', comercios=comercios)

@app.route('/estadisticas', methods=['GET', 'POST'])
def estadisticas():   

    return render_template('estadisticas.html')

@app.route('/verproductos', methods=['GET', 'POST'])
def verproductos():   
    productos = ModelUser.get_productos(db)

    if request.method == 'POST':
        if 'delete_id' in request.form: # Detecta si es una solicitud de borrar
            id = request.form['delete_id']
            ModelUser.del_producto(db, id)
            return redirect('verproductos')
        
        elif 'confirm_id' in request.form:  # Detecta si es una solicitud de edición
            confirm_id = request.form['confirm_id']
            confirm_producto = request.form['confirm_producto']
            confirm_marca = request.form['confirm_marca']
            confirm_local = request.form['confirm_local']
            confirm_peso = request.form['confirm_peso']
            confirm_precio = request.form['confirm_precio']
            confirm_descripcion = request.form['confirm_descripcion']
            confirm_validacion = request.form['confirm_validacion']
            producto = Productos(confirm_id, confirm_producto, confirm_marca, confirm_local, confirm_peso, confirm_precio, confirm_descripcion, confirm_validacion)
            ModelUser.confirmar_producto(db, producto)
            return redirect('verproductos')
        
    return render_template('verproductos.html', productos=productos)

@app.route('/recompensas', methods=['GET', 'POST'])
def recompensas():   

    return render_template('recompensas.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        usuario = request.form['nombre']
        correo = request.form['correo']
        contraseña = request.form['password']
        rol = request.form['rol']

        
        user = Register(usuario, correo, contraseña, rol)

        try:
            ModelUser.registro(db, user)
            return redirect(url_for('login'))
        except Exception as ex:
            flash("Usuario o Correo ya registrado")
            
            return render_template('registro.html')
    return render_template('registro.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

def status_401(error):
    return redirect(url_for('login'))
    

def status_404(error):
    return "<h1>La pagina no existe</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()