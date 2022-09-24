aliments = ("Chicken", "Tuna", "Integral rice", "Pasta", "Quinoa",
            "Oatmeal", "Eggs", "Cooked ham", "Serrano ham", "Omelette", "Bacon")
proteins = (27, 29, 2.6, 5, 16.5, 14, 14.18, 21, 31, 11, 37)
 

def calc_proteins(quantity, protein):

    result = (quantity/100) * protein
    return result


def print_main_menu():
    x = 1
   
    print("╔══════════════════════════════════════════════════════════╗")
    print("║ <---------------------MAIN MENU------------------------> ║ ")
    print("║                                                          ║ ")
    for i in range(len(aliments)):
        phrase = ("║ " + str(x) + " ) " + aliments[i] + " --- 100g contains " + str(proteins[i]) + " g of proteins")
        print(phrase.ljust(58, " ") + " ║")
        x += 1
    print("║                                                          ║ ")
    print("║ <------------------------------------------------------> ║")
    print("╚══════════════════════════════════════════════════════════╝")

    option = int(input("Choose one and lets calculate the proteins!! (input option 1 - " + str(len(aliments)) + ") : "))

    if option in range(1, len(aliments) + 1): #we have to sum 1 because the option 1 is the position 0 of the tuple
        quantity = (int(input("How many grams of " + aliments[int(option) - 1] + " ??? "))) 
        result = calc_proteins(quantity, int(proteins[int(option) - 1])) #we have to substract 1 because the option 1 is the position 0 of the tuple

        result = round(result,2)

        print(str(quantity) + " g of " + aliments[int(option) - 1] + " have " + str(result) + " g of proteins")


def run():
    #print(str(proteins[2]) + " " + str(proteins[4]))
    print_main_menu()


if __name__ == '__main__':
    run()
