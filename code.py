from bottle import run, route, view, get, post, request, static_file#importing functions to help code run
from itertools import count

class canteen_food:
    _ids = count(0)
    
    
    def __init__(self, name, image, stock, description, price):
        self.id = next(self._ids)
        self.food_name = name
        self.food_image = image
        self.food_stock = stock
        self.food_price = price
        self.food_description = description
        
canteen_test = [
    canteen_food("Sushi Roll Pack", "", "5", "price", "description"),
    canteen_food("hot Dog and Chips", "image", "12", "price", "description"),
    canteen_food("Ham and Cheese sandwich", "image", "4", "price", "description") 
    ]



@route("/")
@view("index")
def index():#this function will attatch the decorators above
    pass
        
@route('/picture/<filename>')
def saved_pics(filename):
    return static_file(filename, root = './images')       
        
run(host = "0.0.0.0", port = 8080, reloader = True, debug = True)