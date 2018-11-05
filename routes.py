from flask import Flask, render_template, url_for

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug = True)
