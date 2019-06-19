from bottle import run, route, view, get, post, request, static_file#importing functions to help code run
from itertools import count #imports count from itertools

class canteen_food:#names the class
    _ids = count(0) #sets _ids to count(0)
    
    
    def __init__(self, name, image, stock, price, description, sold):#this function creates all the objects you want in your menu, name, stock, price ect.
        self.id = next(self._ids)
        self.food_name = name #these create the object and then rename it so it is easily referenced
        self.food_image = image
        self.food_stock = stock
        self.food_price = price
        self.food_description = description
        self.food_sold = sold
canteen_test = [ #this is the list that contains all my test data
    canteen_food("Sushi Roll Pack", "sushi.JPG", 5, 20, "Sushi Roll Pack very yum", 0),
    canteen_food("Hot Dog and Chips", "hotdog.JPG", 12, 13.5, "Hot Dog and Chips very yum", 0),
    canteen_food("Ham and Cheese sandwich", "ham.JPG", 4, 12.4, "Ham and Cheese sandwich very yum", 0) 
    ]



@route("/")#allows the python server to find the location of the webpage in my folder
@view("index")#this then displays the webpage to the user
def index():#this function will attatch the decorators above
    pass

@route("/food")
@view("food")
def menu_page():
    data = dict (food_list = canteen_test)# this makes a dictionary with all my test data
    return data # this returns the data

@route ("/tandc")
@view("tandc")
def terms_page():
    pass
        
        
@route("/success/<food_id>")#passes food_id
@view("success")
def success_page(food_id):
    food_id = int(food_id) # this sets food_id to the number of food_id
    found_food = None # sets found_food to none
    for food in canteen_test: #says for each item of food in canteen test DO
        if food.id == food_id: # if the two food id s match.
            found_food = food #set found_food to food
    data = dict(food = found_food) # sets data to the dictionary with all the test data
    found_food.food_stock -= 1 # when a food item is purchased it takes one off stock
    found_food.food_sold += 1 #also adds one to total food sold whoch I display on the table webpage

    return data    

@route("/restock")
@view("restock")
def restock_page():
    data = dict (food_list = canteen_test)
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


@route("/restock-success/<food_id>", method="POST")# method = POST is the method by which the python server recieves the food_id
@view("restock-success")
def restock_success(food_id):
    food_id = int(food_id)
    found_food = None
    for food in canteen_test:
        if food.id == food_id:
            found_food = food
            data = dict(food = found_food)
            restock = request.forms.get("restock")# gets the amount to restock off the form on the webpage
            restock = int(restock)
            found_food.food_stock = found_food.food_stock + restock
            
@route("/table")
@view("table")
def table():
    data = dict (food_list = canteen_test)
    return data

@route('/picture/<filename>')# this allows my webpage to display saved images, which I have saved under the picture folder.
def saved_pics(filename):
    return static_file(filename, root = './images')       
        
run(host = "0.0.0.0", port = 8080, reloader = True, debug = True)# this allows you to access the website on chrome, through port 8080
