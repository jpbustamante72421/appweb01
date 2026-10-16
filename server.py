from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html', titulo="Home", mensaje="Bienvenido a la página de inicio de UDL-ICO")

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo="Servicios", mensaje="Bienvenido a la página de servicios de UDL-ICO")

@app.route('/contacto')
def contacto():
    return render_template('contactos.html', titulo="Contactos", mensaje="Bienvenido a la página de contactos de UDL-ICO")

@app.route('/productos')
def productos():
    return render_template('productos.html', titulo="Productos", mensaje="Bienvenido a la página de productos de UDL-ICO")

if __name__ == '__main__':
    app.run(debug=True, port=5050)