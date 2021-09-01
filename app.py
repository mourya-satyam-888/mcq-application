from flask import Flask, render_template,session,request,redirect,url_for,make_response
from flask_sqlalchemy import SQLAlchemy
import random
import datetime
import os
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get("DATABASE_URL")
app.config['SECRET_KEY']='1x25d1d63s4ddnant'
db=SQLAlchemy(app)
class User(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    username=db.Column(db.String(30), nullable=False, unique=False)
    email_address=db.Column(db.String(50), nullable=False, unique=False)
    marks=db.Column(db.Integer(),nullable=False,default=0)
    date=db.Column(db.String(20),nullable=False)
class Question(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    question = db.Column(db.String(1024), nullable=False, unique=True)
    option_1 = db.Column(db.String(1024), nullable=False, unique=False)
    option_2 = db.Column(db.String(1024), nullable=False, unique=False)
    option_3 = db.Column(db.String(1024), nullable=False, unique=False)
    option_4 = db.Column(db.String(1024), nullable=False, unique=False)
    answer   = db.Column(db.Integer(),nullable=False,unique=False)
class Admin_log(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    ip=db.Column(db.String(20),nullable=False)
#question=[]
@app.route('/')
@app.route('/login')
def index():
    session["name"] =""
    session["email"]=""
    session["flag"] =0
    session['complete']=False
    session["access"]=0
    session["questionsa"]=[]
    return render_template('login.html')
@app.route('/quest',methods=["GET","POST"])
def quest():
    if request.method=="POST":
        session["name"] = request.form.get("username")
        session["email"] = request.form.get("email")
        session['marks']=0
        session["flag"]=0
        all_q = Question.query.all()
        question = []
        for q in all_q:
            question.append(q)
        #print(question)
        total = 5
        question = random.sample(question, total)

        mn = []

        for i in question :
            d = {}
            d['question'] = i.question
            d['option_1'] = i.option_1
            d['option_2'] = i.option_2
            d['option_3'] = i.option_3
            d['option_4'] = i.option_4
            d['answer'] = i.answer
            mn.append(d)
        session["questionsa"] = mn
        return redirect('/questions',code=302)
    return redirect("login.html",code=302)
@app.route('/questions',methods=["GET","POST"])
def generated_question():
    question = session["questionsa"]
    if session['complete']:
        return redirect('/',code="302")
    #print(len(question))
    try:
        if session['flag']==0:
            session['flag']=1;
            return render_template("question.html", q=question[0], que=5-len(question)+1)
        x=question[0]
    except:
        return "<h1>ACCESS DENIED<h1>"
    x=question[0]
    question.pop(0)
    option=request.args.get("option")
    try:
        option=int(option)
    except:
        option=0
    if x["answer"]==int(option):
        session['marks']+=1
    #print(session['marks'])
    try:
        return render_template("question.html", q=question[0],que=5-len(question)+1)
    except:
        return redirect('/sub',code=302)
@app.route('/submit',methods=["GET","POST"])
def subsubmit():
    question = session["questionsa"]
    session['complete']=True
    try:
        x=question[0]
    except:
        return "<h1>ACCESS DENIED<h1>"
    x=question[0]
    question.pop(0)
    option=request.args.get("option")
    try:
        option=int(option)
    except:
        option=0
    if x["answer"]==int(option):
        session['marks']+=1
    #print(session['marks'])
    return redirect('/sub',code=302)
@app.route('/sub',methods=["GET","POST"])
def submit():
    try:
        if session["email"]=="":
            return redirect('login',code=302)
        usr1=User()
        usr1.username=session['name']
        usr1.email_address=session['email']
        usr1.marks=session['marks']
        usr1.date=str(datetime.datetime.now())[:18]
        db.session.add(usr1)
        db.session.commit()
        return render_template("score.html",name=session["name"],total=session['marks'])
    except:
        return redirect('/',code=302)
@app.route('/admin')
def adminlog():
    x = Admin_log.query.all()
    fl = 0
    if (request.cookies.get('ip') == "bar") :
        fl = 1
    
    if fl:
        return redirect('/admin_check',code=302)
    return render_template("adminlogin.html")
@app.route('/admin_check',methods=["GET","POST"])
def admincheck():
    user = request.form.get("username")
    pswd = request.form.get("pswd")
    
    fl=0

    if (request.cookies.get('ip') == "bar") :
        fl = 1
    if (user == "walkover" and pswd == "walkover") or fl:
        session["access"] = 1;
        user = User.query.all()
        user.sort(key=lambda x: x.date, reverse=True)
        mn = []
        for i in user:
            d = {}
            d['username'] = i.username
            d['email_address'] = i.email_address
            d['marks'] = i.marks
            d['date'] = i.date
            mn.append(d)
        # print(len(mn),user)
        session['user'] = mn
        session['pages'] = 1
        session['total'] = -(-len(mn) // 5)
        if fl==0:
            use_ip=Admin_log()
            use_ip.ip=request.environ['REMOTE_ADDR']
            db.session.add(use_ip)
            db.session.commit()
        res = make_response(redirect('/admin-surprise', code=302))
        res.set_cookie('ip', 'bar', expires=datetime.datetime.now() + datetime.timedelta(days=2))
        return res
        #session['ip'].append(request.environ['REMOTE_ADDR'])
        #print(session['ip'])
    return "<h1>Access Denied</h1>"

@app.route('/admin-surprise',methods=["GET","POST"])
def admin():
    #print(request.environ['REMOTE_ADDR'], 'a')
    mn = request.environ['REMOTE_ADDR']
    #print(mn, session['ip'])
    
    fl = 0
    if (request.cookies.get('ip') == "bar") :
        fl = 1
    if (fl):
        session['access'] = 1
    else:
        session['access']=0
    if session["access"] != 1:
        return "<h1>Access Denied</h1>"
    user = session['user']
    page = session['pages']
    option = request.args.get("option")
    try:
        option = int(option)
    except:
        option = 0
    if (option == 1):
        page += 1
    elif (option == 2):
        page -= 1
    session['pages'] = page
    # print(page)
    flag = 1
    flag1 = 1
    if (page == 1):
        flag1 = 0
    if (page == session['total']):
        flag = 0
    # print(user)
    return render_template("admin.html", user=user[5 * (page - 1):5 * page], flag=flag, flag1=flag1, page=1)
if __name__=="__main__":
    app.run(debug=False)
