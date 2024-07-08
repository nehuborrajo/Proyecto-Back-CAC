from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

#codigo de estado
#404 -> error
#200 -> todo ok

#GET -> consultar
#POST -> insertar
#DELETE -> eliminar
#PUT -> actualizo todo el elemento
#PATCH -> actualizo parcialmente (por ej 1 solo campo)

###########################################################

#GET

@app.route('/juegos', methods = ['GET']) #decorador ('ruta de referencia a donde redirige', metodo(get por defecto, si no se especifica))
def ver_juegos():
    db = mysql.connector.connect(
        host='localhost',
        user='root', #mi usuario
        password='12345', #mi contraseña
        database='portaljuegos' #nombre de la base de datos
    )

    cursor = db.cursor(dictionary = True) #lo devuelve como diccionario
    cursor.execute("SELECT * FROM juego")

    productos = cursor.fetchall() #recupera todo lo seleccionado

    cursor.close()
    return jsonify(productos) #lo devuelve tipo json


#DELETE
                            #va a recibir un int
@app.route('/eliminar_juego/<int:id>', methods = ['DELETE']) #decorador ('ruta de referencia a donde redirige', metodo(get por defecto, si no se especifica))
def eliminar_juego(id):
    db = mysql.connector.connect(
        host='localhost',
        user='root', #mi usuario
        password='12345', #mi contraseña
        database='portaljuegos' #nombre de la base de datos
    )

    cursor = db.cursor()
    cursor.execute("DELETE FROM juego WHERE id = %s", (id,)) #se pone ',' para indicar que es una tupla de 1 solo elemento
    db.commit() #guarda los cambios

    cursor.close()
    return jsonify({"mensaje": "ELIMINADO CORRECTAMENTE"}) #creo el diccionario manualmente


#POST

@app.route('/agregar_juego', methods = ['POST']) #decorador ('ruta de referencia a donde redirige', metodo(get por defecto, si no se especifica))
def agregar_juego():
    info = request.json #almacena la informacion q devuelva request (contenido json -> los datos a agregar)
    db = mysql.connector.connect(
        host='localhost',
        user='root', #mi usuario
        password='12345', #mi contraseña
        database='portaljuegos' #nombre de la base de datos
    )

    cursor = db.cursor()
    cursor.execute("INSERT INTO juego (nombre, version, precio) VALUES (%s,%s,%s)", (info["nombre"], info["version"], info["precio"]))
    db.commit()

    cursor.close()
    return jsonify({"mensaje": "AGREGADO CORRECTAMENTE"}) #lo devuelve tipo json


#PUT

@app.route('/actualizar_juego/<int:id>', methods = ['PUT']) #decorador ('ruta de referencia a donde redirige', metodo(get por defecto, si no se especifica))
def actualizar_juego(id):
    info = request.json #almacena la informacion q devuelva request (contenido json -> los datos a agregar)
    db = mysql.connector.connect(
        host='localhost',
        user='root', #mi usuario
        password='12345', #mi contraseña
        database='portaljuegos' #nombre de la base de datos
    )

    cursor = db.cursor()
    cursor.execute("UPDATE juego SET nombre= %s, version= %s, precio= %s WHERE id= %s", (info["nombre"], info["version"], info["precio"], id))
    db.commit()

    cursor.close()
    return jsonify({"mensaje": "ACTUALIZADO CORRECTAMENTE"}) #lo devuelve tipo json




if __name__ == '__main__':
    app.run(debug = True)       #ejecutar y ver los cambios




