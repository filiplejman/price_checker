import time


class Item:

    def __init__(self, name, base_price, stock=0):
        self.name = name
        self.base_price = base_price
        self.discount = Discount()
        self.stock = stock
        self.discount_price = self.base_price
        self.used_discount = None

    def __count_discount(self, discount):
        if discount.discount_value:
            discount_price = self.base_price - discount.discount_value
        else:
            discount_price = (100 - discount.discount_value)*self.base_price
        return discount_price

    def pick_discount(self):
        self.discount.update_rules()
        best_price = self.base_price
        best_discount = None
        for discount in self.discount.rules:
            calculated_discounted_price = self.__count_discount(discount)
            if calculated_discounted_price < best_price:
                best_price = calculated_discounted_price
                best_discount = discount
        self.discount_price = best_price
        self.used_discount = best_discount

    def add_discount(self, discount):
        self.discount.add_rule(discount)


class Discount:

    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def __delete_rule(self, rule):
        self.rules.remove(rule)

    def update_rules(self):
        for rule in self.rules:
            if time.asctime() > rule.expiration_date:
                self.__delete_rule(rule)


class DiscountRules:

    def __init__(self, discount_value, discount_percentage, expiration_date, minimum_quantity, maximum_quantity):
        self.discount_value = discount_value
        self.discount_percentage = discount_percentage
        self.expiration_date = expiration_date
        self.minimum_quantity = minimum_quantity
        self.maximum_quantity = maximum_quantity