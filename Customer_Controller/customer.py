customer_list = []  # On this list/Array we will save the customers


def saveCustomer():
    # Ask for the name of the customer
    new_customer = input("What's the name of the customer? ").capitalize()
    customer_list.append(new_customer)  # Add the customer to the list
    print("The customer " + new_customer + " is saved at the position " +
          str(customer_list.index(new_customer)))  # Show message if the save was successful
    answer = input("Do you want to save more customers? (y/n) ")
    if answer == "y":
        saveCustomer()


# Function that shows the list of customers in order they were created
def show_customers(customer_list):
    for i in range(len(customer_list)):
        print("The customer number " + str(i) + " is : " + customer_list[i])


def run():
    saveCustomer()
    answer2 = input("Do you want to see all the customers? (y/n) ")
    if answer2 == "y":
        show_customers(customer_list)
    else:
        print("Okay,see you later =)")


if __name__ == '__main__':
    run()
