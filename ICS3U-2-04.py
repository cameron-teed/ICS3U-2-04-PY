#!usr/bin/env python

# Created by: Cameron Teed
# Created On: September 2019
# This program calculates the cost of a pizza by getting the diameter.

import constants_pizza


def main():
    # this function calculates the cost of pizza

    # input
    diameter = int(input("Enter the diameter of the pizza you would " +
                         "like (inch): "))

    # process
    sub_total = constants_pizza.LABOR + constants_pizza.RENT + \
        (diameter * constants_pizza.COST_PER_INCH)
    total = sub_total + (sub_total * constants_pizza.HST)

    # output
    print("")
    print("The cost for a {0} inch pizza is: ${1:,.2f}"
          .format(diameter, total))


if __name__ == "__main__":
    main()
