from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "<h1>Biblioteca Virtual</h1><p>Consulta nuestro catálogo de libros aquí.</p>"

@app.route('/libro/<titulo>')
def buscar_libro(titulo):
    return f"<h1>Libro: {titulo}</h1><p>El libro se encuentra disponible para préstamo.</p>"

if __name__ == '__main__':
    app.run(debug=True)git init


from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from Conexion.conexion import conectar
from models import Usuario

app = Flask(__name__)
app.secret_key = 'llave_secreta_biblioteca' # Esto protege la sesión

# --- CONFIGURACIÓN DE LOGIN ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # Si alguien no entra, lo mandamos aquí

@login_manager.user_loader
def load_user(user_id):
    db = conectar()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    db.close()
    if user:
        return Usuario(user['id_usuario'], user['nombre'], user['email'])
    return None

# --- RUTA DE LOGIN (Para entrar) ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        db = conectar()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email=%s AND password=%s", (email, password))
        user_data = cursor.fetchone()
        cursor.close()
        db.close()

        if user_data:
            user_obj = Usuario(user_data['id_usuario'], user_data['nombre'], user_data['email'])
            login_user(user_obj)
            return redirect(url_for('index'))
        else:
            return "Correo o contraseña incorrectos"
            
    return render_template('login.html')

# --- RUTA PROTEGIDA (Solo para logueados) ---
@app.route('/')
@login_required
def index():
    return f"<h1>Bienvenido, {current_user.nombre}</h1><p>Esta es la biblioteca privada.</p><a href='/logout'>Salir</a>"

# --- RUTA PARA SALIR ---
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))








