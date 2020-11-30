#!/usr/bin/env python3

# Created by Tong Gong
# Created time November 2020
# This is a  "Number Guessing Game" program.

import constants


def main():
    # This is the function to play the "Number Guessing Game" program.

    # Input
    userinput = int(input("Enter the number you guess:"))
    print("")

    # Process
    if userinput == constants.my_number:
        print("You guessed right")


if __name__ == "__main__":
    main()
