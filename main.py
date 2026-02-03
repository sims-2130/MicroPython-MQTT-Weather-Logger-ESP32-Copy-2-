import time 
import network 
from machine import Pin 
import dht 
from umqtt.simple import MQTTClient
led = Pin(2, Pin.OUT) # ESP32 onboard LED 
# WiFi setup 
SSID = "Wokwi-GUEST" 
PASSWORD = "" 
wlan = network.WLAN(network.STA_IF) 
wlan.active(True) 
wlan.connect(SSID, PASSWORD) 
while not wlan.isconnected(): 
    time.sleep(0.5) 
print("Connected! IP:", wlan.ifconfig()[0])



# MQTT setup 
MQTT_BROKER = "broker.hivemq.com" 
CLIENT_ID = "esp32-wokwi-demo" 
TOPIC_TEMP = b"esp32/iot/0163temp"
TOPIC_STATUS = b"esp32/iot/0163status"
TOPIC_CMD = b"esp32/iot//0163cmd"
mqtt = MQTTClient(CLIENT_ID, MQTT_BROKER)
mqrr.set-callback 
mqtt.connect() 
# Sensor setup 
sensor = dht.DHT22(Pin(15)) 

# Callback for incoming messages 
def callback(TOPIC_CMD, msg): 
    print("Received:", TOPIC_CMD.decode(), "->", msg.decode()) 
if msg == b"ON": 
    led.value(1) 
elif msg == b"OFF": 
    led.value(0) 
mqtt.set_callback(callback) 
mqtt.subscribe(b"esp32/iot/<index_no>cmd") 
print("Ready to receive commands...") 



while True:
    sensor.measure() 
    temp = sensor.temperature() 
    hum = sensor.humidity() 
    payload = f"{{'temperature': {temp}, 'humidity': {hum}}}" 
    print("Publishing:", payload)
    mqtt.publish(TOPIC_TEMP, payload) 
    mqtt.publish(TOPIC_STATUS , b"Data sent successfully")
    print("Data sent successfully")
    mqtt.check_msg() 


    time.sleep(5)

