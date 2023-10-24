from microbit import *
import temperature

# Initialize variables to store temperature data
current_temperature = 0.0
highest_temperature = -100.0  # Initialize with a low value
lowest_temperature = 200.0  # Initialize with a high value

# Time variables
previous_millis = 0
interval = 60000  # 1 minute interval

while True:
    # Read temperature from the micro:bit sensor and convert to Fahrenheit
    current_temperature = temperature.temperature() * 9 / 5 + 32

    # Update highest and lowest temperatures
    if current_temperature > highest_temperature:
        highest_temperature = current_temperature
    if current_temperature < lowest_temperature:
        lowest_temperature = current_temperature

    # Display temperature at one-minute intervals
    current_millis = running_time()
    if current_millis - previous_millis >= interval:
        previous_millis = current_millis

        # Display the current temperature on the LED screen
        display.scroll(str(round(current_temperature, 2)) + "F")

        # Reset the lowest and highest temperature values after displaying
        lowest_temperature = 200.0
        highest_temperature = -100.0

    # Check for button presses
    if button_a.was_pressed():
        # Button A pressed, display highest temperature
        display.scroll("Highest: " + str(round(highest_temperature, 2)) + "F")
        sleep(1000)  # Delay to prevent multiple readings on button press

    if button_b.was_pressed():
        # Button B pressed, display lowest temperature
        display.scroll("Lowest: " + str(round(lowest_temperature, 2)) + "F")
        sleep(1000)  # Delay to prevent multiple readings on button press

