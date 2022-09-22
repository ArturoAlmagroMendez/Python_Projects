aliments = ("chicken","tuna","integral rice","pasta","quinoa","oatmeal","eggs","cooked ham","serrano ham","omelette","bacon")
proteins = (27,29,2.6,5,16.5,14,14.18,21,31,11,37)

def calc_proteins():
    quantity = int(input("How many grams ?"))


def print_main_menu():
    x = 1
    print(" ")
    print("╔══════════════════════════════════════════════════════════╗")
    for i in range(len(aliments)):
        phrase = ("║ "+ str(x) + " ) " + aliments[i] + " --- 100g contains " + str(proteins[i]) + " g of proteins")
        print(phrase.ljust(58," ") + " ║")
        x += 1
    print("╚══════════════════════════════════════════════════════════╝")    
def run():
    pass


if __name__ == '__main__':
    print_main_menu()