class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise Exception("Name must be between 1 and 15 characters.")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        top_customer = None
        max_total = 0
        for customer in cls.all:
            total = sum(order.price for order in Order.all if order.customer == customer and order.coffee == coffee)
            if total > max_total:
                max_total = total
                top_customer = customer
        return top_customer


class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        if len(name) < 3:
            raise Exception("Name must be at least 3 characters long.")
        self._name = name

    @property
    def name(self):
        return self._name

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise Exception("Customer must be an instance of Customer.")
        if not isinstance(coffee, Coffee):
            raise Exception("Coffee must be an instance of Coffee.")
        if not isinstance(price, float):
            raise Exception("Price must be a float.")
        if not (1.0 <= price <= 10.0):
            raise Exception("Price must be between 1.0 and 10.0.")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee
