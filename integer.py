#!/usr/bin/env python3

# Created by: Paterry Baptichon Junior
# Created on: 2022-04-05
# This is a program which tells you if you number is - or +.


def main():

    # user enters an input
    number = int(input("Enter a number: "))

    # Processes that if user number is equal to 0 than it prints " 0 is just zero"
    if number == 0:
        #  prints " 0 is just zero"
        print("")
        print("(0) is just zero")
    # Process
    elif number > 0:
        #  prints " this integer is positive"
        print("")
        print("this integer is positive")
    # Process
    elif number < 0:
        #  prints " this integer is negative"
        print("")
        print("this integer is negative")


if __name__ == "__main__":
    main()