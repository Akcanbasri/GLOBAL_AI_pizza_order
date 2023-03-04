class Pizza:
    def __init__(self, name, total_cost, pizza_name, sauce_name, beverage_name, time):
        self.name = name
        self.sauce = sauce_name
        self.total_cost = total_cost
        self.pizza_name = pizza_name
        self.time = time
        self.beverage_name = beverage_name

    def __str__(self):
        return f"Hello {self.name}. Here is your order details.\n\nYou ordered at {self.time}\n{self.pizza_name}" \
               f" with {self.sauce} sauce(s) and {self.beverage_name}\nYour bill is ${self.total_cost}"
