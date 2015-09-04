#!/usr/bin/python

import paho.mqtt.client as mqtt
import socket

def on_connect(client, userdata, flags, rc):
    client.subscribe("$SYS/#")

client = mqtt.Client()
client.on_connect = on_connect

client.connect("mqtt-devqa.routers.syseng.us", 1883, 60)

client.publish("acme/randomdata", socket.gethostname())
