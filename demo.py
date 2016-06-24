import math
from flask import Flask, request, render_template, session
app = Flask(__name__)

@app.route('/hello')
def return_hello_message():
    return 'hello, world!'

@app.route('/showform')
def show_form():
    return render_template('form.html')

@app.route('/factorial', methods=['POST'])
def calc_factorial():
    n = int(request.form['number'])
    nfac = math.factorial(n)
    return render_template('factorial.html', source = n, result = nfac)    

@app.route('/account/<id>')
def show_account(id):
    return 'account #' + id

app.secret_key='dfajdsfa;lsdkjfa;ldkfja;dkf'

@app.route('/login')
def login():
    username = 'John Smith'
    session['username'] = username
    return 'logged in as ' + username

@app.route('/whoami')
def show_whoami():
    return 'I am ' + session['username']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8800, debug=True)

