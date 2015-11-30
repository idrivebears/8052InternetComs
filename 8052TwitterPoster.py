import time
import serial
from twitter import *

serConnection = serial.Serial(
    port='/dev/ttyUSB1',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)


config = {}
execfile("config.py", config)
twitter = Twitter(auth = OAuth(config["acces_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

def tweet_message(message):
    result = twitter.statuses.update(status = message)
    print("Status posted")

while(True):
    print("Application running...")
    print("Awaiting serial input...")
    
    message = ''

    while ser.inWaiting() > 0:
        message += ser.read(1)

    if message not '':
        tweet_message(message)
    time.sleep(1)
