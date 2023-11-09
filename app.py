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
# Logic and Conecting
orders = []
total_price = 0
in_progress_orders = []
cooked_orders = []

@app.route('/MenuPage', methods=['POST'])
def place_order():
    item_name = request.form['item_name']
    item_price = float(request.form['item_price'])
  
    order = {
        'Name': item_name,
        'Price': item_price,
        
    }
    orders.append(order)

     # Format the orders list
    formatted_orders = []
    for order in orders:
        formatted_order = f'Product: {order["Name"]} Price: {order["Price"]} Euro'
        formatted_orders.append(formatted_order)


    # calculate total price
    global total_price
    total_price += item_price

    return render_template('MenuPage.html', formatted_orders=formatted_orders, total_price=total_price)
# ---------------------------------------------------------------------------------------------------------------

#redirect orders to luigi
@app.route("/orderbutton", methods=['POST'])
def orderbutton():
    global orders, total_price
    return render_template("/marioPage.html", orders=orders, total_price=total_price)


# -------------------------------------------------------------------------------------------------------------------5
# Take in button
# Route for the "Take In" button
@app.route('/takeIn', methods=['POST'])
def take_in():
    global orders, in_progress_orders
    in_progress_orders = orders.copy()
    # print(in_progress_orders)
    orders.clear()
    print(orders)
    return render_template('KitchenPage.html', in_progress_orders=in_progress_orders)
# -------------------------------------------------------------------------------------------------------------------------
# Go to Oven Button
@app.route('/go_to_oven', methods=['POST'])
def go_to_oven():
    global orders, cooked_orders
    cooked_orders = in_progress_orders.copy()
    in_progress_orders.clear()
    return render_template("KitchenPage.html", cooked_orders=cooked_orders)
# ----- -------------------------------------------------------------------------------------------------------------------
# Reset Function

@app.route('/resetbutton', methods=['POST'])
def resetbutton():
    orders.clear()
    global total_price
    total_price = 0
    return redirect('/MenuPage')
# -----------------------------------------------------------------------------------------------------------------------

# Route to display the 'marioPage.html'
@app.route('/marioPage')
def mario_page():
    global orders, in_progress_orders
    global total_price, cooked_orders
    return render_template('marioPage.html', orders=orders, total_price=total_price, in_progress_orders=in_progress_orders, cooked_orders=cooked_orders)  



#route to display KitchenPage
@app.route('/kitchenPage')
def kitchenPage():
    global orders, in_progress_orders
    return render_template('kitchenPage.html', orders=orders, in_progress_orders=in_progress_orders) 


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
