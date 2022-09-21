customer_list = [] #On this list/Array we will save the customers


def saveCustomer():
    new_customer = input("What's the name of the customer? ") #Ask for the name of the customer
    customer_list.append(new_customer) #Add the customer to the list
    print("The customer " + new_customer + " is saved at the position " +
          str(customer_list.index(new_customer))) #Show message if the save was successful


def show_customers(customer_list): #Function that shows the list of customers in order they were created
    for i in range(customer_list): 
        print(customer_list[i])


def run():
    saveCustomer()
    answer = input("Do you want to save more customers? (y/n) ") 
    while answer == "y":
        saveCustomer()
    answer2 = input("Do you want to see all the customers? (y/n) ")
    if answer2 == "y":
        show_customers(customer_list)
    else:
        print("Okay,see you later =)")


if __name__ == '__main__':
    run()
