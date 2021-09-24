class Tech:

    total_products = 0
    discount = 0.5

    def __init__(self,n,p,w,c):
        self.name = n
        self.price = p
        self.weght = w
        self.color = c
        Tech.total_products +=1

    def apply_discount(self):
        self.price = int(self.price-(self.price*Tech.discount))
    
    def ship_cost(self,rate):
        return f'Shipping cost will be {self.weght*rate}'

    @classmethod
    def get_total_products(cls):
        return f'Total Products:' + str(cls.total_products)