from python_flask_register_login.config import *
from python_flask_register_login.model import User
from werkzeug.security import generate_password_hash,check_password_hash
import uuid # for public id
import jwt
from jwt import decode
import datetime

from flask import render_template,request,flash,redirect,url_for,make_response,jsonify

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET','POST'])
def register_user():
    msg = ''
    if request.method == 'POST':
        formdata = request.form
        name = formdata.get('name')
        email = formdata.get('email')
        password = formdata.get('password')
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(public_id=str(uuid.uuid4()),
                        name=name,
                        email=email,
                        password=generate_password_hash(password=password,method='sha256')
                        )
            db.session.add(user)
            db.session.commit()
            msg = 'User created successfully!'
            render_template('register.html', msg=msg)
        else:
            msg = 'User already exists.Please log in!'
    return render_template('register.html', msg=msg)

@app.route('/login', methods=['GET','POST'])
def login():
    msg = ''
    if request.method == 'POST':
        auth = request.form
        # name = auth.get('name')
        email = auth.get('email')
        password = auth.get('password')
        user = User.query.filter_by(email=email).first()

        if not auth or not auth.get('email') or not auth.get('password'):
            msg = 'Could not verify!please signup!'
            return render_template('login.html', msg=msg)
        elif not user:
            msg = 'User not found!Could not verify!'
            return render_template('login.html', msg=msg)
        elif not user or not check_password_hash(user.password, password):
            msg = 'please check your login details and try again'
            return render_template('login.html',msg=msg)

        return render_template('index.html',name=user.name)
    return render_template('login.html',msg=msg)

@app.route('/logout')
def logout():
    pass








if __name__ == '__main__':
    app.run(debug=True)