import datetime
# importing datetime to use in the bill invoice to print the current time of the bill printed
import reading_the_file
import operations
import updating_the_stock
from updating_the_stock import update_new_stock_after_buying
import generate_invoice

print("\n")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t****************************************************************")
print("\t \t \t \t \t \t\t \t\t Hello and Welcome  Everyone to THE CHAMBER OF HAPPINESS")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t****************************************************************")


def main_func():

    global valid_id, user_quantity, info_of_laptop, total_price_of_the_laptops
    let_loop_get_continue = True
    while let_loop_get_continue:
        print("\n")
        print("                   _____________________________________________________________________________________"
              "____________________________________________________________                 ")
        print("\t\t\t\t\tLets get started")
        print("                   _____________________________________________________________________________________"
              "____________________________________________________________                 ")
        print("\t\t\t\t\tNOTE: PLEASE READ")
        print("                   _____________________________________________________________________________________"
              "____________________________________________________________                 ")
        print("\t\t\t\t\tTO SELL LAPTOPS to the customer ")
        print("\t\t\t\t\tplease enter 'sell' or 'vend' ")
        print("                   _____________________________________________________________________________________"
              "____________________________________________________________                 ")
        print("\t\t\t\t\tTO BUY LAPTOPS FROM THE MANUFACTURER")
        print("\t\t\t\t\tplease enter 'buy' or 'purchase'")
        print("                   _____________________________________________________________________________________"
              "____________________________________________________________                 ")
        print("\t\t\t\t\tIf Done with everything")
        print("\t\t\t\t\tplease enter 'exit' or 'terminate'  to |exit| from the terminal")
        print("                   _____________________________________________________________________________________"
              "____________________________________________________________                 ")
        taking_input = (input("\t\t\t\t\tplease select any of the option below"
                              " according to the instructions:")).lower()
        print("                   _____________________________________________________________________________________"
              "____________________________________________________________                 ")
        if taking_input == "sell" or taking_input == "vend":
            laptopdata2 = reading_the_file.read_the_file()
            info_of_laptop, total_price_of_the_laptops,valid_id, user_quantity, name_of_the_customer,contact_info1, contact_info2, address_info,sell_multiple_laptops = operations.sell_to_customer(laptopdata2)
            #updating_the_stock.update_the_stock(valid_id, user_quantity,laptopdata2)
            print("\n")
            print("\t\t\t\t\t\t\t\t\tThe shipping charge is 100")
            print("-------------------------------------------------------------------------------------------------"
                  "---------------------------------------------")
            generate_invoice.generate_invoice_for_customer(name_of_the_customer, address_info, contact_info1, contact_info2, info_of_laptop, total_price_of_the_laptops)
            #generate_invoice.generate_invoice_for_customer(name, address_info, contact_info1, contact_info2, laptopdata2)
            #generate_invoice.generate_invoice_for_customer(name, address_info, contact_info1, contact_info2, laptopdata2, valid_id,
                                 # user_quantity)

            print("\n")
            print("--------------------------------------------------------")
            print("\t\t\t\t\t\tEnter yes to return to the front page")
            print("--------------------------------------------------------")
            print("\t\t\t\t\t\t Enter No to check out")
            print("--------------------------------------------------------")
            while True:
                again_order = (input("please enter:")).lower()
                if again_order == "yes":
                    main_func()

                elif again_order == "no":
                    print("\t\t\t\t\t\tThank you so much for choosing us")
                    print("\t\t\t\t\t\t\tKeep loving and supporting")
                    break
                else:
                    print("The input does not seems valid, please check ")
                    continue
                break
            let_loop_get_continue = False
        elif taking_input == "buy" or taking_input == "purchase":
            laptopdata3 = reading_the_file.read_the_file()
            quantity,laptop_id,name1, contact_info2_1, contact_info1_1, address_info1,total_price_of_the_laptops,info_of_laptop,quantity = operations.buy_from_manufacturer( laptopdata3)
            print("\n")
            print("\t\t\t\tThe bill is printed below")
            print("\n")
            generate_invoice.generate_invoice_for_manufacturer(quantity,laptop_id,name1, contact_info2_1, contact_info1_1, address_info1,total_price_of_the_laptops,info_of_laptop)

            #update_new_stock_after_buying(laptop_id, quantity,laptopdata3)
            """updating_the_stock.update_laptop_file_after_ordering(name_of_the_laptop, brand_of_the_laptop,
                                                                 price_of_the_laptop,
                                                                 quantity_of_the_laptop, processor_of_the_laptop,
                                                                 graphics_card_of_the_laptop)"""

            print("--------------------------------------------------------")
            print("\t\t\t\t\t\tEnter yes to return to the front page")
            print("--------------------------------------------------------")
            print("\t\t\t\t\t\t Enter No to check out")
            print("--------------------------------------------------------")
            while True:
                again_sell = (input("please enter:")).lower()
                if again_sell == "yes":
                    main_func()

                elif again_sell == "no":
                    print("\t\t\t\t\t\t______________________________________________")
                    print("\t\t\t\t\t\tThank you so much we all loved it")
                    print("\t\t\t\t\t\t______________________________________________")
                    break
                else:
                    print("\t\t\t\t\t\t______________________________________________")
                    print("The input does not seems valid, please check ")
                    print("\t\t\t\t\t\t______________________________________________")
                    continue
                break
            let_loop_get_continue = False
        elif taking_input == "exit" or taking_input == "terminate":
            print("\t\t\t\t\t\t______________________________________________")
            print("\t\t\t\t\t\tTHANK YOU FOR VISITING HOPE YOU VISIT AGAIN")
            print("\t\t\t\t\t\t______________________________________________")

            let_loop_get_continue = False
        else:
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t************************************************")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tplease check, the input does not seems correct")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*************************************************")


if __name__ == "__main__":
    main_func()
