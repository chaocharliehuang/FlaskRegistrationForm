from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process():
    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password']
    session['confirm_pw'] = request.form['confirm_pw']

    if len(session['email']) < 1 or len(session['first_name']) < 1 or len(session['last_name']) < 1 or len(session['password']) < 1 or len(session['confirm_pw']) < 1:
        flash('No fields can be blank!')
    elif not session['first_name'].isalpha() or not session['last_name'].isalpha():
        flash('First and last names cannot contain any numbers!')
    elif len(session['password']) <= 8 or len(session['confirm_pw']) <= 8:
        flash('Password must be longer than 8 characters!')
    elif not EMAIL_REGEX.match(session['email']):
        flash('Invalid email address!')
    elif session['password'] != session['confirm_pw']:
        flash('Passwords don\'t match!')
    else:
        session.clear()
        flash('Thanks for submitting your information.')
    return redirect('/')

app.run(debug=True)