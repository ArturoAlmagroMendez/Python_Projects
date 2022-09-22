aliments = ("chicken", "tuna", "integral rice", "pasta", "quinoa",
            "oatmeal", "eggs", "cooked ham", "serrano ham", "omelette", "bacon")
proteins = (27, 29, 2.6, 5, 16.5, 14, 14.18, 21, 31, 11, 37)
msg = "How many grams? "


def calc_proteins(quantity, protein):

    result = (quantity/100) * protein
    return result

def print_main_menu():
    x = 1
    print(" ")
    print("╔══════════════════════════════════════════════════════════╗")
    for i in range(len(aliments)):
        phrase = ("║ " + str(x) + " ) " +
                  aliments[i] + " --- 100g contains " + str(proteins[i]) + " g of proteins")
        print(phrase.ljust(58, " ") + " ║")
        x += 1
    print("╚══════════════════════════════════════════════════════════╝")

    option = int(input(
        "Choose one and lets calculate the proteins!! (input option 1 - " + str(len(aliments)) + ") : "))

    if option in range(1, len(aliments)):
        quantity = int(input(msg))
        result = calc_proteins(quantity, int(proteins[int(option) - 1]))

        print(str(quantity) + " g of " + aliments[int(option) - 1] + " have " + str(result) + " g of proteins")


def run():
    print_main_menu()


if __name__ == '__main__':
    run()
