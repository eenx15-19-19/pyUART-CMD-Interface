import serial

from serialUART import ser

from clint.textui import puts, indent, colored, prompt
from helpers import verticalLine

def send():
    verticalLine()
    puts(colored.magenta("Send command via UART"))
    puts("[e] Go back")

    command = str()

    while(command != "exit"):
        command = prompt.query("Write command you wish to send and press enter:\n")
        if(command != "exit"):
            puts(colored.cyan("Sending command: " + str(command)))
            ser.write(command)
