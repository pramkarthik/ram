from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session

# Sample food items
FOOD_MENU = [
    {'id': 1, 'name': 'Margherita Pizza', 'price': 250},
    {'id': 2, 'name': 'Veg Burger', 'price': 150},
    {'id': 3, 'name': 'Pasta Alfredo', 'price': 300},
    {'id': 4, 'name': 'French Fries', 'price': 100},
]

@app.route('/')
def index():
    return render_template('index.html', menu=FOOD_MENU)

@app.route('/add/<int:item_id>')
def add_to_cart(item_id):
    cart = session.get('cart', {})
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    items = []
    total = 0
    for item_id, quantity in cart.items():
        for food in FOOD_MENU:
            if food['id'] == int(item_id):
                item_total = food['price'] * quantity
                total += item_total
                items.append({
                    'name': food['name'],
                    'price': food['price'],
                    'quantity': quantity,
                    'total': item_total
                })
    return render_template('cart.html', items=items, total=total)

@app.route('/clear')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)
