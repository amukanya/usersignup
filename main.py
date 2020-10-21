from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too



@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    confpassword = request.form['confpassword']
    name_error = ''
    pass_error = ''
    confpass_error = ''
    if username == '':
        name_error = 'You did not enter a username.'
        username = ''
    if len(username) <= 3:
        name_error = 'Username must have more than 3 letters.'
        username = ''
    if password == '':
        pass_error = 'You did not enter a password.'
        password = ''
    else:
        if not confpassword == password:
            confpass_error = 'Make sure Confirmatiom password matches password.'
            confpassword = ''
    
    if not name_error and not confpass_error:
        username_bold = "<strong>" + username + "</strong>"
        sentence = "Welcome, " + username_bold
        content = "<p>" + sentence + "</p>"
        return content
    else:
        return render_template('edut.html', name_error = name_error, pass_error = pass_error, confpass_error = confpass_error, username = username, password = password, confpassword = confpassword)

@app.route("/")
def index():
    return render_template('edit.html')
app.run()