from flask import Flask, render_template
#Importar la librería de Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

#Instanciar la aplicacion
app = Flask(__name__)

#Agregar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#Decorador para definir la ruta
@app.route('/')
#Función mostrar lista actual de las tareas pendiente
def mostrar_lista_actual():
    return render_template('base.html')

#Decorador para definir la ruta
@app.route('/enviar')
#Función aceptar datos y agregar elementos de la lista de tareas pendientes
def agregar_elemento():
    return 'contro2'

#Decorador para definir la ruta
@app.route('/borrar')
#Función mostrar lista actual de las tareas pendiente
def borrar_lista():
    return 'contro3'


#main del programa
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)