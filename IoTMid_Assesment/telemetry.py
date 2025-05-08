from azure.iot.device import IoTHubDeviceClient, Message
import time
import random
from datetime import datetime

# Replace with your actual device connection string
CONNECTION_STRING = "HostName=iotware.azure-devices.net;DeviceId=pi5;SharedAccessKey=iRhzos11MdzKR8gu6LK1BHRDNu8QR1s43HiH4IgFHV8="

# Create client
device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

# Connect to IoT Hub
device_client.connect()

# Static info for the device
DEVICE_ID = "Sensor-A"
LOCATION = "Chennai"

# Send telemetry
while True:
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    temperature = round(random.uniform(28.0, 30.0), 1)
    humidity = round(random.uniform(55.0, 60.0), 1)
    pm2_5 = random.randint(30, 40)
    pm10 = random.randint(70, 75)

    telemetry = {
        "Timestamp": timestamp,
        "DeviceID": DEVICE_ID,
        "Location": LOCATION,
        "Temperature_C": temperature,
        "Humidity_Percent": humidity,
        "PM2_5": pm2_5,
        "PM10": pm10
    }

    msg = Message(str(telemetry))
    device_client.send_message(msg)
    print(f"Message sent: {telemetry}")
    time.sleep(5)
