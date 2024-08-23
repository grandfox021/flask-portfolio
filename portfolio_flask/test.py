from flask import Flask
from werkzeug.security import check_password_hash,generate_password_hash



class User :

    def __init__(self,name,password):
    
        self.name = name
        self.password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)

    def verify_pass(self,given_pass) :

        return print(check_password_hash(self.password,given_pass))



user = User("hassan" ,"ha0142")
user.verify_pass("ha0142")