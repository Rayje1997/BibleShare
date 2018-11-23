from flask import Flask, render_template, url_for, session, request
import json
import random

# loads the Bible from KJV.json into a dictionary
with open('static/js/KJV.json') as b:
    bible = json.load(b)

# loads users.json into a dictionary
with open('static/js/users.json') as u:
    users = json.load(u)

app = Flask(__name__)
app.static_folder = 'static'

app.secret_key = random.randrange(1000000)

@app.route('/', methods = ['GET', 'POST'])
def index():
    """Controller function for the login page"""
    return render_template('index.html', users=users)

@app.route('/home')
def home():
    """Controller function for the home page"""
    return render_template('home.html', bible = bible)

@app.route('/checkLogin', methods=['GET', 'POST'])
def checkLogin():
    """Controller function for the checkLogin page"""
    return render_template('checkLogin.html', userData = request.data)


if __name__ == '__main__':
    app.run(debug = True)
