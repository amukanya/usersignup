from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too



@app.route("/welcome", methods=['POST'])
def welcome():
    at = '@'
    point = '.'
    username = request.form['username']
    password = request.form['password']
    confpassword = request.form['confpassword']
    email = request.form['email']
    name_error =''
    pass_error =''
    confpass_error =''
    email_error =''
    if username =='':
        name_error = 'You did not enter a username.'
        username =''
    elif len(username) <= 3:
        name_error = 'Username must have more than 3 letters.'
        username =''
    
    if password =='':
        pass_error = 'You did not enter a password.'
        password =''
    elif len(password) <= 3:
        name_error = 'Username must have more than 3 letters.'
        username =''
    else:
        if confpassword != password:
            confpass_error = 'Make sure Confirmatiom password matches password.'
            confpassword =''
    if email !='':
        if len(email) < 3:
            email_error = 'Your email is too short.'
            email =''
        elif len(email) > 20:
            email_error = 'Your email is too long.'
        else:
            if not at in email:
                email_error = 'You are missing -@- .'
                email =''
            elif not point in email:
                email_error = 'You are missing -.- .'
                email =''
    
    if (not name_error and not confpass_error) and (not pass_error and not email_error):
        username_bold = "<strong>" + username + "</strong>"
        sentence = "Welcome, " + username_bold
        content = "<p>" + sentence + "</p>"
        return content
    else:
        return render_template('edit.html', name_error = name_error, pass_error = pass_error, confpass_error = confpass_error,email_error = email_error, username = username, password = password, confpassword = confpassword, email = email)

@app.route("/")
def index():
    return render_template('edit.html')
app.run()