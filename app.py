from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dictionary to store predefined user credentials
users = {
    'Mario12': '12',
    'Luigi13': '13'
}

# Route for rendering the login form
@app.route('/')
def view_form():
    return render_template('loginStaff.html')  

# Route to handle login 
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return redirect('/marioPage')  # Redirect to the 'marioPage' route
        else:
            return '<h1>Invalid credentials!</h1>'

# Route to display the 'marioPage.html'
@app.route('/marioPage')
def mario_page():
    return render_template('marioPage.html')  

if __name__ == '__main__':
    app.run()
