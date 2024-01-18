from app_flask.configuraciones.mysqloconecction import connectToMySQL
from app_flask import EMAIL_REGEX
from flask import flash

class Usuario:
    def __init__(self, datos):
        self.id = datos["id"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.email = datos["email"]
        self.contraseña = datos["contraseña"]
        self.creado_en = datos["creado_en"]
        self.actualizado_en = datos["actualizado_en"]

    @classmethod
    def agregar_uno(cls,datos):
        query = """
                Insert INTO usuario (nombre,apellido,email,contraseña) 
                VALUES(%(nombre)s,%(apellido)s,%(email)s,%(contraseña)s);
                """
        resultado = connectToMySQL('esquema_examen2').query_db(query,datos)
        return resultado
    
    @classmethod
    def seleccionar_uno(cls, datos):
        query = """ 
                SELECT *
                FROM usuario
                WHERE email = %(email)s;
                """
        resultado = connectToMySQL("esquema_examen2").query_db(query, datos)
        
        if len(resultado) == 0:
            return None
        return cls(resultado[0])
    
    @classmethod
    def editar_uno(cls, datos):
        query = """
                UPDATE usuario
                SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s
                WHERE id=%(id)s
                """
        return connectToMySQL('esquema_examen2').query_db(query,datos)
    
    @staticmethod
    def validar_registro(datos):
        es_valido = True
        if len(datos["nombre"]) <= 2:
            flash("Usa un nombre valido con un minimo de 3 caracteres", "error_nombre")
            es_valido = False
        if len(datos["apellido"]) <=2:
            flash("Usa un apellido valido con un minimo de 3 caracteres", "error_apellido")
        
        if not EMAIL_REGEX.match(datos['email']): 
            flash("Email invalido!", "error_email")
            es_valido = False
        
        if len(datos["contraseña"]) <=8:
            flash("La contraseña debe tener al menos 8 caracteres", "error_contraseña")
            es_valido = False
        if datos["c-contraseña"] != datos ["contraseña"]:
            flash("Tus contraseñas no coinciden", "error_coincidir")
            es_valido = False
        return es_valido
    
    @staticmethod
    def validar_cambio(datos):
        es_valido = True
        if len(datos["nombre"]) <= 2:
            flash("Usa un nombre valido con un minimo de 3 caracteres", "error_nombre")
            es_valido = False
        if len(datos["apellido"]) <=2:
            flash("Usa un apellido valido con un minimo de 3 caracteres", "error_apellido")
        
        if not EMAIL_REGEX.match(datos['email']): 
            flash("Email invalido!", "error_email")
            es_valido = False
        return es_valido