from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

# Dictionary to store predefined user credentials
user1 ={'Mario12': 'k12'}
user2 ={'Luigi13': 'k13'}

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

        if username in user1 and user1[username] == password:
            return redirect('/marioPage')  # Redirect to the 'marioPage' route
        elif username in user2 and user2[username] == password:
            return redirect('/kitchenPage')  # Redirect to the 'luigiPage/kitchenPage' route
        else:
            return redirect('/invalidMessage')

# Route to display the 'marioPage.html'
@app.route('/marioPage')
def mario_page():
    return render_template('marioPage.html')  

@app.route('/kitchenPage')
def kitchenPage():
    return render_template('kitchenPage.html') #route to display LuigiPage or KitchenPage

# Route to display the 'invalidMessage.html'
@app.route("/invalidMessage")
def invalid_message() :
    return render_template('invalidMessage.html')

if __name__ == '__main__':
    app.run()
