from flask import Flask, render_template, url_for
import json

# loads the Bible from KJV.json into a dictionary
with open('static/js/KJV.json') as b:
    bible = json.load(b)

# loads users.json into a dictionary
with open('static/js/users.json') as u:
    users = json.load(u)

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/home')
def home():
    return render_template('home.html', bible = bible)

if __name__ == '__main__':
    app.run(debug = True)
