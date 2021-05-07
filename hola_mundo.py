from flask import Flask

app = Flask(__name__) # OBJETO, creación de instancia

@app.route('/') # wrap , decorador, es ('/') es la unica ruta a la que pueden acceder
def index():
    return "Hola mundo desde FLASK" # regresar un string


if __name__ == '__main__':
    # corremos el servidor por default puerto 5000
    app.run(debug = True, # a la escucha de cualquier cambio y se ve reflejado
            port=8000) # podemos cambiar el puerto con (port=xxxx)