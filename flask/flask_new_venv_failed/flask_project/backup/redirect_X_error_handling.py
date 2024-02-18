from flask import abort, redirect, url_for, render_template

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('unauthorized'))

@app.route('/unauthorized')
def unauthorized():
    abort(401)
    hello()

@app.route('/404')
def error404():
    return render_template('404.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
    
