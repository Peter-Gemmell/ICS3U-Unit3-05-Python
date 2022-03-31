#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on March 2022
# this function turns # 1-12 to their respective numbers
def main():
    # this function turns # 1-12 to their respective numbers

    # input
    month_number = int(input("Enter a number of a month: "))
    print("")

    # process & output
    if month_number == 1:
        print("The month is January")
    elif month_number == 2:
        print("The month is February")
    elif month_number == 3:
        print("The month is March")
    elif month_number == 4:
        print("The month is April")
    elif month_number == 5:
        print("The month is May")
    elif month_number == 6:
        print("The month is June")
    elif month_number == 7:
        print("The month is July")
    elif month_number == 8:
        print("The month is August")
    elif month_number == 9:
        print("The month is September")
    elif month_number == 10:
        print("The month is October")
    elif month_number == 11:
        print("The month is November")
    elif month_number == 12:
        print("The month is December")
    else:
        print("{} Is an Invalid input. Not between 1-12.".format(month_number))

    print("\nDone.")


if __name__ == "__main__":
    main()
