from app_flask.configuraciones.mysqloconecction import connectToMySQL
from app_flask import EMAIL_REGEX
from flask import flash
from app_flask.modelos import usuario

class Visita:
    def __init__(self, datos):
        self.usuario_id = datos["usuario_id"]
        self.arbol_id_arbol = datos["arbol_id_arbol"]
        self.usuario = []
    @classmethod
    def seleccionar_todo(cls,datos):
        query = """ 
                select *
                from visitas join usuario on visitas.usuario_id = usuario.id
                where arbol_id_arbol = %(id)s;
                """
        resultado = connectToMySQL("esquema_examen2").query_db(query,datos)

        lista_visitas = []
        print(resultado)
        
        for renglon in resultado:
            visita = Visita(renglon)
            lista_visitas.append(visita)
        print(lista_visitas)
        return lista_visitas

