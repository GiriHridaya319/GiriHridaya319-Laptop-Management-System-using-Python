import reading_the_file
import operations
from operations import *


def update_the_stock(valid_id, user_quantity,laptopdata2):
    #laptopdata2 = reading_the_file.read_the_file()  # putting the read_the_file() function in laptopdata2 variable
    laptopdata2[valid_id][3] = int(laptopdata2[valid_id][3]) - int(user_quantity)
    with open("user.txt", "w") as writing:  # update the stock after user purchase any laptop
        # the stock and write it in a New txt file i.e. new.txt
        for value in laptopdata2.values():
            writing.write(str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) + ","
                          + str(value[4]) + "," + str(value[5]))  # writing in new txt file and 'writing' is the
            # variable where the new.txt file is stored
            writing.write("\n")
    return laptopdata2


# defining a function to update the txt file by appending the info of the new laptop purchased from manufacturer
"""def update_laptop_file_after_ordering(name_of_the_laptop, brand_of_the_laptop,price_of_the_laptop,
                                      quantity_of_the_laptop,processor_of_the_laptop, graphics_card_of_the_laptop):

    appending_new_laptop_details = f" {name_of_the_laptop},           {brand_of_the_laptop},      {price_of_the_laptop}, " \
                                   f"           {quantity_of_the_laptop},       {processor_of_the_laptop}, \
            {graphics_card_of_the_laptop}\n"
    with open("user.txt", "a") as file:
        file.write(appending_new_laptop_details)"""


def update_new_stock_after_buying(laptop_id, quantity,laptopdata3):
    laptopdata3 = reading_the_file.read_the_file()
    laptopdata3[laptop_id][3] = int(laptopdata3[laptop_id][3]) + int(quantity)
    with open("user.txt", "w") as writingAgain:
        for value in laptopdata3.values():
            writingAgain.write(str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) + ","
                               + str(value[4]) + "," + str(value[5]))
            writingAgain.write("\n")
    print("*************************************************************************")
    print("\t\t\t\t\tUpdated In the stock")
    print("*************************************************************************")
