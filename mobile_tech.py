from tech_product import Tech

class Mobile(Tech):
    def __init__(self,n,p,w,c,sc,cam):
        super().__init__(n,p,w,c)

        self.screen = sc
        self.camera = cam


    def __str__(self): 
        return f'Brand: {self.name}\nPrice: {self.price}\nWeight: {self.weght}\nColor: {self.color}\nScreen: {self.screen}\nCamera: {self.camera}\n'

    def apply_discount(self):
        self.price = int(self.price - self.price* (super().discount/2))
