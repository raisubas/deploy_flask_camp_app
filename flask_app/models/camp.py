from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Camp:
    db_name = 'user_camp'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.camp_name = db_data['camp_name']
        self.location = db_data['location']
        self.description = db_data['description']
        self.camping_date = db_data['camping_date']
        self.user_id = db_data['users_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO user_camp.camps (camp_name,location, description, camping_date, users_id) VALUES (%(camp_name)s,%(location)s,%(description)s,%(camping_date)s,%(users_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user_camp.camps;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_camps = []
        for row in results:
            print(row['camping_date'])
            all_camps.append( cls(row) )
        return all_camps
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM user_camp.camps WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )


    @classmethod
    def update(cls, data):
        query = "UPDATE user_camp.camps SET camp_name=%(camp_name)s, description=%(description)s, location=%(location)s, description=%(description)s, camping_date=%(camping_date)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM user_camp.camps WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_camp(camp):
        is_valid = True
        if len(camp['camp_name']) < 1:
            is_valid = False
            flash("Name must be at least 3 character","camp")
        if len(camp['location']) < 1:
            is_valid = False
            flash("Please enter the location","camp")
        if camp['camping_date'] == 0:
            is_valid = False
            flash("Enter a date","camp")
        return is_valid
