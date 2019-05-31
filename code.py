from bottle import run, route, view, get, post, request, static_file#importing functions to help code run
from itertools import count

class canteen_food:
    _ids = count(0)
    
    
    def __init__(self, name, image, stock, price, description):#allows my list to find the right name, stock ect
        self.id = next(self._ids)
        self.food_name = name
        self.food_image = image
        self.food_stock = stock
        self.food_price = price
        self.food_description = description
        
canteen_test = [
    canteen_food("Sushi Roll Pack", "sushi.JPG", 5, 21, "Sushi Roll Pack veri yewmi"),
    canteen_food("Hot Dog and Chips", "hotdog.JPG", 12, 13.50, "Hot Dog and Chips very yum"),
    canteen_food("Ham and Cheese sandwich", "ham.JPG", 4, 100000, "Ham and Cheese sandwich for old people") 
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

    return data    

@route("/restock/<food_id>")
@view("restock")
def restock_page(food_id):
    data = dict(food=canteen_test)
    return data


@route('/restock-success/<food_id>', method='POST')
@view("restock-success")
def restock_success(food_id):
    food_id = int(food_id)
    found_food = None
    for food in canteen_test:
        if food.id == food_id:
            found_food = food
            data = dict(food = found_item)
            restock = request.forms.get(restock)
            found_food.stock = found_food.stock + restock

@route('/picture/<filename>')
def saved_pics(filename):
    return static_file(filename, root = './images')       
        
run(host = "0.0.0.0", port = 8080, reloader = True, debug = True)
