from app_flask import app
from flask import render_template, request, redirect, session, flash
from app_flask.modelos.arbol import Arbol
from app_flask.modelos.usuario import Usuario
from app_flask.modelos.vistas import Visita

@app.route("/dashboard")
def dashboard():
    if "id" not in session:
        return redirect("/")
    
    lista_arboles = Arbol.seleccionar_todo()
    return render_template("dashboard.html", lista_arboles = lista_arboles)

@app.route("/nuevo/arbol")
def nueva_revista():
    if "id" not in session:
        return redirect("/")
    return render_template("nuevo_arbol.html")

@app.route("/procesar/nuevo/arbol", methods=["POST"])
def procesar_nuevo_arbol():
    if Arbol.validar_arbol(request.form) == False:
        return redirect("/nuevo/arbol")
    nueva_arbol ={
    'plantado_por' : f'{session["nombre"]}',
    'id_jardinero' : f'{session["id"]}',
    'plantado_en' : request.form["plantado_en"],
    'lugar' : request.form["lugar"],
    'razon' : request.form["razon"],
    'especie': request.form["especie"]
    }
    id_nuevo_usuario= Arbol.agregar_uno(nueva_arbol)
    return redirect ("/dashboard")

@app.route("/mis/arboles/<int:id>")
def mis_arboles(id):
    if "id" not in session:
        return redirect("/")
    datos = {
        "id" : session["id"]
    }
    lista_mis_arboles = Arbol.seleccionar_todo_mis_arboles(datos)
    return render_template("arbortrario.html", lista_mis_arboles=lista_mis_arboles)

@app.route("/editar/arbol/<int:id>")
def editar_arbol(id):
    if "id" not in session:
        return redirect("/")
    datos = {
        "id" : id
    }
    arbol = Arbol.seleccionar_uno(datos)
    return render_template("editar_arbol.html", arbol=arbol)

@app.route('/procesar/editar/arbol/<int:id>', methods = ['POST'])
def procesar_editar_usuario(id):
    print(request.form)

    if Arbol.validar_arbol(request.form) == False:
        return redirect(f'/editar/arbol/{id}')
    
    datos = {
    'id' : id,
    'plantado_en' : request.form["plantado_en"],
    'lugar' : request.form["lugar"],
    'razon' : request.form["razon"],
    'especie': request.form["especie"]
    }
    Arbol.editar_uno(datos)
    return redirect(f'/mis/arboles/{session["id"]}')

@app.route("/ver/arbol/<int:id>")
def ver_arbol(id):
    if "id" not in session:
        return redirect("/")
    datos = {
        "id" : id
    }
    arbol = Arbol.seleccionar_uno_usurios(datos)
    return render_template("ver_arbol.html", arbol=arbol)

@app.route('/eliminar/arbol/<int:id>', methods =['POST'])
def eliminar_uno(id):
    datos = {
        "id" : id
    }
    Arbol.eliminar_uno(datos)
    return redirect (f'/mis/arboles/{session["id"]}')