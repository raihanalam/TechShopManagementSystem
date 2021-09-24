from tech_product import Tech

class Laptop(Tech):
    def __init__(self,n,p,w,c,ram,cpu,storage):
        super().__init__(n,p,w,c)
        self.ram = ram
        self.cpu = cpu
        self.storage = storage

    def __str__(self): 
        return f'Brand: {self.name}\nPrice: {self.price}\nWeight: {self.weght}\nColor: {self.color}\nRam: {self.ram}\nCPU: {self.cpu}\nStorage: {self.storage}\n'

    def set_double_price(self):
        self.price = 2*self.price

    def change_specs(self,ram,storage):
        if ram > self.ram or storage > self.storage:
            self.price += 10000
        
        self.ram = ram
        self.storage = storage
