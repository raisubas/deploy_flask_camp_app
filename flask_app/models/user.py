from flask_app.config.mysqlconnection import connectToMySQL
from .camp import Camp
import pprint
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class User:
    db_name = "user_camp"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.campdetails = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO user_camp.users (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        return connectToMySQL(cls.db_name).query_db(query,data)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user_camp.users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM user_camp.users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM user_camp.users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        print("get one user", results)
        return cls(results[0])

        @classmethod
        def get_user_with_updates(cls,id):
            query = "SELECT * FROM camps LEFT JOIN users ON users_id = users.id WHERE users.id = {id};"
            results = connectToMySQL(cls.db_name).query_db
            pprint.pprint(results)
            user= cls(results[0])
            for row in results:
                data = {
                    "id": row['id'],
                    "camp_name": row['camp_name'],
                    "location": row['location'],
                    "description": row['description'],
                    "camping_date": row['camping_date'],
                    "created_at": row['created_at'],
                    "updated_at": row['updated_at']
                }
                user.campdetails.append(Camp(data))
                return user
    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM user_camp.users WHERE email = %(email)s;"
        results = connectToMySQL(User.db_name).query_db(query,user)

        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email", "register")
            is_valid=False
        if len(user['first_name']) < 2:
            flash("First name is required", "register")
            is_valid= False
        if len(user['last_name']) < 2:
            flash("Last name is required", "register")
            is_valid= False
        if len(user['password']) < 1:
            flash("Enter at least 5 char password", "register")
            is_valid= False
        if user['confirm'] != user['password']:
            flash("Your passwords do not match", "register")
            is_valid= False
        return is_valid
    @staticmethod
    def validate_login(user):
        is_valid = True
        query = "SELECT * FROM user_camp.users WHERE email = %(email)s;"
        results = connectToMySQL(User.db_name).query_db(query,user)

        if len(user['email']) < 1:
            flash("Please enter your email", "login")
            is_valid= False
        if len(user['password'])  < 1:
            flash("Password is a required field as well", "login")
            is_valid= False
        return is_valid


 