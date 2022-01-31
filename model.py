from python_flask_register_login.config import *

class User(db.Model):
    __tablename__ = 'user_info'
    id = db.Column('id', db.Integer, primary_key=True)
    public_id = db.Column('public_id', db.String(100), unique=True)
    name = db.Column('name', db.String(50))
    email = db.Column('email', db.String(100), unique=True, nullable=False)
    password = db.Column('password', db.String(120))

if __name__ == '__main__':
    db.create_all()


