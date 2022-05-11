import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

# mqttBroker ="mqtt.eclipseprojects.io" 
mqttBroker ="192.168.11.80" 


client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker) 

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE/inside", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE/inside")
    time.sleep(1)

