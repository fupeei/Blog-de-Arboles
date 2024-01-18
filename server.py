from app_flask import app
from app_flask.controladores import controlador_usuarios
from app_flask.controladores import controlador_arboles


if __name__ == "__main__":
    app.run(debug=True)