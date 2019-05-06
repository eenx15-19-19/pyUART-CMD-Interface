import serial

#configure raspberry pi port and parameters, timout = None means it will never timeout, it NEEDS an EOL (End Of Line Character \n) to return from readLine() function
ser = serial.Serial(
    port='/dev/ttyS0', #RPI - /dev/ttyS0
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS,
    timeout=None
)



