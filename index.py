from flask import Flask
from flask import request


app = Flask(__name__) 


@app.route('/') 
def index():
    return "Pagina indice con FLASK" 


@app.route('/saludo') 
def saludo():
    return "Saludo desde FLASK" 


# un parametro por url es ?param=1, el parametro se llama param
# los parametros se puede separar por &
# ?p1=algo&p2=otroalgo.
@app.route('/params') # definimos ruta
def params():
    p1 = request.args.get('p1', 'sin p1') # definimos parametros
    p2 = request.args.get('p2', 'sin p2') # definimos parametros
    return "El parametro 1 y 2 son : {} y {}".format(p1,p2) # imprimos parametros



## Podemos jugar con el redireccionamiento de las paginas y rutas con los condicionales
# ruta/libro/python
# leer los item de la ruta
@app.route('/ruta/') # que se ejecute aún sin argumento
@app.route('/ruta/<nombre>/') # agregar entre diamantes
@app.route('/ruta/<nombre>/<int:edad>') # con <int: > podemos definirlo como numero entero
# los valores son de tipo string 
def ruta(nombre=None,edad=None): # colocarlo como parametro
    if nombre and edad==None:
        return "La ruta escrita fue {}".format(nombre) # imprimos parametros
    if nombre and edad:
        return "La ruta escrita fue {} con edad = {}".format(nombre,edad)
    else:
        return "estas en la 'ruta' sola"




if __name__ == '__main__':
    
    app.run(debug = True, 
            port=8000) 