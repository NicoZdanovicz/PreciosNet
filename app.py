from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

from models.ModelUser import ModelUser
from models.entities.User import User, Register, Productos

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

    if request.method == 'POST':
        producto = request.form['producto']
        marca = request.form['marca']
        local = request.form['local']
        peso = request.form['peso']
        precio = request.form['precio']
        descripcion = request.form['descripcion']
        
        user = Productos(producto, marca, local, peso, precio, descripcion)

        try:
            ModelUser.producto(db, user)
            flash("Producto Cargado con Exito")
            return redirect('home')
        except Exception as ex:
            flash("Error al cargar el Producto")
            return redirect('home')
    return render_template('home.html')

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