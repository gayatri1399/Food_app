import random
import json
import sys
class User:
    def __init__(self):
        self.register={}
        self.order_history={}
        self.place_order_list=[]

    def registeration(self):
        self.name=input('Enter your name :')
        self.ph_no=int(input('Enter phone number :'))
        self.email=input('Enter email address :')
        self.address=input('Enter your address :')
        self.password=input('Enter your password :')
        self.register_details={'Name':self.name,'Ph number':self.ph_no,'Email':self.email,'Address':self.address,'Password':self.password}
        
        self.register_id=random.randint(1,1000)
        self.register[self.email]=self.register_details
        with open('registeration_details.json','w') as f:
            json.dump(self.register,f,indent=4)
        return self.register
    
    def load_student_details(self):
        with open("registeration_details.json","r") as f:
            self.register=json.load(f)
        return self.register
    
    def log_in(self):
        email_id=input('Enter the email address to login :')
        Password=input('Please enter your password :')
        with open("registeration_details.json","r") as f:
            self.register=json.load(f)
        if email_id not in self.register:
            print('You are new user. Please register')
        else:
            
            if self.register[email_id]['Password']==Password:
                print('Login successful! Welcome to resturant!')
                    #break
                
                print('Press 1 to Place new order')
                print('Press 2 for order History')
                print('Press 3 for Update Profile')
                #print('Press 4 to Exit')
                print("*"*100)

                option=int(input('Enter the option number you want to perform :'))
                if option==1:
                        
                    print('*'*100)
                    print('The menu card is :')
                    with open("Food_item.json","r") as f:
                        self.food_item=json.load(f)
                    for i in self.food_item:
                        food=('{} : {}, ({}),[INR :{}] '.format(str(i),self.food_item[str(i)]['Food name'],self.food_item[str(i)]['Food quantity'],self.food_item[str(i)]['Food price']))
                        print(food)
                    a=list((input('Enter the food id you need to buy :')).split())
                    for i in a:
                        if i in self.food_item:
                            place_order={str(i):self.food_item[i]}
                                
                            self.place_order_list.append(place_order)
                    key=random.randint(1,1000)
                    self.order_history[key]=self.place_order_list
                    with open('Order_history.json','w') as f:
                        json.dump(self.order_history,f,indent=4)
                        
                        #key=random.randint(1,1000)

                elif option==2:
                    print('Previous Order history is :')
                    with open('Order_history.json','r') as f:
                        self.order_history=json.load(f)
                    print(self.order_history)

                elif option==3:
                    
                        print('*'*100)
                        print('Press 1 to update name')
                        print('Press 2 to update Ph number')
                        print('Press 3 to update address')
                        print('Press 4 to update Password')
                        #print('Press 5 for exit')
                        option1=int(input('Enter the option you want to perform :'))
                        if option1==1:
                            Update_details= input("Enter Your New Name :")
                            self.register[email_id]['Name']=Update_details
                            with open("registeration_details.json","w") as f:
                                json.dump(self.register,f,indent=4)
                            print('Your updated profile is :')
                            print(self.register[email_id])

                        elif option1==2:
                            Update_details= input("Enter Your New Phone number :")
                            self.register[email_id]['Ph number']=Update_details
                            with open("registeration_details.json","w") as f:
                                json.dump(self.register,f,indent=4)
                            print('Your updated profile is :')
                            print(self.register[email_id])

                        elif option1==3:
                            Update_details= input("Enter Your New address :")
                            self.register[email_id]['Address']=Update_details
                            with open("registeration_details.json","w") as f:
                                json.dump(self.register,f,indent=4)
                            print('Your updated profile is :')
                            print(self.register[email_id])

                        elif option1==4:
                            Update_details= input("Enter Your New Password :")
                            self.register[email_id]['Password']=Update_details
                            with open("registeration_details.json","w") as f:
                                json.dump(self.register,f,indent=4)
                            print('Your updated profile is :')
                            print(self.register[email_id])
                            
                        #elif option1==5:
                         #   print('Thanks for updating information')
                          #  sys.exit()
                            
                        else:
                            print('Invalid input')

                #elif option==4:
                 #   print('Thanks for visiting! Visit again')
                 #   sys.exit()
                else:
                    print('Invalid input')
            else:
                print('You are a new user. Please register')
#d=User()
#d.log_in()
