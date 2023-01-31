from flask import Flask, render_template
app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('landingpage.html')

@app.route('/login')
def indexa():
    return render_template('login.html')

@app.route('/signup')
def indexb():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
