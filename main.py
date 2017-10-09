from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/verify', methods=['POST'])
def verify():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_and_email_url_string = "&username=" + username + "&email=" + email

    if not username:
        error = "Please enter a value"
        return redirect("/?username_error=" + error + username_and_email_url_string)

    if not password:
        error = "Please enter a value"
        return redirect("/?password_error=" + error + username_and_email_url_string)

    if (" " in password) or (len(password) < 3) or (len(password) > 20):
        error = "Invalid password"
        return redirect("/?password_error=" + error + username_and_email_url_string)

    if not verify_password:
        error = "Please enter a value"
        return redirect("/?v_password_error=" + error + username_and_email_url_string)
    
    if password != verify_password:
        error = "Passwords don't match"
        return redirect("/?v_password_error=" + error + username_and_email_url_string)    

    if (len(email) != 0):
        if (" " in email) or (len(email) < 3) or (len(email) > 20) or ("@" not in email) or ("." not in email):
            error = "Invalid email address"
            return redirect("/?email_error=" + error + username_and_email_url_string)

    name = request.form['username']
    return render_template('welcome.html', name=name)

app.run()