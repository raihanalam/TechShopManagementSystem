class SalesPerson:
    employee_id = 0

    def __init__(self,fn,ln,sl,dt):
        self.first_name = fn
        self.last_name = ln
        SalesPerson.employee_id += 1
        self.salary = sl
        self.date_joined = dt
        self.products_sold = []
        self.total_sales = 0

    def sell_product(self,product):
        print(f'Selling {product.name}')
        self.products_sold.append(product)

    def display_sales(self):
        print('-------------------------------')
        for product in self.products_sold:
            print(product)
        print('-------------------------------')
    
    def calculate_sales(self):
        total = 0

        for product in self.products_sold:
            total += product.price

        self.total_sales = total
        
        return total

    def calculate_commission(self,percentage):
        total = self.calculate_sales()

        return f'Commission: {total*percentage}'
    
    def total_product_sold(self):
        return f'The number of products sold: {len(self.products_sold)}'

    def sort_by_price(self):
        self.products_sold.sort(key= lambda product: product.price, reverse=True)
