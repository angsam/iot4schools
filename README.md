# iot4schools.py

MicroPython helper library for connecting Raspberry Pi Pico W to Wi-Fi and Adafruit IO using MQTT.  
Developed as part of the **IoT4Schools** project to simplify cloud communication in MicroPython-based IoT applications for educational use.

## ✨ Features

- Connects Raspberry Pi Pico W to a Wi-Fi network with timeout and auto-reconnect
- Creates an MQTT client for Adafruit IO
- Simple, modular design ideal for students and educators
- Helps build IoT projects quickly and reliably

## 📦 Installation

Copy the `iot4schools.py` file to your Raspberry Pi Pico W using [Thonny](https://thonny.org/). More details can be found in Teachers’ guidelines for the project "Smart waste bins: how to improve waste management in smart cities?" published at https://www.iot.fizyka.pw.edu.pl (Results tab, Project #2).

## 🚀 Example Usage

```python
from iot4schools import connect_wifi, create_mqtt_client, connect_mqtt

# Connect to Wi-Fi
wlan = connect_wifi("YourSSID", "YourPassword")

# Create MQTT client for Adafruit IO
client = create_mqtt_client("your_username", "your_aio_key")

# Connect the MQTT client
connect_mqtt(client)

# Now you can use client.publish(), client.subscribe(), etc.
```

## ✅ Requirements

- Raspberry Pi Pico W
- MicroPython firmware (v1.19 or newer)
- umqtt.simple module (included in standard MicroPython builds)

## 📚 Project Context

This library was developed as part of the IoT4Schools project — an international educational initiative bringing Internet of Things and cloud computing to schools across Europe using Raspberry Pi Pico W and MicroPython.

Disclaimer:
*The European Commission's support to produce this publication does not constitute an endorsement of the contents, which reflect the views only of the authors, and the Commission cannot be held responsible for any use which may be made of the information contained therein.*

## 📝 License

License: CC BY-NC 4.0
Attribution-NonCommercial 4.0 International
You are free to share and adapt the material for non-commercial purposes, with proper attribution.


