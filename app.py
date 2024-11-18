from flask import Flask, render_template, request, url_for, session, redirect, flash

app = Flask(__name__)
app.secret_key = 'vivaelbackend'

usuarios = {}
series={
    'series_por_ver': [],
    'viendo': [],
    'series_vistas':[]
}


@app.route('/')
def home():
    return render_template('home.html',
                           logged_in=session.get('logged_in'),
                           username=session.get('username'),
                           series=series
                           )

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in usuarios:
            error = f'El usuario {username} ya existe.'
            return render_template('register.html', error=error)
        else:
            usuarios[username] = password
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Validación de credenciales.
        username = request.form['username']
        password = request.form['password']

        if username in usuarios and usuarios[username] == password:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('home'))
        else:
            error = "Credenciales incorrectas. Vuelve a intentarlo."
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/logout')
def logout_function():
    # Eliminar los datos de la sesión
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/addserie', methods=['GET', 'POST'])
def add_series():
    if request.method == 'POST':
        nombre = request.form['nombre']
        sinopsis = request.form['sinopsis']
        puntuacion = request.form['puntuacion']
        genero = request.form['genero']
        fecha_estreno = request.form['fecha_estreno']
        capitulos = request.form['capitulos']
        duracion_capitulos = request.form['duracion_capitulos']
        categoria = request.form['categoria']

        info_serie = [nombre, sinopsis, puntuacion, genero, fecha_estreno, capitulos, duracion_capitulos, categoria]
        series[categoria].append(info_serie)

        return redirect(url_for('home'))

    return render_template('add_serie.html')




if __name__ == '__main__':
    app.run()
