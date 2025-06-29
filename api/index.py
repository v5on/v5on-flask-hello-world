from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'v5on - Hello, World!'

@app.route('/about')
def about():
    return 'About'
