#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: October 2019
# This program finds the squares of integers


def main():
    # this function finds the squares of integers
    loop_counter = 0
    sqaures = 0

    print("Find the squares!")

    # input
    user_input_string = input("Enter an integer: ")
    print("")

    # process & output
    try:
        user_input = int(user_input_string)
        if user_input < 0:
            for loop_counter in range(0, user_input - 1, -1):
                sqaures = loop_counter ** 2
                print("{0}² = {1}".format(loop_counter, sqaures))
        else:
            for loop_counter in range(user_input + 1):
                sqaures = loop_counter ** 2
                print("{0}² = {1}".format(loop_counter, sqaures))

    except Exception:
        print("Wrong input. Try again.")


if __name__ == "__main__":
    main()
