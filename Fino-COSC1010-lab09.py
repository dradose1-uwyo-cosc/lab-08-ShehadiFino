# Shehadi Fino
# UWYO COSC 1010
# 11-11-24
# Lab 09
# Lab Section:14
# Sources, people worked with, help given to: Ryan
# Your
# Comments
# Here


# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
# - If it is not, default to a 10" pizza (you can store ten). These checks should
# occur in init as well.
# - For toppings, you will need to add the toppings.
# - This method needs to be able to handle multiple values.
# - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety
# checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.


# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per
# inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the
# list.
# You will need the following methods:
# - __init__()
# - This one does not need to take in any extra parameters.
# - It should create and set the attributes defined above.
# - placeOrder():
# - This method will allow a customer to order a pizza.
# - Which will increment the number of orders.
# - It will need to create a pizza object.
# - You will need to prompt the user for:
# - the size
# - the sauce, tell the user if nothing is entered it will default to red sauce
# (check for an empty string).
# - all the toppings the user wants, ending prompting on an empty string.
# - Implementation of this is left to you; you can, for example:
# - have a while loop and append new entries to a list
# - have the user separate all toppings by a space and turn that into a list.
# - Upon completion, create the pizza object and store it in the list.
# - getPrice()
# - You will need to determine the price of the pizza.
# - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings()
# * price_per_topping.
# - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
# - Creates a receipt of the current pizza.
# - Show the sauce, size, and toppings.
# - Show the price for the size.
# - The price for the toppings.
# - The total price.
# - getNumberOfOrders()
# - This will simply return the number of orders.


# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.

class Pizza:
    def __init__(self, size, sauce = "red"):
        self.set_Size(size)
        self.sauce = sauce
        self.toppings = ["cheese"]

    def get_size(self):
        return self.size

    def set_Size(self, size):
        if isinstance(size, int) and size >= 10:
            self.size = size
        else:
            self.size = 10

    def get_sauce(self):
        return self.sauce
    
    def get_toppings(self):
        return self.toppings

    def set_toppings(self, *toppings):
        self.toppings.extend(toppings)

    def amount_of_toppings(self):
        return len(self.toppings)

class Pizzeria:
    price_per_topping = 0.30
    price_per_inch = 0.60

    def __init__(self):
        self.orders = 0
        self.pizzas = []

    def place_order(self):
        try:
            size = int(input("Enter pizza size as a whole number in inches. Smallest size is 10): "))
        except ValueError:
            size = 10
        sauce = input("Enter preferred pizza sauce (leave empty for red sauce): ")
        if sauce == "":
            sauce = "red"
            
        toppings = []
        while True:
            topping = input("Enter your choice of toppings(leave empty to finsih): ")
            if topping == "":
                break
            toppings.append(topping)
        pizza = Pizza(size, sauce)
        pizza.set_toppings(*toppings)
        self.pizzas.append(pizza)
        self.orders += 1

    def get_price(self, pizza):
        size_cost = pizza.get_size() * self.price_per_inch
        toppings_cost = pizza.amount_of_toppings() * self.price_per_topping
        total_price = size_cost + toppings_cost
        return total_price

    def get_receipt(self, pizza):
        size_cost = pizza.get_size() * self.price_per_inch
        toppings_cost = pizza.amount_of_toppings() * self.price_per_topping
        total_price = self.get_price(pizza)

        print(f"\nYou ordered a {pizza.get_size()} inch pizza with {pizza.get_sauce()} sauce and these toppings: ")
        for topping in pizza.get_toppings():
            print(topping)

        print(f"\nYou ordered a {pizza.get_size()} pizza for ${size_cost:.2f}")
        print(f"You ordered {pizza.amount_of_toppings()} topping(s) for ${toppings_cost:.2f}")
        print(f"Your total price is: ${total_price:.2f}")

    def number_of_orders(self):
        return self.orders 

pizzeria = Pizzeria()

while True:
    order = input("Would you like to place an order? (Type 'exit' to exit): ")
    if order.lower() == "exit":
        break

    pizzeria.place_order()
    pizzeria.get_receipt(pizzeria.pizzas[-1])

print(f"Total orders placed: {pizzeria.number_of_orders()}")




    