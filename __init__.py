#! C:/Users/skala/AppData/Local/Programs/Python/Python310/python.exe

import wtforms
from flask import Flask
from wtforms import Form

app = Flask(__name__) 

@app.route('/')
def homepage():
    return "Hi"
if __name__ == "__main__":
    app.run()  

class RegistrationForm(Form):
    username = TextField("Username", [validators.Length(min=4,max=20]) 
    username = TextField("Email Adress", [validators.Length(min=6,max=50])   
    password = PasswordField('Password', validators.Required(),
                                         validators.EqualTo('confirm', message='Password must match.')])
    confirm = PasswordField('Repeat Password') 
    