from flask import Flask, request, render_template
from markupsafe import escape
from models import Products
from database import session

app = Flask(__name__)

@app.route('/')
def Homepage():
    return render_template("Index.html")

@app.route('/products/')
def productpage():
    addproduct()
    product_get=get_product()
    

    return render_template("Productpage.html",product_get=product_get)




def addproduct():
    product1=Products(Name="Marvel Spiderman",Price=499,quantity=10)
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