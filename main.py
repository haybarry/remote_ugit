import machine
import network
# import ugit

import gc
print("RAM used = {RAM_used}kb".format(RAM_used = gc.mem_alloc()/1024))
print("RAM free = {RAM_free}kb".format(RAM_free = gc.mem_free()/1024))
print("RAM total = {RAM_total}kb".format(RAM_total = (gc.mem_alloc() + gc.mem_free())/1024))

# import mqtt_as import MQTTClient, config

gc.collect()

red = machine.Pin(25, machine.Pin.OUT)
yellow = machine.Pin(26, machine.Pin.OUT)
green = machine.Pin(27, machine.Pin.OUT)
button = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)
ota = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)


#Network and MQTT Parameters
# TOPIC           = 'test/mqtt_async'
# RXTOPIC         = 'test/mqtt_async'
# MOVTOPIC        = 'test/movement'
# config['server']   = '192.168.1.180'  #'192.168.0.14' # can also be a hostname
# config['ssid']     = 'WiFi-DE48'
# config['wifi_pw']  = '85725843'
# config.user     = 'haybarry'
# config.password = '221d33a55b32bb74bd18a5ead330901f40d3a2ba'

while True:
    green.value(button.value())