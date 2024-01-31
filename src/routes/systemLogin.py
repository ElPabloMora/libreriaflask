from flask import Blueprint, render_template, flash, redirect, url_for, request
from database.database import conect_db
from werkzeug.security import generate_password_hash
from models.user import User
from models.modeluser import ModelUser


connect = conect_db()
cursor = connect.cursor()

systemlogin = Blueprint('systemlogin',__name__)

@systemlogin.route('/')
def index():
    return render_template('home.html')


@systemlogin.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username != '' and password != '':
            passwordhasd = generate_password_hash(password,method='pbkdf2:sha256')
            cursor.execute('INSERT INTO login (username,password) VALUES (%s,%s)',(username,passwordhasd))
            connect.commit()
            flash("You're registered!",'alert-success')
            return redirect(url_for('systemlogin.login'))
    return render_template('signup.html')
    
@systemlogin.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User(0,request.form['username'],request.form['password'])
        loggedUser = ModelUser.login(connect,user)
        if loggedUser != None:
            if loggedUser.password:
                flash("You're logged!")
                return redirect(url_for('systemcontrol.mainprimary'))
            else:
                flash('Invalid password!','alert-danger')
        else:
            flash('User no found!','alert-danger')
    return render_template('login.html')