from flask import Flask, render_template, request, session, redirect, url_for
import datahandler


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route("/register")
def render_form_page():
    return render_template('form.html', act="Register")


@app.route("/register-user", methods=["POST"])
def register_user():
    username = request.form["username"]
    password = request.form["password"]
    if datahandler.insert_user(username, password):
        session['username'] = username
        return render_template('index.html', username=username)
    else:
        return render_template('form.html', act="Register", errormsg="Username already exists!")


@app.route("/login")
def login_page():
    return render_template('form.html', act="Login")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('hello'))


@app.route("/login-user", methods=["POST"])
def user_login():
    username = request.form['username']
    password = request.form['password']
    if datahandler.check_user(username, password):
        session['username'] = username
        return render_template('index.html', username=username)
    return render_template('form.html', act="Login",
                           errormsg="Invalid Username/Password combination provided.")


@app.route("/")
def hello():
    return render_template('index.html')


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
