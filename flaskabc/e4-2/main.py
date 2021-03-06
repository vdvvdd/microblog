from flask import Flask 
from flask import request 
from flask import render_template 
from flask import redirect
from db import *

app = Flask(__name__)

from wtforms import Form, TextField, PasswordField, validators

class LoginForm(Form):
    username = TextField("username", [validators.Required()])
    password = PasswordField("password", [validators.Required()])

@app.route("/user", methods=['GET', 'POST'])
def login():
    myForm = LoginForm(request.form)
    if request.method=='POST':
        if myForm.validate() and is_exist(myForm.username.data, myForm.password.data):
        #if myForm.validate() and myForm.username.data=='daihao' and myForm.password.data=='123456':
            return redirect("https://cn.bing.com/")
        else:
            message = "login failed"
            # myForm.username.data = ""
            # myForm.password.data = ""
            return render_template('index.html', form=myForm, message=message)

    return render_template('index.html', form=myForm)

@app.route("/register", methods=['GET', 'POST'])
def register():
    myForm = LoginForm(request.form)
    if request.method == 'POST':
        if myForm.validate():
            add_user(myForm.username.data, myForm.password.data)
            return "Register successfully"
    return render_template('index.html', form=myForm)


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')