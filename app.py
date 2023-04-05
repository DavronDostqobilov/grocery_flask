from flask import Flask,request
from db import GroceryDB

app = Flask(__name__)
db = GroceryDB()


# view all grocery
@app.route('/grocery')
def all_grocery():
    """Get all grocery"""
    produkt=db.table.all()
    table=f"""
    <table border=1> 
    <tr>
    <th>Name</th>
    <th>Quantity</th>
    <th>Price</th>
    <th>Type</th>
    </tr>
    """
    for i in produkt:
        table+=f"""
        <tr>
        <td>{i['name']}</td>
        <td>{i['quantity']}</td>
        <td>{i['price']}</td>
        <td>{i['type']}</td>
        </tr>
        """
    table+='</table>'
    return table

# view add grocery
@app.route('/grocery/add', methods=['POST'])
def add_grocery():
    """Add a grocery"""
    data=request.get_json()
    db.add(data)
    return {
            "name": "Carrrot",
            "quantity": 10,
            "price": 1.15,
            "type": "vegetable"
        }


# view all grocery by type
@app.route('/grocery/type/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    return db.get_by_type(type)


# view all grocery by name
@app.route('/grocery/name/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    return db.get_by_name(name)


# view all grocery by price
@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    return db.get_by_price(price)



if __name__ == '__main__':
    app.run(debug=True, port=5566)