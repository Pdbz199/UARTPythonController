import serial
from pykeyboard import PyKeyboard
s = serial.Serial('COM7')

keyboard = PyKeyboard()

def press(key):
    keyboard.press_key(key)
    
def release(key):
    keyboard.release_key(key)

def parseCommand(cmd):
    splitCmd = cmd.split(' ')
    if "press" in splitCmd[0]:
        press(int(splitCmd[1]))
    else:
        for cmd in splitCmd[1:]:
            release(int(cmd))

while(True):
    command = str(s.readline())[2:-4]
    print(command)
    parseCommand(command)