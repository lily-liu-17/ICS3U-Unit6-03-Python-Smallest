#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program finds the smallest of 10 random numbers

import random


def samallest_number(number_list):
    # This function finds the samllest of 10 random numbers

    smallest = number_list[1]

    for loop_counter in number_list:
        if loop_counter < smallest:
            smallest = loop_counter

    return smallest


def main():
    # This program finds the averae of 10 random numbers
    number_list = []

    print("Here is a list of random numbers : ")
    print("")

    for loop_counter in range(1, 11):
        random_number = random.randint(1, 100)
        number_list.append(random_number)
        print("The random number {0} is : {1}".format(loop_counter, random_number))

    smallest = samallest_number(number_list)

    print("")
    print("\nThe samllest number is {0}".format(smallest))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
