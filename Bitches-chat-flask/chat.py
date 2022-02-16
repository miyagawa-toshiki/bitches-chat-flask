from cgitb import text
from email.policy import default
from ensurepip import bootstrap
from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user,logout_user,login_required
from sqlalchemy import Integer
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime
import pytz
from flask_bootstrap import Bootstrap
from negative import Negative

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50), nullable=False)
    score = db.Column(Integer, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
    default=datetime.now(pytz.timezone('Asia/Tokyo')))

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        # データを全部取ってくる
        posts=Post.query.all()
        return render_template('index.html',posts=posts)

    return render_template('index.html')

@app.route('/create', methods=['GET','POST'])
def create():
    #受け取ったかどうか
    if request.method == 'POST':
        txt=request.form.get('text')
        score=Negative(txt)
        post=Post(text=txt, score=score)
        db.session.add(post)
        db.session.commit()
        return redirect('/')

    else:
        return render_template('create.html')
