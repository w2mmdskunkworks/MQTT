import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")),
        " ",message.topic, message.qos, message.retain)
    # print ("message topic=",message.topic)

# mqttBroker ="mqtt.eclipseprojects.io"
mqttBroker ="192.168.11.80" 

client = mqtt.Client("Argon Pi")
client.connect(mqttBroker) 

client.loop_start()

client.subscribe("TEMPERATURE/#")
client.on_message=on_message 

time.sleep(120)
client.loop_stop()
