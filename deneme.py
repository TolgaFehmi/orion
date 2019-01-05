#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import urllib
myAPI = "TDHYOIR9TC9BDUQK"
s=0
n=0
s_url=""
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=14)

while True:
    result = instance.read()
    if result.is_valid():
        s=result.temperature
        n=result.humidity
        s_url="https://api.thingspeak.com/update?api_key=TDHYOIR9TC9BDUQK&field1="+str(s)
        n_url="https://api.thingspeak.com/update?api_key=TDHYOIR9TC9BDUQK&field2="+str(n)
        print "Degerler gönderiliyor..."
        source = urllib.urlopen(s_url)
        print source.read()
        time.sleep(15)   
        source = urllib.urlopen(n_url)
        print source.read()
        print "Değerler gönderildi"
        time.sleep(45)
