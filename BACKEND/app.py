from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database (you can replace this with a real database)
products_db = [
    {"id": 1, "name": "Product 1", "price": 100, "description": "Description for Product 1"},
    {"id": 2, "name": "Product 2", "price": 200, "description": "Description for Product 2"},
    {"id": 3, "name": "Product 3", "price": 300, "description": "Description for Product 3"}
]

# Home Route
@app.route('/')
def home():
    return render_template('home.html')

# Products Listing Route
@app.route('/products')
def products():
    return render_template('products.html', products=products_db)

# Individual Product Detail Route
@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products_db if p['id'] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    return "Product not found", 404

# Admin Add Product Route (GET and POST)
@app.route('/admin/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        new_product = {
            "id": len(products_db) + 1,
            "name": request.form['name'],
            "price": float(request.form['price']),
            "description": request.form['description']
        }
        products_db.append(new_product)
        return redirect(url_for('products'))
    return render_template('add_product.html')

if __name__ == '__main__':
    app.run(debug=True)