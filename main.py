import sys
from cutomer_classes import *
from pizza_classes import *


def get_menu():
    with open("Menu.txt", "r", encoding="utf-8") as f:
        print(f.read())


def get_menu_for_code():
    with open("pizza_menu.txt", "r") as f:
        lines = f.readlines()

    pizza_menu = {}

    for line in lines:
        name, price = line.strip().split(": ")
        pizza_menu[name] = float(price)

    return pizza_menu


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


def buy_sauces():
    cost = 0
    menu = get_menu_for_code()

    while True:
        order = input("What sauce you would like to order?")

        if order.isdigit() and int(order) == 11:
            price = menu.get("Olives")
            cost += price
            return cost, "Olives"

        if order.isdigit() and int(order) == 12:
            price = menu.get("Mushrooms")
            cost += price
            return cost, "Mushrooms"

        if order.isdigit() and int(order) == 13:
            price = menu.get("GoatCheese")
            cost += price
            return cost, "GoatCheese"

        if order.isdigit() and int(order) == 14:
            price = menu.get("Meat")
            cost += price
            return cost, "Meat"

        if order.isdigit() and int(order) == 15:
            price = menu.get("Onions")
            cost += price
            return cost, "Onions"

        if order.isdigit() and int(order) == 16:
            price = menu.get("Corn")
            cost += price
            return cost, "Corn"

        if order.upper() == "N":
            break
        else:
            sys.stderr.write("You Entered Wrong Order Operation! ")
            sys.stderr.flush()

        if order == "q":
            break


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


def main():
    print("Welcome to Pizza order System made by Melis and Basri ")
    name = input("What is yur name? ")
    id_number = input("Enter your ID Number: ")
    card_num = input("Enter your Credit card number for registration: ")
    card_password = input('Enter your password for registration: ')

    customer = Customer(name, id_number, card_num, card_password)

    customer.save_to_csv(customer.name, customer.id_number, customer.card_number, customer.card_password)

    print(f"Hello MR/Ms{name}. Here is the menu below, You can only choose one pizza and one sauce at the same time! ")
    get_menu()

    result_for_pizza = buy_pizza()
    pizza_cost, pizza_name = result_for_pizza
    result_for_sauces = buy_sauces()
    sauces_cost, sauce_name = result_for_sauces
    result_for_beverage = buy_beverage()
    beverage_cost, beverage_name = result_for_beverage

    total_cost = pizza_cost + sauces_cost + beverage_cost
    pizza = Pizza(name, total_cost, pizza_name, sauce_name, beverage_name, datetime.datetime.now())
    print("--------------------------------\n")
    print(pizza)

    customer.check_payment(customer.card_number, customer.card_password)

    print("Thank you! Have a good Day!")


if __name__ == "__main__":
    main()
