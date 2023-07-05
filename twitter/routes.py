from flask import render_template
from twitter import app


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/profile")
def profile():
    return render_template('profile.html', title='profile')


@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('register.html', title='Register')


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Login')


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/feed")
def feed():
    return render_template('feed.html', title='Feed')

@app.route("/settings")
def settings():
    return render_template('settings.html', title='settings')