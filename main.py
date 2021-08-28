from flask import Flask, render_template,session,request,redirect,url_for
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
question=[]
@app.route('/')
@app.route('/login')
def login():
    session["name"] =""
    session["email"]=""
    session["flag"] =0
    return render_template('login.html')
@app.route('/quest',methods=["GET","POST"])
def quest():
    if request.method=="POST":
        session["name"] = request.form.get("username")
        session["email"] = request.form.get("email")
        session["flag"]=0
        all_q = Question.query.all()
        global question
        question = []
        for q in all_q:
            question.append(q)
        print(question)
        total = 5
        question = random.sample(question, total)
        return redirect('/questions',code=302)
    return render_template("login.html")
@app.route('/questions',methods=["GET","POST"])
def generated_question():
    global question
    if session['flag']==0:
        session['flag']=1;
        return render_template("question.html", q=question[0], que=5-len(question)+1)
    x=question[0]
    question.pop(0)
    option=request.args.get("option")
    if x.ans==int(option):
        session['marks']+=1
    return render_template("question.html", q=question[0],que=5-len(question)+1)
app.run(debug=True)