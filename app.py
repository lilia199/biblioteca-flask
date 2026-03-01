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


pip freeze > requirements.txt







