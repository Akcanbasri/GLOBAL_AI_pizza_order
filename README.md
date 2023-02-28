This Codes Writed by Hasan Basri Akcan and Melis İldireci

# GLOBAL_AI_pizza_order

The main() function is the central part of a pizza order system program, which allows customers to order a pizza and add sauce toppings. It starts by greeting the user and asking for their name, ID number, credit card number, and password to register the customer's details.

Once the customer's details are registered, the function displays the pizza menu and prompts the customer to enter their order, one pizza and one sauce topping at a time. The program uses the buy_pizza() and buy_sauces() functions to get the customer's orders and calculate the total cost of the order.

After getting the orders and calculating the cost, the function creates a Pizza object with the customer's name, total cost, pizza name, sauce name, and the current date and time. The function then calls the check_payment() method of the Customer class to validate the payment using the customer's registered credit card details.

Finally, the program displays the order details and thanks the customer for their order.
