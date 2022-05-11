import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

# mqttBroker ="mqtt.eclipseprojects.io" 
mqttBroker ="192.168.11.80" 

client = mqtt.Client("Temperature_Outside")
client.connect(mqttBroker) 

while True:
    randNumber = uniform(0, 10)
    client.publish("TEMPERATURE/outside", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE/outside")
    time.sleep(1)

