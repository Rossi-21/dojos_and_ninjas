from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    def __init__(self, data):
       self.id = data['id']
       self.name = data['name']
       self.created_at = data['created_at']
       self.updated_at = data['updated_at']
       self.ninjas = []

    @classmethod
    def save(cls, data):
        query = """INSERT INTO dojos (name, created_at, updated_at)
        Values (%(name)s, NOW(), NOW());"""
        return connectToMySQL('dojos').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos 

    @classmethod
    def get_one(cls,data):
        query = "Select * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojos').query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = """SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = 
        dojos.id WHERE dojos.id = %(id)s;"""
        results = connectToMySQL('dojos').query_db(query, data)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db["updated_at"]
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo
    
    