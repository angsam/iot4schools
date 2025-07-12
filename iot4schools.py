import network
import utime
from umqtt.simple import MQTTClient

def connect_wifi(ssid, password):
    # Create a WLAN object in station (client) mode
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)  # Activate the Wi-Fi interface

    wlan.disconnect()  # Ensure previous connections are dropped
    utime.sleep(1)     # Short delay before trying to connect again

    wlan.connect(ssid, password)  # Attempt to connect to the given Wi-Fi network

    timeout = 10  # Maximum number of seconds to wait for connection
    for i in range(timeout):
        if wlan.isconnected():  # Check if connection was successful
            print("Connected to Wi-Fi:", wlan.ifconfig())  # Print network configuration
            return wlan  # Return the connected WLAN object
        print("Connecting to Wi-Fi...")  # Inform the user connection is in progress
        utime.sleep(1)  # Wait one second before retrying

    print("Wi-Fi connection failed!")  # Inform the user if connection fails after timeout
    return None  # Return None if connection was unsuccessful


def create_mqtt_client(username, key, client_id="RPI", server="io.adafruit.com", port=1883):
    return MQTTClient(client_id, server, port, username, key)

def connect_mqtt(client):
    client.connect()
    print("Connected to Adafruit IO!")
    
def check_wifi(wlan,ssid, password):
    # Check if the WLAN object exists and is still connected
    if not wlan or not wlan.isconnected():
        print("Wi-Fi disconnected. Reconnecting...")
        wlan = connect_wifi(ssid, password) # Attempt to reconnect
        if wlan:  
            connect_mqtt() # Reconnect to MQTT if Wi-Fi is back
    return wlan 
