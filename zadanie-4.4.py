import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calculate(choice, num1, num2):
    if choice == 1:
        print (f"Wynik to {num1 + num2}")
        return (num1 + num2)
    elif choice == 2:
        print (f"Wynik to {num1 - num2}")
        return (num1 - num2)
    elif choice == 3:
        print (f"Wynik to {num1 * num2}")
        return (num1 * num2)
    elif choice == 4:
        print (f"Wynik to {num1 / num2}")
        return (num1 / num2)
    else:
        exit(1)

if __name__ == "__main__":
    choice = int(input("Podaj zamierzone działanie matematyczne, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    num1 = int(input("podaj pierwszą liczbę:"))
    num2 = int(input("podaj kolejną liczbę:"))

    działania = ['Void', 'dodaję', 'odejmuję', 'mnożę', 'dzielę']

    logging.debug("zlecona czynność to: %s %s i %s" % (działania[choice], num1, num2))

    calculate(choice, num1, num2)