#all imports
from datetime import datetime
import json
from collections import namedtuple

#logging decorator
def log_action(func):
    def wrapper(*args):
        result= func(*args)
        print(f"{func.__name__} called at {datetime.now()}")
        return result
    return wrapper
#warehouse class
class Warehouse:
    #class variables
    warehouse_location="Jaipur"
    total_items_count=0
    #list of objects
    all_instances=[]
    def __init__(self,name,price,category):
        self.item_name=name
        self.price=price
        self.category=category
        self.__class__.all_instances.append(self)
        self.__class__.total_items_count+=1
    @property
    def email(self):
        return f"{self.item_name}{self.warehouse_location}@store.com"
    @log_action
    def apply_discount_percent(self,discount):
        return self.price-(discount*self.price)/100
    #dunder methods
    def __str__(self):
        return f"""
Item : {self.item_name}
Price:{self.price}
Category:{self.category}
"""
    def __add__(self,other):
        return self.price+other.price
    def __len__(self):
        return len(self.item_name)
    def get_maintenance_plan(self):
        print("General checkup")
    #class method
    @classmethod
    def update_location(cls,location):
        cls.warehouse_location=location
    #static method
    @staticmethod
    def is_valid_price(price):
        if price>0:
            return "valid price"
        else:
            return "invalid price"
#child class inheriting warehouse class
class Electronics(Warehouse):
    def __init__(self,name,price,category,time):
        super().__init__(name,price,category)
        self.Warranty_period=time
    #overriding method 
    def get_maintenance_plan(self):
        print("Monthly checkup")
#generting report of the manager and the available inventory
def generate_report():
    Manager=namedtuple("Manager",["id","name","dept"])
    m1=Manager(1,"Divya","computers")

    data=[obj.__dict__ for obj in Warehouse.all_instances]
    warehouse_report={"manger":m1._asdict(),"item_data":data}\
    
    with open("warehouse_final_data.json","w") as file:
        json.dump(warehouse_report,file,indent=4)

def main():
    #has code for testing of various functions 
    a=Warehouse("Laptop",40000,"Electronics")
    # print(a.email)
    # print(a)
    b=Warehouse("Tablet",20000,"Smart Gadgets")
    # print(a+b)
    # print(len(a))
    # a.update_location("Delhi")
    # print(a.apply_discount_percent(10))
    # print(a.warehouse_location)
    # n=Electronics("Television",90000,Electronics,"four months")
    # n.get_maintenance_plan()
    print(Warehouse.is_valid_price(0))
    generate_report()

if __name__=="__main__":
    main()