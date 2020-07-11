from flask import Flask, render_template, request, redirect, url_for
from models.user import Db, User
from modules.userform import UserForm
from modules.random_users_form import RandomUsersForm
from modules.edit_userform import EditUserForm
import names
import random


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:s14a-key@localhost:5432/usersdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ukhkvdafgrbsqy:8bdd96c3ab8b6d0e271bdfbff1986899910722e179a916ed83f5d48307ef64dc@ec2-54-152-175-141.compute-1.amazonaws.com:5432/dfe46f1k3kjv99'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "s14a-key"
Db.init_app(app)


@app.route('/')
def index():
    # Query all
    users = User.query.all()
    
    users_dict = {}    
    for user in users:
        users_dict[user.user_id] = [user.first_name, user.age]
            
    return render_template("index.html", users=users_dict)


@app.route('/read/<user_id>')
def user_profile(user_id):
	user = User.query.filter_by(user_id=user_id).all()[0]
	#user = User.query.filter(User.user_id==user_id).all()
	fname = user.first_name
	age = user.age
	return render_template("user.html", first_name=fname, age=age)
    

@app.route('/adduser', methods=['GET', 'POST'])
def addUser():
    form = UserForm()
    # If GET
    if request.method == 'GET':
        return render_template('adduser.html', form=form)
    # If POST
    else:
        if form.validate_on_submit():
            first_name = request.form['first_name']
            age = request.form['age']
            new_user = User(first_name=first_name, age=age)
            Db.session.add(new_user)
            Db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('adduser.html', form=form)


@app.route('/adduser/<first_name>/<age>')
def addUserFromUrl(first_name, age):
    Db.session.add(User(first_name=first_name, age=age))
    Db.session.commit()
    return redirect(url_for('index'))
    
    
@app.route('/addusers_random', methods=['GET', 'POST'])
def addUsersRandom():
    form = RandomUsersForm()
    # If GET
    if request.method == 'GET':
        return render_template('addusers_random.html', form=form)
    # If POST
    else:
        if form.validate_on_submit():
            n_users = int(request.form['n_users'])
            for i in range(n_users):
                fname = names.get_first_name()
                age = random.randint(0, 110)
                new_user = User(first_name=fname, age=age)
                Db.session.add(new_user)
                Db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('addusers_random.html', form=form)
    

@app.route('/delete/<user_id>')
def deleteUserFromUrl(user_id):
	Db.session.query(User).filter(User.user_id == user_id).delete()
	Db.session.commit()
	return user_id
	
	
@app.route('/edituser/<user_id>', methods=['GET'])
def editUserPost(user_id):
    user = User.query.filter_by(user_id=user_id).all()[0]
    current_fname = user.first_name
    current_age = user.age

    form = EditUserForm()
    return render_template('edituser.html', form=form, current_user_id=user_id, current_fname=current_fname, current_age=current_age)
	


@app.route('/edituser', methods=['POST'])
def editUserGet():
    form = EditUserForm()

    if form.validate_on_submit():    
        user_id = int(request.form['user_id'])
        first_name = request.form['first_name']
        age = int(request.form['age'])
        Db.session.query(User).filter(User.user_id == user_id).update({User.first_name:first_name, User.age:age}, synchronize_session = False)
        Db.session.commit()
        return redirect(url_for('index'))

