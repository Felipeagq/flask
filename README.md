# Documentación del micro framework de Python, FLASK.

## Porque Flask:
- Solo usamos lo que necesitamos.
- Permite pruebas unitarias.
- Facil compresión.
- Uso de Cookies.
- Manejo de sesiones.
- Curva de aprendizaje baja.



# Cosas vistas:
- Herencia de plantillas.
- carpeta static.
- Macros.
- Formularios en Flask. https://www.youtube.com/watch?v=74nwU6tBeV0&list=PLagErt3C7iltAydvN6SgCVKsOH4xQQKsk&index=11



# Formulario en Flask:
- crear un archivo "form.py", dentro del achivo "_macro.html" crear el render del formulario y en la pagina html a mostrar, colocar el block.
![alt text](https://raw.github.com/Felipeagq/flask/master/imagenes/from1.png)
![alt text](https://raw.github.com/Felipeagq/flask/master/imagenes/from2.png)
![alt text](https://raw.github.com/Felipeagq/flask/master/imagenes/from3.png)



# Validar formularios:
- Para crear el validador de formularios hay  importar "from wtforms import validators" en el archivo "form.py" y colocar los parametros de validación.
![alt text](https://raw.github.com/Felipeagq/flask/master/imagenes/val_form1.png)
- Luego para implementar la validación, en el archivo "index.py", agregar
![alt text](https://raw.github.com/Felipeagq/flask/master/imagenes/val.png)
- Luego en "_macro.html", debemos validar si hay errores.
![alt text](https://raw.github.com/Felipeagq/flask/master/imagenes/val2.png)



# Agregar validación propia:
![alt text](https://raw.github.com/Felipeagq/flask/master/imagenes/val_p1.png)
![alt text](https://raw.github.com/Felipeagq/flask/master/imagenes/val_p2.png)
![alt text](https://raw.github.com/Felipeagq/flask/master/imagenes/val_p3.png)










# Tomado de :
El curso de YouTube de CodigoFacilito: https://www.youtube.com/playlist?list=PLagErt3C7iltAydvN6SgCVKsOH4xQQKsk.