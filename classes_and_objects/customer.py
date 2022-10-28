'''
customer 
    have class instance varibles to keep track of name and shopping cart object. 
    **set the shopping cart instance variable equal to a new shopping cart object in the initializer 
    class initializer should take in the initial value of the customer's name via a parameter
    have a method to add a new product to the shopping cart (using shopping cart's add product method)
    have a method to view all products in the customer's shopping cart (by looping over the shopping cart's product list and printing each product to the terminal)
'''
# from product import Product
from typing import Concatenate
from shopping_cart import Shopping_cart

class Customer: 
    def __init__(self, customer_name, item):
        self.name = customer_name
        self.item = item
        self.shopping_cart = Shopping_cart()

    def add_to_shopping_cart(self, item):
       self.shopping_cart.item_list = self.shopping_cart.add_product(item)
        
    def view_all_in_cart(self):
        items = []
        for name in self.shopping_cart.item_list:
            item = name.name
            print(item)            
        
