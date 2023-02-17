import random
import json
import sys
class Admin:
    def __init__(self):
        self.food_item={}
        

    def add_new_food_items(self):
        self.name=input('Enter food name :')
        self.quantity=(input("Enter food quantity you want to buy :"))
        self.price=int(input('Enter food price :'))
        self.discount=int(input('Enter food discount :'))
        self.stock=int(input('Enter food stock in the restaurant :'))
        
        self.item={'Food name':self.name,'Food quantity':self.quantity,'Food price':self.price,'Food discount':self.discount,'Food stock':self.stock}
        
        food_id=random.randint(1,100)
        self.food_item[food_id]=self.item
        with open('Food_item.json','w') as f:
            json.dump(self.food_item,f,indent=4)
        return self.food_item
    
    def load_food_item(self):
        with open("Food_item.json","r") as f:
            self.food_item=json.load(f)
        return self.food_item

    def remove_food_item(self):
        with open("Food_item.json","r") as f:
            self.food_item=json.load(f)
        print(self.food_item)
        food_item_key=(input('Enter the key you want to delete :'))
        
        if food_item_key not in self.food_item:
            print('Invalid key')
            print('Please enter the correct key')
            return self.food_item
        else:
            del self.food_item[food_item_key]
            #print('Remaining food item is :')
            with open('Food_item.json','w') as f:
                json.dump(self.food_item,f,indent=4)
            return self.food_item

    def edit_food_item(self):
        with open("Food_item.json","r") as f:
            self.food_item=json.load(f)
        print(self.food_item)
        food_id=(input('Enter the id you want to update :'))
        
        if food_id not in self.food_item:
            print('Invalid key')
            print('Please enter the correct key')
        else:
            print(self.food_item[food_id])
            
            print("*"*100)
            print("Prees 1 to Update Food Name")
            print("Prees 2 to Update Quantity")
            print("Prees 3 to Update Price")
            print("Prees 4 to Update Discount")
            print("Prees 5 to Update Stock")
                #print('Press 6 to Exit')
            update_input = int(input("Enter Your Number Here :"))
            
            if update_input ==1:
                food_name = input("Enter Your New Food Name :")
                self.food_item[food_id]["Food name"] = food_name
                with open("Food_item.json","w") as f:
                    json.dump(self.food_item,f,indent=4)
                print('Your updated item is :')
                print(self.food_item[food_id])
                print("*"*100)
                return self.food_item

            elif update_input ==2:
                food_quantity = input("Enter Your New Quantity :")
                self.food_item[food_id]["Food quantity"] = food_quantity
                with open("Food_item.json","w") as f:
                    json.dump(self.food_item,f,indent=4)
                print('Your updated item is :')
                print(self.food_item[food_id])
                print("*"*100)
                return self.food_item
                
            elif update_input ==3:
                food_price = input("Enter Your New Price :")
                self.food_item[food_id]["Food price"] = food_price
                with open("Food_item.json","w") as f:
                    json.dump(self.food_item,f,indent=4)
                print('Your updated item is :')
                
                print(self.food_item[food_id])
                print("*"*100)
                return self.food_item
                
            elif update_input ==4:
                food_discount = input("Enter Your New Discount :")
                self.food_item[food_id]["Food discount"] = food_discount
                with open("Food_item.json","w") as f:
                    json.dump(self.food_item,f,indent=4)
                print('Your updated item is :')
                print(self.food_item[food_id])
                print("*"*100)
                return self.food_item

            elif update_input ==5:
                food_stock = input("Enter Your New stock :")
                self.food_item[food_id]["Food stock"] = food_stock
                with open("Food_item.json","w") as f:
                    json.dump(self.food_item,f,indent=4)
                print('Your updated item is :')
                print(self.food_item[food_id])
                print("*"*100)
                return self.food_item

            else:
                print('Thanks for Updating the information')
                #sys.exit()
                
                


        

#c=Admin()
#print(c.add_new_food_items())
#print(c.add_new_food_items())
#print(c.load_food_item())
#print(c.remove_food_item())
#print(c.edit_food_item())
