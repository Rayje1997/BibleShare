from flask import Flask, render_template, url_for, session, request, redirect
import json
import random

#######################################
# initial variable setup
######################################

# loads the Bible from KJV.json into a dictionary
with open('static/js/KJV.json') as b:
    bible = json.load(b)
# loads users.json into a dictionary
with open('static/js/users.json') as u:
    users = json.load(u)
app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = str(random.randrange(1000000))

########################################
# end of variable setup
#######################################

@app.route('/', methods = ['GET', 'POST'])
def index():
    """Controller function for the login page"""

    return render_template('index.html')

@app.route('/home')
def home():
    """Controller function for the home page"""
    return render_template('home.html', bible = bible)

@app.route('/checkLogin', methods = ['GET', 'POST'])
def checkLogin():

    error = None

    if request.method == 'POST':
        for user in range(len(users)):
            if request.form['username'] == users[user]['username']:
                session['username'] = request.form['username']
                return redirect(url_for('home'))
            else:
                error = "Invalid login credentials. Please login."
                return redirect(url_for('index'))
    return render_template('checkLogin.html')


if __name__ == '__main__':
    app.run(debug = True)
