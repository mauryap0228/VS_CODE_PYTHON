# Data Analyzer #
# A program that takes a list of numbers
# (simulating sensor readings), analyzes them, and displays the results visually.

# Goals
# Store a dataset of numbers (like temperature readings over 10 days)
# Calculate min, max, average, and range
# # Plot the data as a line graph using matplotlib
# Make it look clean with labeled axes and a title

import serial
import time
import matplotlib.pyplot as plt

#  Serial setup
ser = serial.Serial('/dev/cu.usbmodem1401', 9600)

temp_readings = []
humidity_readings = []

start_time = time.time()
duration = 3600  # 1 hour

print("Collecting data for 1 hour...")

while time.time() - start_time < duration:
    line = ser.readline().decode('utf-8').strip()

    if line.startswith("Temp:"):
        try:
            # line looks like: "Temp: 72.50 F  Humidity: 45.00 %"
            parts = line.split()
            temp_value = float(parts[1])       # the number right after "Temp:"
            # the number right after "Humidity:"
            humidity_value = float(parts[4])

            temp_readings.append(temp_value)
            humidity_readings.append(humidity_value)

            print(
                f"Logged -> Temp: {temp_value}F  Humidity: {humidity_value}%")
        except (IndexError, ValueError):
            print("Skipped a malformed line:", line)

print("Done collecting.")
ser.close()

#  Analysis functions


def info(readings, label, unit):
    minimum = min(readings)
    maximum = max(readings)
    avg = round(sum(readings) / len(readings), 2)
    data_range = max(readings) - min(readings)
    print(f"""
        Minimum {label}: {minimum}{unit}
        Maximum {label}: {maximum}{unit}
        Average {label}: {avg}{unit}
        Range:           {data_range}{unit}""")


def above_average(readings, label, unit):
    avg = round(sum(readings) / len(readings), 2)
    above_list = []
    above = 0
    for i in readings:
        if i > avg:
            above_list.append(i)
            above += 1
    print(f""" {above} {label} readings are above average ({avg}{unit}):
          {above_list}""")


def plot_data(readings, label, unit, color):
    days = list(range(1, len(readings) + 1))
    avg = round(sum(readings) / len(readings), 2)

    plt.figure(figsize=(10, 5))
    plt.plot(days, readings, color=color, marker="o", label=label.capitalize())
    plt.axhline(y=avg, color="red", linestyle="--",
                label=f"Average ({avg}{unit})")
    plt.title(f"{label.capitalize()} Readings Over {len(readings)} Intervals")
    plt.xlabel("Reading #")
    plt.ylabel(f"{label.capitalize()} ({unit})")
    plt.legend()
    plt.grid(True)
    plt.show()


# Run analysis on the collected data
if len(temp_readings) > 0:
    info(temp_readings, "temperature", "°F")
    above_average(temp_readings, "temperature", "°F")
    plot_data(temp_readings, "temperature", "°F", "blue")

if len(humidity_readings) > 0:
    info(humidity_readings, "humidity", "%")
    above_average(humidity_readings, "humidity", "%")
    plot_data(humidity_readings, "humidity", "%", "green")
