from flask import Flask
from flask import request
from flask import render_template # renderizar template
import form 

app = Flask(__name__) 
# app = Flask(__name__, template_folder='Ruta/carpeta/templates')  para indicar otra ruta de los templates


@app.route('/') 
def root():
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


# Renderizar templates
@app.route('/index') 
@app.route('/index/<nombre>') 
@app.route('/index/<nombre>/<edad>') 
def index(nombre=None,edad=None):
    # el diccionario como en Django, no sirve
    return render_template('index.html',nombre=nombre,edad=edad) # la carpeta debe ser llamada "templates"
# y estar al mismo nivel del presente archivo .py


@app.route('/blog1/<item>') 
def blog1(item=None):
    return render_template('blog1.html',item=item)


@app.route('/blog2',methods = ['GET','POST']) # ambos metodos puedes acceder
def blog2():
    comment_form = form.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate(): # el formulario solo funciona con POST
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print('Error en el formulario')
    return render_template('blog2.html', form = comment_form)


if __name__ == '__main__':
    
    app.run(debug = True, 
            port=8000) 