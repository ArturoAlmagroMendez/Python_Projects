client_list = []
def saveCustomer():

    new_client = input("What's the name of the customer? ")
    client_list.append(new_client)
    print("The client " + new_client + " is saved at the position " + str(client_list.index(new_client)))
    answer = input("Do you want to save more customers? (y/n) ")
    if answer == "y":
        saveCustomer()

    answer2 = input("Do you want to see all the customers? (y/n) ")
    if answer2 == "y":
        show_customers(client_list)
        print
    else:
        print("Okay,see you later =)")
    
  
def show_customers(client_list):
    for i in range(len(client_list)):
        print("Customer number " + str(i) + " : " + client_list[i])


def run():
    saveCustomer()
    


if __name__ == '__main__':
    run()
