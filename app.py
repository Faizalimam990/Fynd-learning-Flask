from flask import Flask, request, render_template,redirect
from markupsafe import escape
from models import Products
from database import session

app = Flask(__name__)

@app.route('/')
def Homepage():
    return render_template("index.html")

@app.route('/products/')
def productpage():
    
    product_get=get_product()
    

    return render_template("productpage.html",product_get=product_get)



# @app.route('/addproducts/',methods=['POST','GET'])
# def addproductpage():
    
#     name=request.form['name']
#     price=int(request.form['Price'])
#     quantity=int(request.form['quantity'])
#     addproduct(name,price,quantity)
#     return "<h1>Product added</h1>"
        
@app.get('/addproducts/')
def product_add():
    return render_template('addproduct.html')   


@app.post('/addproducts/')
def product_post():
    name=request.form['Name']
    price=int(request.form['Price'])
    quantity=int(request.form['quantity'])
    addproduct(name,price,quantity)
    return redirect ('/products/')

def addproduct(name,price,quantity):
    product1=Products(Name=name,Price=price,quantity=quantity)
    session.add(product1)
    session.commit()

def get_product():
    return session.query(Products).all()


@app.route('/users/',methods=['GET','POST'])
def userspage():
    if request.method == 'GET':
        firstname = request.args.get('fname')
        lastname = request.args.get('lname')
        return f'<h1>Users page: {firstname} {lastname}</h1> <p>This is a Get Page</p> '
    
    elif request.method == 'POST':
        firstname = request.form['fname']
        lastname = request.form['lname']
        return f'<h1>Users page: {firstname} {lastname}</h1> <P>This is a Post Page</p> '


@app.route('/form/')
def formpage():

    return    render_template('users.html')






if __name__ == "__main__":
    app.run(debug=True)