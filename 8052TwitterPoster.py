import time
import serial
from twitter import *
from twython import Twython

#https://twitter.com/8052MicroLopez
#marioalex

serConnection = serial.Serial(
    port='COM1',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

config = {}
execfile("config.py", config)
twitter = Twython(config['token'], config['token_key'], config['con_secret'], config['con_secret_key'])
time.sleep(5)
twitter.update_status(status='MOV TWITTER, HELLO_WORLD')
#twitter = Twitter(auth = OAuth(config['token'], config['token_key'], config['con_secret'], config['con_secret_key']))

#result = twitter.statuses.update(status = "Hello world?")

def tweet_message(message):
    #result = twitter.statuses.update(status = message)
    print("Status posted")
    time.sleep(3)

print("Application running...")
while(True):

    print("Awaiting serial input...")

    message = ""

    while serConnection.inWaiting() > 0:
        message += serConnection.read(1)
    print(message)
    #tweet_message(message)

    #if not message:
    #    tweet_message(message)
    time.sleep(1)
