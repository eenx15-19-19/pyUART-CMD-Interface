import serial

import serialUART

from clint.textui import puts, indent, colored, prompt
from helpers import verticalLine


def recieve():
    verticalLine()
    puts(colored.magenta("Recieve command via UART"))
    puts(colored.cyan("Waiting to recieve..."))
    
    line = ser.readline() #read a '\n' terminated line
