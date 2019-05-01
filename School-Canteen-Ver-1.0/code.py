from bottle import run, route, view, get, post, request, staticfile
from itertools import count

class school_canteen:
    _ids = count(0)
    
    
    def __init__(self, name, image, stock, description):
        self.id = next(self._ids)
        self.food_name = name
        self.food_image = image
        self.food_stock = stock
        self.food_price = price
        self.food_description = description
        
canteen_test = [
    
    
    
    
    
    ]
        
    