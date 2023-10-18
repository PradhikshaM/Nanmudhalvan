import random
import time

# Simulated environmental data generation
def generate_environmental_data():
    temperature = random.uniform(10, 40)  # Simulated temperature data (in Celsius)
    humidity = random.uniform(30, 80)     # Simulated humidity data (in percentage)
    return temperature, humidity

# Main loop to continuously collect and print data
while True:
    temperature, humidity = generate_environmental_data()
    
    # You can replace this with code to send data to your IoT platform
    print(f"Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%")
    
    # Adjust the time interval as needed (e.g., every 5 minutes)
    time.sleep(300)  # Sleep for 5 minutes (300 seconds)