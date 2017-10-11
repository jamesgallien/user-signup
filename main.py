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

    if not username:
        error = "Please enter a value"
        return render_template("signup.html", username_error=error, username=username, email=email)

    if not password:
        error = "Please enter a value"
        return render_template("signup.html", password_error=error, username=username, email=email)

    if (" " in password) or (len(password) < 3) or (len(password) > 20):
        error = "Invalid password"
        return render_template("signup.html", password_error=error, username=username, email=email)

    if not verify_password:
        error = "'Password' and 'Verify Password' are required fields"
        return render_template("signup.html", password_error=error, p_verify_error=error, username=username, email=email)
    
    if password != verify_password:
        error = "Passwords must match"
        return render_template("signup.html", password_error=error, p_verify_error=error, username=username, email=email)    

    if (len(email) != 0):
        if (" " in email) or (len(email) < 3) or (len(email) > 20) or ("@" not in email) or ("." not in email):
            error = "Invalid email address"
            return render_template("signup.html", email_error=error, username=username, email=email)

    name = request.form['username']
    return render_template('welcome.html', name=name)

app.run()