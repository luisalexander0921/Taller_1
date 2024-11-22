from flask import Flask, request, redirect, url_for, render_template, session, flash
from models.user import usuarios, obtener_usuario_por_username

app = Flask(__name__, template_folder='views')
app.secret_key = 'boa_constrictor'

# Página principal
@app.route('/')
def index():
    if 'username' in session:
        usuario = obtener_usuario_por_username(session['username'])
        if usuario:
            return f"<h1>Bienvenido, {usuario.username}!</h1>"
    flash('Debes iniciar sesión primero.', 'warning')
    return redirect(url_for('login'))

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificar credenciales usando la función
        usuario = obtener_usuario_por_username(username)
        if usuario and usuario.password == password:
            session['username'] = usuario.username
            session['es_admin'] = usuario.es_admin
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        flash('Usuario o contraseña incorrectos', 'danger')

    return render_template('login.html')  # Busca en 'views'

# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada', 'info')
    return redirect(url_for('login'))

# Ruta para el panel de administración
@app.route('/admin')
def admin_dashboard():
    if 'username' in session and session.get('es_admin'):
        return "<h1>Bienvenido al panel de administración</h1>"
    flash('No tienes permisos para acceder a esta página.', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
