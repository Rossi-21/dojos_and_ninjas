from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
       self.id = data['id']
       self.first_name = data['first_name']
       self.last_name = data['last_name']
       self.age = data['age']
       self.created_at = data['created_at']
       self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
                VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);               
        """
        return connectToMySQL('dojos').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "Select * FROM ninjas;"
        results = connectToMySQL('dojos').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas
    
    @classmethod
    def get_one(cls,data):
        query = "Select * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL('dojos').query_db(query,data)
        return cls(result[0])

    @classmethod
    def delete(cls,data):
        query = "DELETE from ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojos').query_db(query,data)

    @classmethod
    def update(cls,data):
        query = """ 
        UPDATE ninjas 
        SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s 
        WHERE id = %(id)s;"""
        return connectToMySQL('dojos').query_db(query,data)

