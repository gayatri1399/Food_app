from admin import *
from user import *
a=Admin()
b=User()
print('**********************************Welcome to Restruant****************************************')
while True:
    print("*"*100)
    print('Press 1 to login as Admin')
    print('Press 2 to login as User')
    print('Press 3 to Exit')
    choice=int(input('Enter you choice :'))
    if choice==1:
        print("*"*100)
        print('Press 1 to add new food items')
        print('Press 2 to load food item')
        print('Press 3 to remove food item')
        print('Press 4 to edit food item')
        print("*"*100)
        option=int(input('Enter you option you want to perform :'))
        print("*"*100)
        if option==1:
            print(a.add_new_food_items())
        elif option==2:
            print(a.load_food_item())
        elif option==3:
            print(a.remove_food_item())
        elif option==4:
            print(a.edit_food_item())
        else:
            print('Please enter valid input')
    elif choice==2:
        print("*"*100)
        print('Press 1 for registeration')
        print('Press 2 for load student details')
        print('Press 3 for log in')
        print("*"*100)
        option=int(input('Enter you option you want to perform :'))
        print("*"*100)
        if option==1:
            print(b.registeration())
        elif option==2:
            print(b.load_student_details())
        elif option==3:
            b.log_in()
        else:
            print('Please enter valid input')
    elif choice==3:
        print('Thanks for visiting! Visit again')
        sys.exit()
    else:
        print('Please enter valid input')