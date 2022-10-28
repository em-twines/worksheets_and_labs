
'''
shopping cart
    have a method to calcuate and return the current total of all products in the cart
    have a method to add new products to the cart (appending the product's list)
    have a method to empty all products from the cart
'''

from product import Product

class Shopping_cart:
    def __init__(self):
        self.item_list = []
        # self.item = ""
        
    def add_product(self, product_to_add):
        self.item_list.append(product_to_add)
        return self.item_list
        
    def calculate_total(self):
        self.item_list
        total = 0
        for product in self.item_list:
            total += product.price
        return total

    def empty_cart(self):
        self.item_list.clear()

