class Item:

    def __init__(self, id, name, price, count):
        self.id = id,
        self.name = name
        self.price = price
        self.count = count

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name, 
            'price': self.price,
            'count': self.count,
        }