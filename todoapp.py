from flask import Flask, render_template, request, redirect, url_for
#Importar la librería de Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

#Instanciar la aplicacion
app = Flask(__name__)

#Agregar la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Agregamos una clase para nuestros elementos 
class modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    marca_complet = db.Column(db.Boolean)

#Decorador para definir la ruta
@app.route('/')
#Función mostrar lista actual de las tareas pendiente
def mostrar_lista_actual():
    Lista_t = modelo.query.all()
    return render_template('base.html', Lista_t=Lista_t)

#Decorador para definir la ruta
@app.route('/enviar', methods=['POST'])
#Función aceptar datos y agregar elementos de la lista de tareas pendientes
def agregar_elemento():
    if request.method == 'POST':
        nuevo_titulo = request.form['nuevo_titulo']
        nueva_tarea = modelo(titulo=nuevo_titulo, marca_complet=False)
        db.session.add(nueva_tarea)
        db.session.commit()
    return redirect(url_for('mostrar_lista_actual'))

#Decorador para definir la ruta
@app.route('/borrar/<int:id_tarea>')
#Función mostrar lista actual de las tareas pendiente
def borrar_lista(id_tarea):
    tarea_a_borrar = modelo.query.get(id_tarea)
    db.session.delete(tarea_a_borrar)
    db.session.commit()
    return redirect(url_for('mostrar_lista_actual'))

#main del programa
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
