import reading_the_file
import generate_invoice
import updating_the_stock


def sell_to_customer(laptopdata2):
    global sell_multiple, valid_id, user_quantity, contact_info1, name, contact_info2, address_info, sell_multiple_laptops, name_of_the_customer
    print("\n")
    print("\t\t\t\t\t\t\t___________________________________________________________")
    print("\t\t\t\t\t\t\tLETS GET STARTED WITH ALL THE LAPTOPS FOR YOU TO LOOK AT")
    print("\t\t\t\t\t\t\t___________________________________________________________")
    print("\t\t\t\t\t\t\t___________________________________________________________")

    print("\t\t\t\t\t\t\t\tBelow are all the Laptops available in the stock")
    print("\t\t\t\t\t\t\t___________________________________________________________")
    print("\n")
    print("_______________________________________________________________________________"
          "_______________________________________")
    print("\n")

    let_loop_to_continue = True
    total_price_of_the_laptops = 0  # initialize total price to 0
    info_of_laptop = []  # initialize empty list to store laptop information
    while let_loop_to_continue:
        # display laptop stock
        print(
            "S.N     Name                           Brand                     Price                 Quantity "
            "                    processor                  Graphics card")
        print("_________________________________________________________________________________"
              "________________________________________________________________________________________________")
        with open("user.txt", "r") as secondfile:
            s = 1
            for i in secondfile:
                print(s, "\t" + i.replace(",", "\t \t"))
                print("_______________________________________________________________________________"
                      "__________________________________________________________________________________-")
                s += 1
            print("\n")
        # get laptop id and quantity from user
        while True:
            try:
                valid_id = int(input("Enter id of the laptop: "))
                print("--------------------------------------------------------")
                break
            except ValueError:
                print("--------------------------------------------------------")
                print("**The input doesnot seems valid **")
                print("--------------------------------------------------------")
        print("\n")
        laptopdata = reading_the_file.read_the_file()
        while valid_id <= 0 or valid_id > len(laptopdata):
            print("--------------------------------------------------------")
            print("***please provide with valid laptop id***")
            print("--------------------------------------------------------")
            print("\n")
            print("--------------------------------------------------------")
            valid_id = int(input("enter id of the laptop you want to purchase"))
            print("--------------------------------------------------------")
        print("**********************|These are the laptop details you have selected|*****************")
        print("\n")
        print("------------------------------------------------------------------------", "|")
        print(f"    \tName of the laptop:                 {laptopdata[valid_id][0]}")
        print("------------------------------------------------------------------------", "|")
        print(f"\n     \tBrand of the laptop:               {laptopdata[valid_id][1]}")
        print("------------------------------------------------------------------------", "|")
        print(f"\n     \tPrice of the laptop:                {laptopdata[valid_id][2]}")
        print("------------------------------------------------------------------------", "|")
        print(f"\n     \tQuantity of the laptop:              {laptopdata[valid_id][3]}")
        print("------------------------------------------------------------------------", "|")
        print(f"\n     \tProcessor of the laptop:          {laptopdata[valid_id][4]}")
        print("------------------------------------------------------------------------", "|")
        print(f"\n    \tGraphics card of the laptop :      {laptopdata[valid_id][5]}")
        print("------------------------------------------------------------------------", "|")
        print("\n")
        while True:
            try:
                print("--------------------------------------------------------")
                user_quantity = int(input("enter number of quantity of the laptop:"))
                break
            except ValueError:
                print("--------------------------------------------------------")
                print("invalid input, please check")
        while user_quantity < 0 or user_quantity > int(laptopdata[valid_id][3]):
            print("--------------------------------------------------------")
            print("*****Dear user the quantity is not available in the stock****")
            user_quantity = int(input("Enter number of quantity of the laptop:"))
        updating_the_stock.update_the_stock(valid_id, user_quantity, laptopdata2)
        # calculate total price and add laptop information to list
        total_price_of_the_laptops += int(laptopdata[valid_id][2].replace("$", "")) * int(user_quantity)
        info_of_laptop.append((laptopdata[valid_id][0], laptopdata[valid_id][2], user_quantity))
        sell_multiple_laptops = (input("enter yes to purchase multiple laptop enter no to print the bill:")).lower()
        if sell_multiple_laptops == "yes":
            continue
        elif sell_multiple_laptops == "no":
            let_loop_to_continue = False
            print("***Dear user valid does not seems valid***")
            print("******************************************************************************")
            print("\t\t\t\t\tFOR BILLING PURPOSE WE WOULD LIKE TO ENTER YOUR DETAILS ")
            print("*******************************************************************************")
            name_of_the_customer = input("\t\t\t\t\t\t\tEnter your Name: ")
            print("----------------------------------------------------------------------")
            # try except to catch ValueError exception
            while True:
                try:
                    contact_info1 = int(input("\t\t\t\t\t\t\tEnter your Phone number: "))
                    break
                except ValueError:
                    print("----------------------------------------------------------------------")
                    print("\t\t\t\t\t\t\t***enter a valid Phone number***")
                    print("----------------------------------------------------------------------")
            print("----------------------------------------------------------------------")
            while True:
                contact_info2 = input("\t\t\t\t\t\t\tEnter your email: ")
                if "@" not in contact_info2:
                    print("\t\t\t\t\t\t\t***********Email does not seems valid**********")
                else:
                    break
            print("----------------------------------------------------------------------")
            address_info = input("\t\t\t\t\t\t\tEnter your Address: ")
            print("----------------------------------------------------------------------")
        else:
            print("\t\t\t\t***** Dear user the input value is invalid****")
    return info_of_laptop, total_price_of_the_laptops,valid_id, user_quantity, name_of_the_customer, contact_info1, contact_info2, address_info,sell_multiple_laptops


# defining the function to buy from manufacture and provide necessary details to the seller
def buy_from_manufacturer( laptopdata3):
    global user_quantity, valid_id, name1, contact_info2_1, contact_info1_1, address_info1
    print("**********************************************************************")
    print("lets get started to order  any kind of new laptops")
    print("**********************************************************************")
    print("\n")
    print("**********************************************************************")
    print("lets get started to order laptops")
    print("**********************************************************************")
    print("\n")
    print("**********************************************************************")
    print("Below are all the Laptops available in the stock")
    print("**********************************************************************")

    let_loop_to_continue = True
    total_price_of_the_laptops = 0  # initialize total price to 0
    info_of_laptop = []  # initialize empty list to store laptop information
    while let_loop_to_continue:
        print(
            "S.N          Name                       Brand               Price                   Quantity "
            "                           processor              Graphics card")
        print("_________________________________________________________________________________"
              "____________________________________________________________________________________________________")
        # opening the user.txt file in the read mode for the customer to display our laptop stock for them to purchase
        with open("user.txt", "r") as secondfile:
            s = 1
            for i in secondfile:
                print(s, "\t" + i.replace(",", "\t \t"))
                print("_______________________________________________________________________________"
                      "_____________________________________________________________________________________________")
                s += 1
            print("\n")
        while True:
            try:
                laptop_id = int(input("Enter id of the laptop to order: "))
                print("--------------------------------------------------------")
                break
            except ValueError:
                print("--------------------------------------------------------")
                print("**Enter valid input**")
                print("--------------------------------------------------------")
        print("\n")

        laptopdata = reading_the_file.read_the_file()  # putting the read_the_file() function in laptopdata variable
        # generating a message if the id of the laptop is not in stock
        while laptop_id <= 0 or laptop_id > len(laptopdata):
            print("--------------------------------------------------------")
            print("please provide with valid laptop id")
            print("--------------------------------------------------------")
            print("\n")
            print("--------------------------------------------------------")
            valid_id = int(input("enter id of the laptop you want to order"))
            print("--------------------------------------------------------")
        print("**********************|These are the laptop details you have selected|*****************")
        print("\n")
        print("------------------------------------------------------------------------", "|")
        print(f"    \tName of the laptop:                 {laptopdata[laptop_id][0]}")  # printing the 0 index of laptopdata
        # of the user enter id of the laptop which is stored in valid_id variable
        print("------------------------------------------------------------------------", "|")
        print(f"\n     \tBrand of the laptop:               {laptopdata[laptop_id][1]}")  # printing the 1 index of
        # laptopdata of the user enter id of the laptop which is stored in valid_id variable
        print("------------------------------------------------------------------------", "|")
        print(f"\n     \tPrice of the laptop:                {laptopdata[laptop_id][2]}")  # printing the 2 index of
        # laptopdata of the user enter id of the laptop which is stored in valid_id variable
        print("------------------------------------------------------------------------", "|")
        print(f"\n     \tQuantity of the laptop:              {laptopdata[laptop_id][3]}")  # printing the 3 index of
        # laptopdata of the user enter id of the laptop which is stored in valid_id variable
        print("------------------------------------------------------------------------", "|")
        print(f"\n     \tProcessor of the laptop:          {laptopdata[laptop_id][4]}")  # printing the 4 index of laptopdata
        # of the user enter id of the laptop which is stored in valid_id variable
        print("------------------------------------------------------------------------", "|")
        print(f"\n    \tGraphics card of the laptop :      {laptopdata[laptop_id][5]}")  # printing the 5 index of laptopdata
        # of the user enter id of the laptop which is stored in valid_id variable
        print("------------------------------------------------------------------------", "|")
        print("\n")
        # try except to catch ValueError exception
        while True:
            try:
                print("--------------------------------------------------------")
                quantity = int(input("enter number of quantity of the laptop to order:"))
                print("--------------------------------------------------------")
                break
            except ValueError:
                print("--------------------------------------------------------")
                print("invalid input, please check")
                print("--------------------------------------------------------")

        # generating a message if the quantity of the laptop is not in stock
        while quantity < 0 or quantity > int(laptopdata[laptop_id][3]):
            print("--------------------------------------------------------")
            print("*****Dear user the quantity is not available in the stock*****")
            print("--------------------------------------------------------")
            print("\n")
            print("--------------------------------------------------------")
            quantity = int(input("enter number of quantity of the laptop:"))
            print("--------------------------------------------------------")
        print("\n")
        updating_the_stock.update_new_stock_after_buying(laptop_id, quantity, laptopdata3)
        # calculate total price and add laptop information to list
        total_price_of_the_laptops += int(laptopdata[laptop_id][2].replace("$", "")) * int(quantity)
        info_of_laptop.append((laptopdata[laptop_id][0],laptopdata[laptop_id][1], laptopdata[laptop_id][2],laptopdata[laptop_id][3],laptopdata[laptop_id][4],laptopdata[laptop_id][5], quantity))
        print("**********************************************************************")

        purchase_multiple_laptops = (input("enter yes to purchase multiple laptop enter no to print the bill:")).lower()
        if purchase_multiple_laptops == "yes":
            continue
        elif purchase_multiple_laptops == "no":
            let_loop_to_continue = False
            print("\t\t\t\t\t\t\tFor billing propose, we would like you to enter your personal details")
            print("\t\t\t\t\t\t\t**************************************************************************")
            name1 = input("Enter the Name of the company: ")
            print("----------------------------------------------------------------------")
            # using try except to catch if ValueError exception occurs
            while True:
                try:
                    contact_info1_1 = int(input("Enter your Phone number: "))
                    print("----------------------------------------------------------------------")
                    break
                except ValueError:
                    print("enter a valid phone number")
                    print("----------------------------------------------------------------------")
            while True:
                contact_info2_1 = input("Enter your email: ")
                if "@" not in contact_info2_1:
                    print("email does not seems valid")
                else:
                    break
            print("----------------------------------------------------------------------")
            address_info1 = input("Enter your Address: ")
            print("----------------------------------------------------------------------")
        else:
            print("**Invalid Input****")
        return quantity,laptop_id,name1, contact_info2_1, contact_info1_1, address_info1,total_price_of_the_laptops,info_of_laptop,quantity

