# defining a function to read the file from the user.txt file
def read_the_file():
    with open("user.txt", "r") as readfile:
        laptopstock = {}  # laptopstock is our dictionary
        id_of_laptops = 1
        for i in readfile:
            i = i.replace("\n", "")  # replacing any new line character("\n") in the variable "i" and replace it with empty string("")
            laptopstock[id_of_laptops] = i.split(",")  # using the split() function to split the string to a list with ,(comma)
            id_of_laptops += 1
    return laptopstock

