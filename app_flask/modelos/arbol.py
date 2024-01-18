from app_flask.configuraciones.mysqloconecction import connectToMySQL
from app_flask import EMAIL_REGEX
from flask import flash

class Arbol:
    def __init__(self, datos):
        self.id_arbol = datos["id_arbol"]
        self.plantado_por = datos["plantado_por"]
        self.id_jardinero = datos["id_jardinero"]
        self.lugar = datos["lugar"]
        self.plantado_en = datos["plantado_en"]
        self.razon = datos["razon"]
        self.especie = datos["especie"]

    @classmethod
    def seleccionar_todo(cls):
        query = """ 
                SELECT *
                FROM arbol;
                """
        resultado = connectToMySQL("esquema_examen2").query_db(query)
        
        lista_arboles = []
        
        for renglon in resultado:
            arbol = Arbol(renglon)
            lista_arboles.append(arbol)
        return lista_arboles
    
    
    @classmethod
    def agregar_uno(cls,datos):
        query = """
                Insert INTO arbol (plantado_por,id_jardinero,lugar,plantado_en,razon,especie)
                VALUES(%(plantado_por)s,%(id_jardinero)s,%(lugar)s,%(plantado_en)s,%(razon)s,%(especie)s);
                """
        resultado = connectToMySQL('esquema_examen2').query_db(query,datos)
        return resultado
    
    @classmethod
    def seleccionar_todo_mis_arboles(cls,datos):
        query = """ 
                SELECT *
                FROM arbol
                WHERE id_jardinero = %(id)s;
                """
        resultado = connectToMySQL("esquema_examen2").query_db(query,datos)
        
        lista_arboles = []
        
        for renglon in resultado:
            arbol = Arbol(renglon)
            lista_arboles.append(arbol)
        return lista_arboles
    
    @classmethod
    def editar_uno(cls, datos):
        query = """
                UPDATE arbol
                SET lugar = %(lugar)s, plantado_en = %(plantado_en)s, razon = %(razon)s, especie = %(especie)s
                WHERE id_arbol=%(id)s
                """
        return connectToMySQL('esquema_examen2').query_db(query,datos)
    
    @classmethod
    def seleccionar_uno(cls, datos):
        query = """ 
                SELECT *
                FROM arbol
                WHERE id_arbol = %(id)s;
                """
        resultado = connectToMySQL("esquema_examen2").query_db(query, datos)
        
        print(resultado)
        if len(resultado) != 0:
            arbol = Arbol(resultado[0])
            return arbol
        return None
    
    @classmethod
    def eliminar_uno(cls,datos):
        query = """
                DELETE FROM arbol
                WHERE id_arbol = %(id)s;
                """
        return connectToMySQL('esquema_examen2').query_db(query,datos)
    
    @classmethod
    def seleccionar_uno_usurios(cls, datos):
        query = """ 
                select *
                from arbol join usuario on arbol.id_jardinero = usuario.id
                where id_arbol = %(id)s;
                """
        resultado = connectToMySQL("esquema_examen2").query_db(query, datos)
        
        print(resultado)
        if len(resultado) != 0:
            arbol = Arbol(resultado[0])
            return arbol
        return None
    
    @classmethod
    def eliminar_uno(cls,datos):
        query = """
                DELETE FROM arbol
                WHERE id_arbol = %(id)s;
                """
        return connectToMySQL('esquema_examen2').query_db(query,datos)
    
    @staticmethod
    def validar_arbol(datos):
        es_valido = True
        if len(datos["especie"]) <= 5:
            flash("La especie debe tener minimo de 5 caracteres", "error_especie")
            es_valido = False
        if len(datos["lugar"]) <=2:
            flash("El lugar debe tener minimo 2 caracteres", "error_lugar")
        if len(datos["razon"]) >=50:
            flash("La razon debe tener maximo 50 caracteres", "error_razon")
        return es_valido
    