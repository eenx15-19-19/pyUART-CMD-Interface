from __future__ import print_function
from clint.textui import puts, indent, colored, validators, prompt

import serialUART

# Import user created features
from send import send
from recieve import recieve
from helpers import verticalLine




def wrong_input():
    puts(colored.red("Wrong input, try again"))


main_menu = [{'selector':'s','prompt':'Send','return':'s'},
                {'selector':'r','prompt':'Recieve','return':'r'},
                {'selector':'exit','prompt':'Exit program','return':'exit'}]


def main():
    verticalLine()
    puts("Welcome to EENX15-1919 UART test interface!")
    while True:
        verticalLine()
        action = prompt.options(colored.magenta("What would you like to do?"), main_menu)
        if(action == "s"):
            send()
        elif(action == "r"):
            recieve()
        elif(action == "exit"):
            serial.close()
            exit()
        else:
            wrong_input

main()


