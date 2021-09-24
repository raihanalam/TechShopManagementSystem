from tech_product import Tech
from laptop_tech import Laptop
from mobile_tech import Mobile
from sales_person import SalesPerson
from datetime import date


phone1  = Mobile('iphone 11',60000,500,'Black','1920-1080',10)
phone2  = Mobile('iphone 12',70000,550,'Silver','1920-1080',12)
phone3  = Mobile('One Plus Omega',50000,550,'Pink','1920-1080',120)

laptop1 = Laptop('HP-Pavilion-13',70000,1.5,'Mate',12, 'Core-i5', 100)
laptop2 = Laptop('Asus-Zeobook',75000,1.4,'Silver',16, 'Rayzen 4800', 100)
laptop3 = Laptop('Macbook Air-13',90000,1.5,'Golden',8, 'Core-i5', 100)

print(phone1)
print(laptop1)

phone1.apply_discount()

print(phone1.price)

print(laptop3.ship_cost(10))

print(Tech.get_total_products())

print(laptop3.price)

laptop3.set_double_price()
print(laptop3.price)

laptop3.change_specs(10,120)

print(laptop3.price)

saleperson1 = SalesPerson('Raihan','Alam',50000,date(2021,8,23))

saleperson1.sell_product(phone1)
saleperson1.sell_product(phone2)
saleperson1.sell_product(laptop1)
saleperson1.sell_product(laptop3)

print(saleperson1.total_product_sold())
saleperson1.display_sales()
print(saleperson1.calculate_sales())
print(saleperson1.calculate_commission(0.2))

saleperson1.sort_by_price()
saleperson1.display_sales()


