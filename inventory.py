#This programs stores and captures data for shoe products at a Nike warehouse

#========The beginning of the class==========
class Shoe:
    #construct method with different attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        pass

    #method which returns cost of the shoes
    def get_cost(self):
        pass
        print(self.cost)
        return self.cost
    #method which returns quantity of shoes
    def get_quantity(self):
        pass
        print(self.quantity)
        return self.quantity
    #method which returns a string presentation
    def __str__(self):
        pass
        return f'{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}'
    
        '''

#=============Shoe list===========
'''
#The list will be used to store a list of objects of shoes.
shoe_list = []

#==========Functions outside the class==============
#This function reads the inventory.txt file and creates a shoes object
def read_shoes_data():
    pass
    #open file
    file = open('inventory.txt','r')
    lines = file.readlines()
    #This skips the first line in the invertory text file
    products = lines[1:]
    #loop for creating shoe objects
    for x in range(len(products)):
        #this ensures the program does not crash due to index error
        while True:
            try:
                takkie = products[x].split(',')
                break
            except IndexError:
                print("\n")
                break    
        #shoe object is created and appended to soe_list 
        shoe = Shoe(takkie[0],takkie[1],takkie[2],takkie[3],takkie[4])
        shoe_list.append(shoe)
#======================================================================================

#function for capturing data for a shoe
def capture_shoes():
    pass
    #user inputs data for the shoe 
    country = input("Enter country: ").strip()
    code = input("Enter product code: ").strip()
    product  = input("Enter product name: ").strip()

    #while loop to ensure user enters the correct value
    while True:
        try:
            cost = float(input("Enter price of the product: "))
            break
        except ValueError:
            print("Invalid input")

    #while loop to ensure user enters the correct value
    while True:
        try:
            quantity = int(input("Enter quantity of the product: "))            
            break
        except ValueError:
            print("Invalid input")   

    #new shoe object is created and appended to the shoe_list
    captured = Shoe(country,code,product,cost,quantity)
    shoe_list.append(f'\n{captured}')

    #adds captured shoe to the inventory.txt file
    file = open('inventory.txt','a')
    file.write(f"\n{country},{code},{product},{str(cost)},{str(quantity)}")
#=============================================================================================

#function to view all shoe products
def view_all():
    pass
    #for loop to print each line in the inventory.txt file
    for x in shoe_list:
        print(str(x))
#==============================================================================================

#function to restock a shoe that is low on quantity
def re_stock():
    pass
    #variable to store low quantity values and compare them
    low_quantity = []

    #for loop to extract quantity values for each shoe
    for x in shoe_list:
        info = str(x).split(', ')
        low_quantity.append(int(info[4]))
    lowest = low_quantity.index(min(low_quantity))

    #returns shoe with the lowest quantity
    print(shoe_list[lowest])

    #user input to decide if they want  to restock or not
    choice = input("Would you like to add to the quantity?(yes/no): ").lower()
    
    #while loop  to ensure user enters one of the provided options
    while choice!= 'yes' and choice != 'no':
        print("Invalid")
        choice = input("Would you like to add to the quantity?(yes/no): ").lower()
    else:       
        #if statement to restock shoes 
        if choice == 'yes':

            #prompts user to enter the new quantity for the shoes
            while True:
                try:
                    new_quatity = int(input("Enter new product quantity: "))                    
                    break
                except ValueError:
                    print("Invalid input") 
            
            file = open('inventory.txt','r')
            lines = file.readlines()
            new_val = lines[lowest+1].split(',')
            new_val[4] = str(f'{new_quatity}\n') #replaces value in the value
            lines[lowest+1] =','.join(new_val)

            new_file = open('inventory.txt','w')
            #this writes the inventory.txt file with the updated quantity values
            for x in lines:
                new_file.write(x)

            #updates shoe_list
            shoe_list[lowest] = Shoe(new_val[0], new_val[1],new_val[2],new_val[3],new_val[4])
            print("Updated!")

        elif choice == 'no':
            print("Updated!")
#======================================================================================================

#function to search shoe by code 
def seach_shoe():
    #shoe_code  variable to store shoe_code names
    shoe_code = []

    #loop for extracting shoe codes
    for x in shoe_list:
        info = str(x).split(', ')
        shoe_code.append(info[1])

    #prompts user to search for show using code
    search = input("Search shoe using code: ")

    #executed if the shoe is not found and prompts the user to  search again
    while search not in shoe_code:
        print('Shoe not found! Search again')
        search = input("Search shoe using code: ")
    
    #prints details for the searched show
    pos = shoe_code.index(search)
    print(str(shoe_list[pos]))

    pass
#==========================================================================================================

#function that calculates the total value for each shoe product
def value_per_item():
    pass
    #imports data from the inventory.txt file
    file = open('inventory.txt','r')
    lines = file.readlines()

    #skips the first line in the the inventory.txt file 
    products = lines[1:]

    #loop for extracting the quantity and the price of the shoes
    for x in range(len(products)):
        while True:
            try:
                product = products[x].split(',')
                break
            except IndexError:
                print('')
                break

        #returns the total value for each shoe product
        value = float(product[3])*int(product[4])
        print(f'Product: {product[2]}         Total value: {value}')
#==========================================================================================================

#This function returns a shoe with the highest quantity and puts it up for sale
def highest_qty():
    pass
    file = open('inventory.txt','r')
    lines = file.readlines()
    high_quantity = []

    #skips the first line in the the inventory.txt file 
    products = lines[1:]
    #for loop to extract quantity values for each shoe
    for x in range(len(products)):
        while True:
            try:
                quantity = products[x].split(',')
                
                break
            except IndexError:
                print('')
                break
        high_quantity.append(int(quantity[4].strip()))

    #this returns the index  of the shoe with the highest quantity and puts it  up for sale
    position =  high_quantity.index(max(high_quantity))  
    name = products[position].split(',')
    print(f"The {name[1]} {name[2]} is available for sale")
    print("\n")
    

#==========Main Menu======================================

#function which reads data from the inventory text file and creates a shoe object
read_shoes_data()
print('\n')
print('Products imported')

while True:
    #prints menu for the user
    menu = input('''Select one of the following Options below:
c - to capture a shoe
va - View all shoes
rs - to restock shoes
s - search shoe
v - value for every shoe
h - to print producct with the highest quantity
e - Exit
: ''').lower()
            
    #This statement  allows the user to capture a new shoe
    if menu == 'c':
        #capture_shoes() function is called
        capture_shoes()
    
    #allows user to view all shoe products
    elif menu == 'va':
        #view_all() function is called
        print("\n")
        view_all()
        print("\n")

    #This allows the user to  restock a shoe product
    elif menu == 'rs':
        pass
        #re_stock() function is called
        re_stock()
    
    #this allows the user to search for a shoe
    elif menu == 's':
        pass
        #seach_shoe() function is called
        seach_shoe()

    #this returns the total value for each shoe product
    elif menu == 'v':
        pass
        #value_per_item() function is called
        value_per_item()

    elif menu == 'h':
        pass
        #highest_qty()  function is called
        highest_qty()  

    #Allows the user to exit the program
    elif menu == 'e':
        print('Goodbye!!!')
        #exit function is called
        exit()
    else:
        print("You have made a wrong choice, Please Try again")
