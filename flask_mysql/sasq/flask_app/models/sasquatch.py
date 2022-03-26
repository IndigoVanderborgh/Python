from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Sasquatch:
    db_name = 'sasq'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.description = db_data['description']
        self.location = db_data['location']
        self.sighting_at = db_data['sighting_at']
        self.users_id = db_data['users_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.number_sasq = db_data['number_sasq']
        user = User.get_by_id({"id": db_data["users_id"]})
        self.name = user.first_name +" "+ user.last_name

    @classmethod
    def save(cls,data):
        query = "INSERT INTO sasquatch (description, location, sighting_at, users_id, number_sasq) VALUES (%(description)s,%(location)s,%(sighting_at)s,%(users_id)s, %(number_sasq)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sasquatch;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_sasquatch = []
        for row in results:
            print(row['sighting_at'])
            all_sasquatch.append( cls(row) )
        return all_sasquatch
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM sasquatch WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE sasquatch SET location=%(location)s, description=%(description)s, sighting_at=%(sighting_at)s,updated_at=NOW(), number_sasq=%(number_sasq)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM sasquatch WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_sasquatch(sasquatch):
        is_valid = True
        if len(sasquatch['location']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters","sasquatch")
        if len(sasquatch['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","sasquatch")
        if sasquatch['sighting_at'] == "":
            is_valid = False
            flash("Please enter a date","sasquatch")
        print(sasquatch["number_sasq"])
        if int(sasquatch["number_sasq"]) < 1:
            is_valid = False
            flash("Number must be greater than 1","sasquatch")
        return is_valid
