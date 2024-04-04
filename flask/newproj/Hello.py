from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('score.html', marks = score)

if __name__ == '__main__':
   app.run(debug=True) #debug=True will reload the server each time you make a change to the code and save it.

                     # host='0.0.0.0' will make your server available from any IP address. 
