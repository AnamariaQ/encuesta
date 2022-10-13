from flask import render_template, request, redirect, session
from encuesta import app
from flask import render_template, redirect, request, session

# importar la clase de Amigos de la carpeta models del archivo amigo.py
from encuesta.models.encuesta import Dojos

@app.route('/')
def raiz():
    return render_template("index.html")
    #*! En lugar de devolver una cadena, 
    #*! devolveremos el resultado del método render_template
    #*!pasando el nombre de nuestro archivo HTML


@app.route('/process', methods=['POST'])
def enviar():
    print(request.form)
    if not Dojos.validate_encuesta(request.form):
        return redirect ('/')
    session['nombre'] = request.form['nombre']
    session['ubicacion'] = request.form['ubicacion']
    session['lenguaje'] = request.form['lenguaje']
    session['comentarios'] = request.form['comentarios']
    Dojos.save(request.form)
    return redirect('/result')

@app.route('/result')
def resultado():
    return render_template("result.html", data=session)