from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.camp import Camp


@app.route('/new/camp')
def new_camp():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_camp.html',user=User.get_by_id(data))


@app.route('/create/camp',methods=['POST'])
def create_camp():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Camp.validate_camp(request.form):
        return redirect('/new/camp')
    data = {
        "camp_name": request.form["camp_name"],
        "location": request.form["location"],
        "description": request.form["description"],
        "camping_date": request.form["camping_date"],
        "users_id": session["user_id"]
    }
    Camp.save(data)
    return redirect('/dashboard')

@app.route('/edit/camp/<int:id>')
def edit_camp(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_camp.html",edit=Camp.get_one(data),user=User.get_by_id(user_data))

    return render_template("edit_camp.html",edit=amp.get_one(data),user=User.get_by_id(user_data))
@app.route('/update/camp',methods=['POST'])
def update_camp():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Camp.validate_camp(request.form):
        return redirect('/new/camp')
    data = {
        "camp_name": request.form["camp_name"],
        "location": request.form["location"],
        "description": request.form["description"],
        "camping_date": request.form["camping_date"],
        "id": request.form['id']
    }
    Camp.update(data)
    return redirect('/dashboard')

@app.route('/camp/<int:id>')
def camp_camp(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_camp.html",camp=Camp.get_one(data),user=User.get_by_id(user_data))

@app.route('/destroy/camp/<int:id>')
def destroy_camp(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Camp.destroy(data)
    return redirect('/dashboard')