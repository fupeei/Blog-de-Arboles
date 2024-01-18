from app_flask import app
from flask import render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
from app_flask.modelos.usuario import Usuario

bcrypt = Bcrypt(app)

@app.route("/")
def formularios():
    return render_template("formulario.html")

@app.route("/procesar/nuevo/usuario", methods=["POST"])
def procesar_nuevo_usuario():
    
    if Usuario.validar_registro(request.form) == False:
        return redirect("/")
    
    

    contraseña_encriptada = bcrypt.generate_password_hash(request.form["contraseña"])

    usuario_encriptado = {
        **request.form,
        "contraseña" : contraseña_encriptada
    }

    nuevo_usuario ={ 
    'nombre' : request.form["nombre"],
    'apellido': request.form["apellido"],
    'email': request.form["email"],
    'contraseña': request.form["contraseña"]
    }
    id_nuevo_usuario= Usuario.agregar_uno(usuario_encriptado)

    session["nombre"] = request.form["nombre"]
    session["apellido"] = request.form["apellido"]
    session["id"] = id_nuevo_usuario
    
    return redirect ("/dashboard")

@app.route('/procesa/login', methods=["POST"]   )
def procesa_login():
    datos = {
        "email" : request.form["email"],
        "contraseña" : request.form["contraseña"]
    }
    usuario = Usuario.seleccionar_uno(datos)
    print(usuario)
    
    if usuario == None:
        flash("Correo o contraseña invalidos", "error_login")
        return redirect("/")
    if not bcrypt.check_password_hash(usuario.contraseña, request.form['contraseña']):
        flash("Correo o contraseña invalidos", "error_login_c")
        return redirect('/')
    
    session["nombre"] = usuario.nombre
    session["apellido"] = usuario.apellido
    session["id"] = usuario.id
    session["email"] = usuario.email
    
    return redirect("/dashboard")

@app.route("/procesa/logout", methods=["POST"])
def procesa_logout():
    session.clear()
    return redirect("/")