import os 
# this is my juntos project
from app import app
from flask import render_template, request, redirect, session, url_for

app.secret_key = b'\xfe\xd9\xb5\xdd\xec\x03\xf4GT\xa9\xccA\xf8\xa2\xb0\x80'


from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'social_network' 

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin2:B69f7f4X5TWCLjb@cluster0-zdqji.mongodb.net/social_network?retryWrites=true&w=majority' 

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
     #connect to the database
    collection = mongo.db.users
    #pull data from database
    events = collection.find({}).sort("date", -1)
    #use data
    return render_template('index.html')

# CONNECT TO DB, ADD DATA

@app.route('/signuppage', methods=['GET','POST'])

def signup():
    if request.method == "POST":
        #take in the info they gave us, check if username is taken, if username is available then put into a database of users
        users = mongo.db.users
        existing_user = users.find_one({"username":request.form['username']})
        if existing_user is None:
            users.insert({"username":request.form['username'], "password": request.form['password']})
            return render_template ('feed.html')
        else: 
            return "That username is taken. Try logging in, or try a different username"
    else:
        return render_template ('signuppage.html')

        
@app.route('/feed', methods=['GET', 'POST'])

def feed():
    #connect to database
    collection = mongo.db.users
    #Pull data 
    events = collection.find({}).sort("date", -1)
    #use data
    return render_template('feed.html')

# LOG IN
@app.route('/login', methods=['POST', 'GET'])

def login():
    if request.method == "POST":
        #take in the info they gave us, check if username is taken, if username is available then put into a database of users
        users = mongo.db.users
        existing_user = users.find_one({"username":request.form['username']})
        if existing_user is None:
            return render_template ('signuppage.html')
        else: 
            return render_template ('feed.html')
    else:
        return render_template('login.html')  

    
# LOG OUT

@app.route('/logout')

def logout():
    session.clear()
    return redirect('/')
    
#s def feed():
#     if request.method == "POST":
#         #take in the info they gave us, check if username is taken, if username is available then put into a database of users
#         users = mongo.db.users
#         existing_user = users.find_one({"username":request.form['username']})
#         if existing_user is None:
#             users.insert({"username":request.form['username'], "password": request.form['password']})
#             return render_template ('feed.html')
#         else: 
#             return "That username is taken. Try logging in, or try a different username"
#     else:
#         return render_template('feed.html')  

