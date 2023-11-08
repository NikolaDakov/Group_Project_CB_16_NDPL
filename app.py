from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary to store predefined user credentials
user1 ={'Mario12': '12'}
user2 ={'Luigi13': '13'}

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
# -----------------------------------------------------------------------------------------------------------------------
# this will be for trasfer data from menuPage to mario and luigi's pages
# Create a list to store orders (you can replace this with a database)
# Logic and Conecting
orders = []

@app.route('/MenuPage', methods=['POST'])
def place_order():
    item_name = request.form['item_name']
    item_price = float(request.form['item_price'])
    
    # You can add more processing here, e.g., calculating total price

    order = {
        'Name': item_name,
        'Price': item_price,
    }
    
    orders.append(order)
     # Format the orders list
    formatted_orders = []
    for order in orders:
        formatted_order = f'Pizza: {order["Name"]} Price: {order["Price"]} Euro'
        formatted_orders.append(formatted_order)
    # print(formatted_orders)
    return render_template('MenuPage.html', formatted_orders=formatted_orders )
# ---------------------------------------------------------------------------------------------------------------
#redirect orders to luigi
@app.route("/orderbutton", methods=['POST'])
def orderbutton():
    return render_template("/marioPage.html", orders=orders)
#redirect orders to Luigi

# -------------------------------------------------------------------------------------------------------------------5
# Reset Function
@app.route('/resetbutton', methods=['POST'])
def resetbutton():
    orders.clear()
    print(orders)
    return redirect('/MenuPage')

# -----------------------------------------------------------------------------------------------------------------------
# Route to display the 'marioPage.html'
@app.route('/marioPage')
def mario_page():
    return render_template('marioPage.html')  

#route to display LuigiPage or KitchenPage
@app.route('/kitchenPage')
def kitchenPage():
    return render_template('kitchenPage.html', orders=orders) 

# Route to display the 'invalidMessage.html'
@app.route('/invalidMessage')
def invalid_message():
    return render_template('invalidMessage.html')

# Route  to display the menupage!
@app.route('/MenuPage')
def MenuPage():
    return render_template('MenuPage.html')  

if __name__ == '__main__':
    app.run()
