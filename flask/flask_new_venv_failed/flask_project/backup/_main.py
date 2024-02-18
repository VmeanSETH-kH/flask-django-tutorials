from flask import Flask
from flask import url_for

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # Adjust port if needed

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/hello/vimeanseth')
def vimeanseth():
    return 'I am VimeanSETH, a 3rd year student at Department of EECS, Kyushu Univeristy'

@app.route('/hello/<username>')
def hello_username(username):
    return f'Hello, {username}. Welcome to my page!'

# '/static/style.css' is the path to the file
# url_for('static', filename='style.css')
