'''
alarm clock should
    keep track of current time
    if it's on or off
    time it's set to

    have a method to set or change the current time and print it to the console

    when I import it here, I want to print the time, call the change time method to change the time, and toggle the alarm off

'''

from alarm_clock import Alarm_clock

alarm_clock = Alarm_clock("12:09", True, "14:00" )

# alarm_clock.change_current_time()

alarm_clock.status = False

print(alarm_clock.status)


'''
in main.py
    import customer and product classes and instantiate a customer as well as three products
        print customer name
        call customer's add product to shopping cart three times and add the three products you created
        call the customer's view products method
        call the customer's shopping cart get total method. reurn this and print it
        call the customer's shopping cart emtpy cart method
        check if all products have been removed
'''

from customer import Customer
from product import Product
from shopping_cart import Shopping_cart

customer_1 = Customer("Emily", "")

laffy_taffy = Product("laffy taffy", 5, "food")
coca_cola = Product("coca cola", 6.50, "drink")
popcorn = Product("popcorn", 7.50, "food")

print(customer_1.name)



customer_1.add_to_shopping_cart(laffy_taffy)
customer_1.add_to_shopping_cart(coca_cola)
customer_1.add_to_shopping_cart(popcorn)

current_cart = customer_1.view_all_in_cart()
result = customer_1.shopping_cart.calculate_total()
print(result)

customer_1.shopping_cart.empty_cart()
current_cart = customer_1.view_all_in_cart()

