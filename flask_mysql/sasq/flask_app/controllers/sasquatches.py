from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.sasquatch import Sasquatch
from flask_app.models.user import User


# @app.route('/new/sighting')
# def new_sighting():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data = {
#         "id":session['user_id']
#     }
#     return render_template('new_sighting.html',user=User.get_by_id(data))

@app.route('/new/sighting')
def new_sighting():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_sighting.html',user=User.get_by_id(data))

@app.route('/create/sighting',methods=['POST'])
def create_sighting():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Sasquatch.validate_sasquatch(request.form):
        return redirect('/new/sighting')
    data = {
        "description": request.form["description"],
        "location": request.form["location"],
        "sighting_at": request.form["sighting_at"],
        "users_id": session["user_id"],
        "number_sasq": request.form['number_sasq']
    }
    Sasquatch.save(data)
    return redirect('/dashboard')

@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_sighting.html",edit=Sasquatch.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/sighting',methods=['POST'])
def update_sasquatch():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Sasquatch.validate_sasquatch(request.form):
        return redirect('/edit/'+request.form["id"])
    data = {
        "id": request.form["id"],
        "description": request.form["description"],
        "location": request.form["location"],
        "sighting_at": request.form["sighting_at"],
        "number_sasq": int(request.form['number_sasq']),
    }
    Sasquatch.update(data)
    return redirect('/dashboard')

@app.route('/show/<int:id>')
def show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_sighting.html",sasquatch=Sasquatch.get_one(data),user=User.get_by_id(user_data))

@app.route('/destroy/<int:id>')
def destroy_sasquatch(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Sasquatch.destroy(data)
    return redirect('/dashboard')
