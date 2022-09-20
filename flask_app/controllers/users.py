from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.camp import Camp
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():

    if not User.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect('/dashboard')

@app.route('/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)

    if not User.validate_login(request.form):
        return redirect('/')
    data ={ 
        "email": request.form['email'],
        "password": request.form['password']
    }
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
       
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html",users=User.get_by_id(data), camps=Camp.get_all())


@app.route('/view_camps/<int:id>')
def camp_user_who_posted(id):
    user = User.get_user_with_updates(id)
    return render_template("show_camp.html", user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')