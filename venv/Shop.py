class Shop:

    def __init__(self, name, link, address=None):
        self.name = name
        self.address = address
        self.link = link
        self.items = []
        self.shipping_info = ShippingDetails()

    def add_item(self, item):
        self.items.append(item)

    def delete_item(self, item):
        self.items.remove(item)


class ShippingDetails:

    def __init__(self):
        self.methods = None

    def add(self):
        pass


class ShippingMethod:
    pass