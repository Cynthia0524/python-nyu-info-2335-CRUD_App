import csv

#Read the original product list
products_path = "data/products.csv"
#products_path = "/Users/cynthia/Desktop/Github/Python-nyu-info-2335-CRUD_App/data/products.csv"
products = []
keys = ["id","name","aisle","department","price"]
with open(products_path, "r") as products_file:
    reader = csv.DictReader(products_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
    for row in reader:
        dic = dict.fromkeys(keys)
        for key in keys:
            dic[key] = row[key]
        products.append(dic)

#Define some useful functions
def look_up_id(id):
    match = [product for product in products if product["id"] == id]
    return match[0]

def operation_guide():
    print("\n")
    print("There are " + str(len(products)) + " products in the database. Please select an operation: ")
    print("\n")
    print("    operation | description")
    print("    --------- | ------------------")
    print("    'List'    | Display a list of product identifiers and names.")
    print("    'Show'    | Show information about a product.")
    print("    'Create'  | Add a new product.")
    print("    'Update'  | Edit an existing product.")
    print("    'Destroy' | Delete an existing product.")
    print("\n")

def after_operation():
    choice = input("\nDo you want to continue?\n'Yes' for guide\n'No' for exit\nOr directly input your operation\n")
    if choice == "Yes":
        operation_guide()
        operation = input(" ")
    elif choice in ["List","Show","Create","Update","Destroy"]: operation = choice
    elif choice == "No": operation = "Exit"
    else: operation = choice
    return operation

def greatest_id(products):
    ids = []
    for product in products:
        ids.append(int(product["id"]))
    return max(ids)

def valid_id(id):
    ids = []
    for product in products:
        ids.append(product["id"])
    while(id not in ids):
        id = input("Wrong identifier! Please try again: ")
    return id

#Welcome page
username = input("Please input your username: ")
print("\n" + "-------------------------------" + "\n" + "PRODUCTS APPLICATION" + "\n" + "-------------------------------")
print("Welcome @" + username + "!")
print("\n")
operation_guide()

#Input user's operation
operation = input(" ")

#Start the operation processes
while True:

    if operation == "List":
        print("THERE ARE " + str(len(products)) + " PRODUCTS:")
        for product in products:
            print("  + " + str(product))

        operation = after_operation()


    elif operation == "Show":
        show_id = input("OK. Please specify the product's identifier: ")
        show_id = valid_id(show_id)
        print("SHOWING A PRODUCT HERE!")
        print(str(look_up_id(show_id)))

        operation = after_operation()


    elif operation == "Create":
        print("OK. Please specify the product's information...")
        new_product = dict.fromkeys(keys)
        new_product["id"] = str(greatest_id(products)+1)
        for key in keys[1:]:
            new_product[key] = input("    "+key+": ")
        #if len(float(new_product["price"]))
        while(len(new_product["price"].split(".")[-1]) > 2):
        		new_product["price"] = input("Please input a price formatted as a number with two decimal places: ")
        print("CREATING A PRODUCT HERE!")
        print(new_product)
        print("\n")
        products.append(new_product)

        operation = after_operation()


    elif operation == "Update":
        update_product = dict.fromkeys(keys)
        update_product["id"] = input("OK. Please specify the product's identifier: ")
        update_product["id"] = valid_id(update_product["id"])
        print("OK. Please specify the product's information...")
        for key in keys[1:]:
            update_product[key] = input("    Change "+key+" from "+"'"+look_up_id(update_product["id"])[key]+"'"+" to: ")
        while(len(update_product["price"].split(".")[-1]) > 2):
        		update_product["price"] = input("Please input a price formatted as a number with two decimal places: ")
        print("UPDATING A PRODUCT HERE!")
        print(update_product)
        for product in products:
            if product["id"] == update_product["id"]:
                index = products.index(product)
                products[index] = update_product

        operation = after_operation()


    elif operation == "Destroy":
        destroy_id = input("OK. Please specify the product's identifier: ")
        destroy_id = valid_id(destroy_id)
        print("DESTROYING A PRODUCT HERE!")
        print(look_up_id(destroy_id))
        for product in products:
            if product["id"] == destroy_id:
                index = products.index(product)
                del products[index]

        operation = after_operation()


    elif operation in ["Exit","No"]:
    		save = input("Do you want to save the changes? Yes or No: ")
    		if save == "Yes":
        		with open(products_path, "w") as products_file:
        				writer = csv.DictWriter(products_file, fieldnames=keys)
        				writer.writeheader() # uses fieldnames set above
        				for i in products:
        						writer.writerow(i)
        				break
    		elif save == "No": break

    else:
        operation = input("Wrong input! Please try again: ")
        print("\n")
