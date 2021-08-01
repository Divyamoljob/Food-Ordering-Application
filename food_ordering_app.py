class Database:
    foods = []
    food_id = 20000
    users = []
    history = []
    
    def __init__(self):
        foods = {}
        foods['food_id'] = Database.food_id+1
        Database.food_id+=1
        foods['food_title'] = 'Tandoori Chicken'
        foods['quantity'] = '120gm'
        foods['price'] = 1200
        foods['discount'] = 10
        foods['discounted_price'] = 1000
        Database.foods.append(foods)
    
        foods = {}
        foods['food_id'] = Database.food_id+1
        Database.food_id+=1
        foods['food_title'] = 'Vegan Burger'
        foods['quantity'] = '150gm'
        foods['price'] = 500
        foods['discount'] = 20
        foods['discounted_price'] = 400
        Database.foods.append(foods)
        
        foods = {}
        foods['food_id'] = Database.food_id+1
        Database.food_id+=1
        foods['food_title'] = 'Truffle Cake'
        foods['quantity'] = '120gm'
        foods['price'] = 1200
        foods['discount'] = 50
        foods['discounted_price'] = 600
        Database.foods.append(foods)

# **********************************************Users***************************************

class User(Database):
    def __init__(self):
        self.session = False
        self.email = ""
        
    def userReg(self):
        userdetails = {}
        name = input('Enter your full name :')
        phone_number = input("Enter your phone number :")
        email_id = input("Enter your email: ")
        address = input("Enter your address: ")
        password = input("Enter your password: ")
        
        userdetails['name'] = name
        userdetails['phone_number'] = phone_number
        userdetails['email_id'] = email_id
        userdetails['address'] = address
        userdetails['password'] = password
        Database.users.append(userdetails)
        print('Account created successfully')
        
    def user_login(self):
        users = Database.users
        username = input('Enter email : ')
        password = input('Enter password : ')
        if len(users)>0:
            for i in range(len(users)):
                if users[i]['email_id']==username and users[i]['password']==password:
                    self.session = True
                    self.email = username
                    print('You are successfully logged in')
                    break
                else:
                    pass
            else:
                print('Password or username is incorrrect')
                
    def view_foods(self):
        if self.session==True:
            d = Database()
            foods = Database.foods
            for i in range(len(foods)):
                print(foods[i]['food_id'], end = "\t")  
                print(foods[i]['food_title'], end = "\t")   
                print(foods[i]['quantity'], end = "\t") 
                print(foods[i]['price'], end = "\t") 
                print(foods[i]['discount'], end = "\t") 
                print(foods[i]['discounted_price'], end = "\t") 
                print("\n")
        else:
            print('Please Login')
        
    def view_history(self):
        history = Database.history
        email = self.email
        for i in range(len(history)):
            if history[i][0]==email:
                print(history[i][1], end = "\t")  
                print(history[i][2], end = "\t")   
                print(history[i][3], end = "\t") 
                print(history[i][4], end = "\t") 
                print(history[i][5], end = "\t") 
                print(history[i][6], end = "\t") 
                print("\n")
                
    def newOrder(self):
        if self.session == True:
            food = Database.foods
            
            choice = input('Enter food id : ').split(',')
            if len(choice)>1:
                for i in choice:
                    for foods in range(len(food)):
                        if food[foods]['food_id']==int(i):
                            listOfFood = []
                            listOfFood.append(self.email)
                            listOfFood.append(food[foods]['food_id'])
                            listOfFood.append(food[foods]['food_title'])
                            listOfFood.append(food[foods]['quantity'])
                            listOfFood.append(food[foods]['price'])
                            listOfFood.append(food[foods]['discount'])
                            listOfFood.append(food[foods]['discounted_price'])
                            Database.history.append(listOfFood)                            
                            print('Food order has been placed successfully for ', i)
                            break
                    else:
                        print('Food id not found')
            else:
                for foods in range(len(food)):
                    if food[foods]['food_id']==int(choice[0]):
                        print(choice[0])
                        listOfFood = []
                        listOfFood.append(self.email)
                        listOfFood.append(food[foods]['food_id'])
                        listOfFood.append(food[foods]['food_title'])
                        listOfFood.append(food[foods]['quantity'])
                        listOfFood.append(food[foods]['price'])
                        listOfFood.append(food[foods]['discount'])
                        listOfFood.append(food[foods]['discounted_price'])
                        Database.history.append(listOfFood)                            
                        print('Food order has been placed successfully for ', choice[0])
                        break
                else:
                    print('Invalid food ID')
        else:
            print('Please login to continue')
            
    def update_profile(self):
        users = Database.users
        print('Please select the field which you want to update')
        print('1. Name')
        print('2. Phone Number')
        print('3. Address')
        user_input = int(input('Enter your choice : '))
        if user_input==1:
            data = input('Enter your data : ')
            for i in range(len(users)):
                if users[i]['email_id']==self.email:
                    users[i]['name'] = data
                    print('Name has been updated successfully')
                    break
        elif user_input==2:
            data = input('Enter your data : ')
            for i in range(len(users)):
                if users[i]['email_id']==self.email:
                    users[i]['phone_number'] = data
                    print('Phone number has been updated successfully')
                    break
        elif user_input==3:
            data = input('Enter your data : ')
            for i in range(len(users)):
                if users[i]['email_id']==self.email:
                    users[i]['address'] = data
                    print('Address has been updated successfully')
                    break
        else:
            print('Invalid choice')
        
    def logout(self):
        self.session = False
        print('logged out successfully')

# ************************************************ADMIN*********************************************************

class Admins(Database):
    username = 'admin'
    password = 'admin'
    Session = False
    admin_users = [{'username': 'admin', 'password': 'admin'},]

    def add_foods(self):
        if Admins.Session==True:
            foods = {}
            food_title = input('Enter food name : ');
            quantity = input('Enter quantity : ')
            price = int(input('Enter price ; '))
            discount = int(input('Enter discount : '))
            discounted_price = int(input('Enter discounted price : '))

            foods['food_id'] = Database.food_id+1
            Database.food_id+=1

            foods['food_title'] = food_title
            foods['quantity'] = quantity
            foods['price'] = price
            foods['discount'] = discount
            foods['discounted_price'] = discounted_price
            Database.foods.append(foods)  
            print('New food item inserted successfully')
        else:
            print('Please login')

    def view_foods(self):
        if Admins.Session==True:
            foods = Database.foods
            for i in range(len(foods)):
                print(foods[i]['food_id'], end = "\t")  
                print(foods[i]['food_title'], end = "\t")   
                print(foods[i]['quantity'], end = "\t") 
                print(foods[i]['price'], end = "\t") 
                print(foods[i]['discount'], end = "\t") 
                print(foods[i]['discounted_price'], end = "\t") 
                print("\n")
        else:
            print('Please login')

    def edit_foods(self):
        if Admins.Session==True:
            food_id = int(input('Enter food id : '))
            foods = Database.foods
            for i in range(len(foods)):
                if foods[i]['food_id'] == food_id:
                    change = input('Enter the field (Food name, quantity, price, discount, discounted price): ')
                    data = input('Enter the data : ')
                    Database.foods[i][change]=data
                    print('Changed successfully')
                    break              
        else:
            print('Please login')
            

    def delete_foods(self):
        if Admins.Session==True:
            food_id = int(input('Enter food id : '))
            foods = Database.foods
            for i in range(len(foods)):
                if foods[i]['food_id'] == food_id:
                    del Database.foods[i]
                    print('Deleted successfully')
                    break              
        else:
            print('Please login')

    def admin_login(self):
        username = input('Enter username : ')
        password = input('Enter password : ')
        admins = Admins.admin_users
        for i in range(len(admins)):
            if admins[i]['username']==username and admins[i]['password']==password:
                print('You are logged in')
                Admins.Session = True
            else:
                print('Username or password is incorrect')

    def logout(self):
        Admins.Session = False
        print('Logged out successfully')
