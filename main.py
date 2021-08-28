from flask import Flask, render_template,session
from flask_sqlalchemy import SQLAlchemy
import random
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///working.db'
app.config['SECRET_KEY']='1x25d1d63s4ddnant'
db=SQLAlchemy(app)
class User(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    username=db.Column(db.String(30), nullable=False, unique=True)
    email_address=db.Column(db.String(50), nullable=False, unique=True)
    marks=db.Column(db.Integer(),nullable=False,default=0)
class Question(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    question = db.Column(db.String(1024), nullable=False, unique=True)
    option_1 = db.Column(db.String(30), nullable=False, unique=False)
    option_2 = db.Column(db.String(30), nullable=False, unique=False)
    option_3 = db.Column(db.String(30), nullable=False, unique=False)
    option_4 = db.Column(db.String(30), nullable=False, unique=False)
    answer   = db.Column(db.Integer(),nullable=False,unique=False)

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/questions')
def submit():
    session['name']=random.randint(0,100000)
    return f'number is {session["name"]}'
app.run(debug=True)
