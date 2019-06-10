from bottle import run, route, view, get, post, request, static_file#importing functions to help code run
from itertools import count

class canteen_food:
    _ids = count(0)
    
    
    def __init__(self, name, image, stock, price, description, sold):#allows my list to find the right name, stock ect
        self.id = next(self._ids)
        self.food_name = name
        self.food_image = image
        self.food_stock = stock
        self.food_price = price
        self.food_description = description
        self.food_sold = sold
canteen_test = [
    canteen_food("Sushi Roll Pack", "sushi.JPG", 5, 21, "Sushi Roll Pack veri yewmi", 0),
    canteen_food("Hot Dog and Chips", "hotdog.JPG", 12, 13.5, "Hot Dog and Chips very yum", 0),
    canteen_food("Ham and Cheese sandwich", "ham.JPG", 4, 12.4, "Ham and Cheese sandwich for old people", 0) 
    ]



@route("/")
@view("index")
def index():#this function will attatch the decorators above
    pass

@route("/food")
@view("food")
def menu_page():
    data = dict (food_list = canteen_test)
    return data

@route ("/tandc")
@view("tandc")
def terms_page():
    pass
        
        
@route("/success/<food_id>")
@view("success")
def success_page(food_id):
    food_id = int(food_id)
    found_food = None
    for food in canteen_test:
        if food.id == food_id:
            found_food = food
    data = dict(food = found_food)
    found_food.food_stock -= 1
    found_food.food_sold += 1

    return data    

@route("/restock/<food_id>")
@view("restock")
def restock_page(food_id):
    
    food_id = int(food_id)
    found_food = None
    for food in canteen_test:
        if food.id == food_id:
            found_food = food
    data = dict(food_list = found_food)    

    return data


@route("/restock-success/<food_id>", method="POST")
@view("restock-success")
def restock_success(food_id):
    food_id = int(food_id)
    found_food = None
    for food in canteen_test:
        if food.id == food_id:
            found_food = food
            data = dict(food = found_food)
            restock = request.forms.get("restock")
            restock = int(restock)
            found_food.food_stock = found_food.food_stock + restock
            
@route("/table")
@view("table")
def table():
    data = dict (food_list = canteen_test)
    return data

@route('/picture/<filename>')
def saved_pics(filename):
    return static_file(filename, root = './images')       
        
run(host = "0.0.0.0", port = 8080, reloader = True, debug = True)
