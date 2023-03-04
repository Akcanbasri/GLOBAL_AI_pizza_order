# libraries which is we need.
import sys
from customer_classes import *
from pizza_classes import *
import time


# Prints Menu for user.
def get_menu():
    with open("Menu.txt", "r", encoding="utf-8") as f:
        print(f.read())


# Reads menu for our codes.
def get_menu_for_code():
    with open("pizza_menu.txt", "r") as f:
        lines = f.readlines()

    pizza_menu = {}

    for line in lines:
        name, price = line.strip().split(": ")
        pizza_menu[name] = float(price)

    return pizza_menu


# Users Choose his/her own Pizzas here.
def buy_pizza():
    cost = 0
    menu = get_menu_for_code()

    while True:
        order = input("What pizza you would like to order?")

        if order.isdigit() and int(order) == 1:
            price = menu.get("Classic")
            cost += price
            return cost, "Classic"

        if order.isdigit() and int(order) == 2:
            price = menu.get("Margherita")
            cost += price
            return cost, "Margherita"

        if order.isdigit() and int(order) == 3:
            price = menu.get("TurkPizza")
            cost += price
            return cost, "TurkPizza"

        if order.isdigit() and int(order) == 4:
            price = menu.get("PlainPizza")
            cost += price
            return cost, "PlainPizza"

        if order.upper() == "N":
            break
        else:
            sys.stderr.write("You Entered Wrong Order Operation! ")
            sys.stderr.flush()


# Users Choose his/her own Sauces here.
def buy_sauces():
    cost = 0
    menu = get_menu_for_code()

    while True:
        order = input("What sauce you would like to order?")

        if order.isdigit() and int(order) == 11:
            price = menu.get("Olives")
            cost += price
            return cost, "Olives"

        elif order.isdigit() and int(order) == 12:
            price = menu.get("Mushrooms")
            cost += price
            return cost, "Mushrooms"

        elif order.isdigit() and int(order) == 13:
            price = menu.get("GoatCheese")
            cost += price
            return cost, "GoatCheese"

        elif order.isdigit() and int(order) == 14:
            price = menu.get("Meat")
            cost += price
            return cost, "Meat"

        elif order.isdigit() and int(order) == 15:
            price = menu.get("Onions")
            cost += price
            return cost, "Onions"

        elif order.isdigit() and int(order) == 16:
            price = menu.get("Corn")
            cost += price
            return cost, "Corn"

        elif order.upper() == "N":
            break
        else:
            sys.stderr.write("You Entered Wrong Order Operation! ")
            sys.stderr.flush()

        if order == "q":
            break


# Users Choose his/her own Beverages here.
def buy_beverage():
    cost = 0
    menu = get_menu_for_code()
    while True:
        order = input("What beverage you would like to order?")

        if order.isdigit() and int(order) == 21:
            price = menu.get("Cola")
            if price is not None:
                cost += price
                return cost, "Cola"
            else:
                print("price not found beverage")

        if order.isdigit() and int(order) == 22:
            price = menu.get("Sprite")
            if price is not None:
                cost += price
                return cost, "Sprite"
            else:
                print("price not found beverage")

        if order.isdigit() and int(order) == 23:
            price = menu.get("Fusetea")
            if price is not None:
                cost += price
                return cost, "Fusetea"
            else:
                print("price not found beverage")

        if order.isdigit() and int(order) == 24:
            price = menu.get("Sevenup")
            if price is not None:
                cost += price
                return cost, "Sevenup"
            else:
                print("price not found beverage")

        if order.upper() == "N":
            break
        else:
            sys.stderr.write("You Entered Wrong Order Operation! ")
            sys.stderr.flush()

        if order == "q":
            break
    print("--------------------------------\n")


# Users Choose his/her own Extras here.
def buy_extra():
    cost = 0
    menu = get_menu_for_code()

    while True:
        order = input("What extras you would like to order?")

        if order.isdigit() and int(order) == 31:
            price = menu.get("Olives")
            cost += price
            return cost, "Olives"

        elif order.isdigit() and int(order) == 32:
            price = menu.get("SweetCorn")
            cost += price
            return cost, "SweetCorn"

        elif order.isdigit() and int(order) == 33:
            price = menu.get("Tomato")
            cost += price
            return cost, "Tomato"

        elif order.isdigit() and int(order) == 34:
            price = menu.get("Mozarella")
            cost += price
            return cost, "Mozarella"

        elif order.isdigit() and int(order) == 35:
            price = menu.get("Pickle")
            cost += price
            return cost, "Pickle"

        elif order.isdigit() and int(order) == 36:
            price = menu.get("Pepper")
            cost += price
            return cost, "Pepper"

        elif order.upper() == "N":
            break
        else:
            sys.stderr.write("You Entered Wrong Order Operation! ")
            sys.stderr.flush()

        if order == "q":
            break


# Here is our main function for our pizza simulation.
def main():
    print("Welcome to Pizza order System made by Melis and Basri ")
    # Getting info for our system.
    name = input("What is yur name? ")
    id_number = input("Enter your ID Number: ")
    card_num = input("Enter your Credit card number for registration: ")
    card_password = input('Enter your password for registration: ')

    # Creating a customer class.
    customer = Customer(name, id_number, card_num, card_password)
    # Adding customer to .csv file.
    customer.save_to_csv(customer.name, customer.id_number, customer.card_number, customer.card_password)

    print(
        f"Hello MR/Ms {name.capitalize()}.Here is the menu below,"
        f"You can only choose one pizza and one sauce at the same time! ")

    # Calling get menu function.
    get_menu()

    # Getting Pizza name info for our bill.
    result_for_pizza = buy_pizza()
    pizza_cost, pizza_name = result_for_pizza
    time.sleep(1)
    print("\n")

    # Getting Sauces name info for our bill.
    sauce_count = int(input("How many sauces would you like to add to your pizza? "))
    i = 0
    total_sauce_price = 0
    sauces_name_list = list()

    if 1 <= sauce_count < 4:
        while i < sauce_count:
            result_for_sauces = buy_sauces()
            sauces_cost, sauce_name = result_for_sauces
            total_sauce_price += sauces_cost
            sauces_name_list.append(sauce_name)
            i += 1
    else:
        sys.stderr.write("You can only choose between 1 and 3 sauces!")
        sys.stderr.flush()
    time.sleep(1)
    print("\n")

    # Getting Beverage name info for our bill.
    result_for_beverage = buy_beverage()
    beverage_cost, beverage_name = result_for_beverage
    time.sleep(1)
    print("\n")

    # Getting Extras name info for our bill.
    extra_count = int(input("How many extras would you like to add to your pizza? "))
    i = 0
    total_extra_price = 0
    extras_name_list = list()

    if 1 <= extra_count <= 6:
        while i < extra_count:
            result_for_extras = buy_extra()
            extras_cost, extra_name = result_for_extras
            total_extra_price += extras_cost
            extras_name_list.append(extra_name)
            i += 1
    else:
        sys.stderr.write("You can only choose between 1 and 6 extras!")
        sys.stderr.flush()
    time.sleep(1)
    print("\n")

    # Calculating total price for our pizza with its price.
    total_cost = pizza_cost + total_sauce_price + beverage_cost + total_extra_price
    pizza = Pizza(name, total_cost, pizza_name, sauces_name_list, beverage_name, datetime.datetime.now(),
                  extras_name_list)
    print("--------------------------------")
    #  Checking customer's card number and password from .csv file
    print("Your payment is checking....\n")
    time.sleep(2)
    customer.check_payment(customer.card_number, customer.card_password)
    print(pizza)
    print("Thank you! Have a good Day!")
    print("--------------------------------")


# Calling main function
if __name__ == "__main__":
    main()
