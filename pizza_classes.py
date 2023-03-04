class Pizza:
    def __init__(self, name, total_cost, pizza_name, sauce_name, beverage_name, time, extra):
        self.name = name
        self.sauce = sauce_name
        self.total_cost = total_cost
        self.pizza_name = pizza_name
        self.time = time
        self.beverage_name = beverage_name
        self.extra = extra

    def __str__(self):
        return f"Hello {self.name}. Here is your order details.\nYou ordered at {self.time}\n" \
               f"Pizza name: {self.pizza_name}\nPizza sacuce(s): {self.sauce}\nYour beverage: {self.beverage_name}\n" \
               f"Your extra(s): {self.extra}\nYour Total cost is ${self.total_cost}"
