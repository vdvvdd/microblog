from flask import Flask
from flask import flash, render_template
from flask import request, abort

app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
def index():
    flash('hello baby')
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    form = request.form
    username = form.get("username")
    password = form.get("password")

    if not username:
        flash("please input username")
        return render_template("index.html")
    if not password:
        flash("please input password")
        return render_template("index.html")

    if username == "dh" and password == "123":
        flash("login success")
        return render_template("index.html")
    else:
        flash("username or password is wrong")
        return render_template("index.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.route('/users/<userid>')
def users(userid):
    if int(userid) == 1:
        return render_template("user.html")
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
