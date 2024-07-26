
# defining a function to print the bill in the terminal and write the bill in the new txt file after customer purchases
import datetime


def generate_invoice_for_customer(name_of_the_customer, address_info, contact_info1, contact_info2, info_of_laptop, total_price_of_the_laptops):
    current_date_and_time = datetime.datetime.now()  # storing the current date and time in the current_date_and_time variable
    with_shipping_charge = total_price_of_the_laptops + 100
    add_shipping_charge = True
    while True:
        print("\n")
        shipping_charge = (input("If you would like to ship the product to your house enter"
                                 " YES and if you don't want to ship your product enter NO:")).lower()
        if shipping_charge == "yes":
            with_shipping_charge =total_price_of_the_laptops + 100
            break
        elif shipping_charge == "no":
            add_shipping_charge = False
            break
        else:
            print("**The value deosnot seems valid***")
            continue
    # writing the bill in the new txt file named as billing.txt to give the bill to the user after every purchase
    with open("billing.txt", "w") as billing_file:  # storing the billing.txt file in the billing_file variable to wtite in it
        billing_file.write("\t\t\t\t----------------------------------------------------------"
                           "---------------------------------------")
        billing_file.write("\n")
        billing_file.write("\t\t\t\t---------------------------------------Bill invoice----------"
                           "------------------------------------")
        billing_file.write("\n")
        billing_file.write("\n")
        billing_file.write("\t\t\t\tDate and Time = " + str(current_date_and_time))
        billing_file.write("\n")
        billing_file.write("\t\t\t\t------------------------------------------------------------"
                           "-------------------------------------")
        billing_file.write("\n")
        billing_file.write("\t\t\t\tINVOICE TO:")

        billing_file.write("\t" + str(name_of_the_customer))
        billing_file.write("\n")
        billing_file.write("\t\t\t\t------------------------------------------------------------"
                           "-------------------------------------")
        billing_file.write("\n")
        billing_file.write("\t\t\t\tPhone Number: " + str(contact_info1))
        billing_file.write("\n")
        billing_file.write("\t\t\t\tEmail address:" + str(contact_info2))
        billing_file.write("\n")
        billing_file.write("\t\t\t\tAddress:" + str(address_info))
        billing_file.write("\n")
        billing_file.write("\t\t\t\t-------------------------------------------------------"
                           "------------------------------------------")
        billing_file.write("\n")
        for laptopdata2 in info_of_laptop:
            billing_file.write("\t\t\t\tName of the laptop = " + str(laptopdata2[0]))
            billing_file.write("\n")
            billing_file.write("\t\t\t\t-------------------------------------------------------"
                               "------------------------------------------")
            billing_file.write("\n")
            billing_file.write("\t\t\t\tQuantity selected by the user =" + str(laptopdata2[2]))
            billing_file.write("\n")
            billing_file.write("\t\t\t\t-------------------------------------------------------"
                               "------------------------------------------")
            billing_file.write("\n")
            billing_file.write("\t\t\t\tunit_price = " + str(laptopdata2[1]))
            billing_file.write("\n")
            billing_file.write("\t\t\t\t-------------------------------------------------------"
                               "------------------------------------------")
            billing_file.write("\n")
            billing_file.write("\n")
        billing_file.write("\t\t\t\t total price without shipping charge = " + str(total_price_of_the_laptops))
        billing_file.write("\n")
        # if the add_shipping_charge is declared True then the shipping charge is written in the file if not then the shipping charge is not written in the file
        if add_shipping_charge:
            billing_file.write("\t\t\t\ttotal_price with shipping charge = " + str(with_shipping_charge))
            billing_file.write("\n")

        billing_file.write("\n")
        billing_file.write("\t\t\t\t---------------------------------------Thank you for your cooperation--"
                           "------------------------")
        billing_file.write("\n")

        # printing the bill in the terminal

        print("\t\t\t\t---------------------------------------Bill invoice--------------------------------")
        print("\t\t\t\tDate and Time of the purchase = " + str(current_date_and_time))
        print("\t\t\t\t---------------------------------------------------------"
              "----------------------------------------")
        print("\t\t\t\tINVOICE TO:" + str(name_of_the_customer))
        print("\t\t\t\t---------------------------------------------------------"
              "----------------------------------------")
        print("\t\t\t\tPhone Number: " + str(contact_info1))
        print("\t\t\t\tEmail address:" + str(contact_info2))
        print("\t\t\t\tAddress:" + str(address_info))
        print("\t\t\t\t---------------------------------------------------------"
              "----------------------------------------")
        for laptopdata2  in info_of_laptop:
            print("\t\t\t\tName of the laptop = " + str(laptopdata2[0]))
            print("\t\t\t\t---------------------------------------------------------"
                  "----------------------------------------")
            print("\t\t\t\tQuantity_selected_user =" + str(laptopdata2[2]))

            print("\t\t\t\tunit_price = " + str(laptopdata2[1]))
            print("\t\t\t\t---------------------------------------------------------"
                  "----------------------------------------")
        print("\t\t\t\ttotal_price without shipping charge = " + str(total_price_of_the_laptops))
        if add_shipping_charge:
            print("\t\t\t\ttotal_price with shipping charge = " + str(with_shipping_charge))
            print("\t\t\t\t---------------------------------------------------------"
                  "----------------------------------------")
        print("\t\t\t\t---------------------------------------------------------"
              "----------------------------------------")




# defining a function to print the bill in the terminal and write the bill in the new txt file after buying from manufacturer
def generate_invoice_for_manufacturer(laptop_id, quantity,name1, contact_info2_1, contact_info1_1, address_info1,total_price_of_the_laptops,info_of_laptop):
    current_date_and_time = datetime.datetime.now()
    # calculating the vat

    with open("billing_file_for_man.txt", "w") as billing_file_for_man:  # opening a new text file named as billing_file_for_man to write the bill generated after ordering from manfacturer
        billing_file_for_man.write("\t\t\t\t----------------------------------------------------------"
                                   "---------------------------------------")
        billing_file_for_man.write("\n")
        billing_file_for_man.write("\t\t\t\t---------------------------------------Bill invoice----------"
                                   "------------------------------------")
        billing_file_for_man.write("\n")
        billing_file_for_man.write("\t\t\t\t------------------------------------------------------------"
                                   "-------------------------------------")
        billing_file_for_man.write("\n")
        billing_file_for_man.write("\t\t\t\tDate and Time = " + str(current_date_and_time))
        billing_file_for_man.write("\n")
        billing_file_for_man.write("\t\t\t\t------------------------------------------------------------"
                                   "-------------------------------------")
        billing_file_for_man.write("\n")
        billing_file_for_man.write("\t\t\t\tINVOICE TO(Company name):")

        billing_file_for_man.write("\t" + str(name1))
        billing_file_for_man.write("\n")
        billing_file_for_man.write("\t\t\t\t------------------------------------------------------------"
                                   "-------------------------------------")
        billing_file_for_man.write("\n")
        billing_file_for_man.write("\t\t\t\tPhone Number: " + str(contact_info1_1))
        billing_file_for_man.write("\n")
        billing_file_for_man.write("\t\t\t\tEmail address:" + str(contact_info2_1))
        billing_file_for_man.write("\n")
        billing_file_for_man.write("\t\t\t\tAddress:" + str(address_info1))
        billing_file_for_man.write("\n")
        billing_file_for_man.write("\t\t\t\t-------------------------------------------------------"
                                   "------------------------------------------")
        for laptopps in info_of_laptop:
            billing_file_for_man.write("\n")
            billing_file_for_man.write("\t\t\t\tname of the laptop = " + str(laptopps[0]))
            billing_file_for_man.write("\n")
            billing_file_for_man.write("\t\t\t\tquantity of the  laptop =" + str(laptopps[6]))
            billing_file_for_man.write("\n")
            billing_file_for_man.write("\t\t\t\tprocessor of the   laptop =" + str(laptopps[4]))
            billing_file_for_man.write("\n")
            billing_file_for_man.write("\t\t\t\tGraphics card of the laptop =" + str(laptopps[5]))
            billing_file_for_man.write("\n")
            billing_file_for_man.write("\t\t\t\t---------------------------------------------------------"
                                       "----------------------------------------")
            billing_file_for_man.write("\n")
            billing_file_for_man.write("\t\t\t\tunit_price = " + str(laptopps[2]))
            billing_file_for_man.write("\n")
            billing_file_for_man.write("\t\t\t\t------------------------------------------------------"
                                   "-------------------------------------------")
        billing_file_for_man.write("\n")
        total_price_without_vat = int(total_price_of_the_laptops) * int(quantity)
        vat = float((13 / 100) * 100)
        vat = 0.13

        total_price_without_vat = int(total_price_without_vat)
        total_price_with_vat= total_price_without_vat + (total_price_without_vat * vat)
        billing_file_for_man.write("\t\t\t\t------------------------------------------------------"
                                   "-------------------------------------------")
        billing_file_for_man.write("\n")
        billing_file_for_man.write("\t\t\t\tSub total(Without VAT) = " + str(total_price_without_vat))
        billing_file_for_man.write("\n")

        billing_file_for_man.write("\t\t\t\t------------------------------------------------------"
                                   "-------------------------------------------")
        billing_file_for_man.write("\n")
        billing_file_for_man.write("\t\t\t\tTotal amount (With VAT) = " + str(total_price_with_vat))
        billing_file_for_man.write("\n")
        billing_file_for_man.write("\t\t\t\t--------------------------------------------------"
                                   "------------------------------------------------")
        billing_file_for_man.write("\n")
        billing_file_for_man.write("\t\t\t\t---------------------------------------Thank you for your cooperation--"
                                   "------------------------")
        billing_file_for_man.write("\t\t\t\t--------------------------------------------------"
                                   "------------------------------------------------")
        # printing the bill in the terminal
        print("\t\t\t\t------------------------------------------------------------"
              "---------------------------------------")

        print("\t\t\t\t----------------------------------------------------------"
              "---------------------------------------")
        print("\t\t\t\t---------------------------------------Bill invoice----------"
              "------------------------------------")
        print("\t\t\t\t------------------------------------------------------------"
              "-------------------------------------")
        print("\t\t\t\tDate and Time = " + str(current_date_and_time))
        print("\t\t\t\t------------------------------------------------------------"
              "-------------------------------------")
        print("\t\t\t\tINVOICE TO(Company Name):", "\t" + str(name1))
        print("\t\t\t\t------------------------------------------------------------"
              "-------------------------------------")
        print("\t\t\t\tPhone Number: " + str(contact_info1_1))
        print("\t\t\t\tEmail address:" + str(contact_info2_1))
        print("\t\t\t\tAddress:" + str(address_info1))
        print("\t\t\t\t-------------------------------------------------------"
              "------------------------------------------")
        for laptopps in info_of_laptop:
            print("\t\t\t\tname_of_product = " + str(laptopps[0]))
            print("\t\t\t\tquantity_selected_user =" + str(laptopps[6]))
            print("\t\t\t\tprocessor of the laptop =" + str(laptopps[4]))
            print("\t\t\t\tgraphics card of the laptop =" + str(laptopps[5]))
            print("\t\t\t\t---------------------------------------------------------"
                  "----------------------------------------")
        print("\t\t\t\tunit_price = " + str(laptopps[2]))
        print("\t\t\t\t------------------------------------------------------"
              "-------------------------------------------")
        
        total_price_without_vat = int(total_price_of_the_laptops) * int(quantity)
        vat = (13 / 100) * 100
        vat = 0.13

        total_price_with_vat = total_price_without_vat + (total_price_of_the_laptops * vat)
        print("\t\t\t\t------------------------------------------------------"
              "-------------------------------------------")
        #total_price = int(str(laptopps[2].replace("$", "")) * int(str(laptopps[3])))
        print("\t\t\t\tSub total(Without VAT)= " + str(total_price_without_vat))
        print("\t\t\t\t------------------------------------------------------"
                                   "-------------------------------------------")
        print("\t\t\t\tTotal amount (With VAT) = " + str(total_price_with_vat))
        print("\t\t\t\t--------------------------------------------------"
              "------------------------------------------------")
        print("\t\t\t\t---------------------------------------Thank you for your cooperation--"
              "------------------------")
        print("\t\t\t\t------------------------------------------------------------"
              "---------------------------------------")

