import serial
import getch
serialport = serial.Serial ("/dev/ttyS0")
serialport.baudrate = 115200
while(True):
    x = getch.getch()

    if x=='w':
       command = '+200+20015+00'
    elif x=='a':
        command = '-200+20015+00'
    elif x=='s':
        command = '-200-20015+00'
    elif x=='d':
        command = '+200-20015+00'
    elif x=='b':
        command = '+000+00015+00'
    elif x=='h':
        command = '+125+07515+00'
    elif x=='g':
        command = '-090-11015+00'
    else:
        break
    # type your code here
    serialport.write(command.encode())