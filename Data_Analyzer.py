# Data Analyzer #
# A program that takes a list of numbers
# (simulating sensor readings), analyzes them, and displays the results visually.

# Goals
# Store a dataset of numbers (like temperature readings over 10 days)
# Calculate min, max, average, and range
# # Plot the data as a line graph using matplotlib
# Make it look clean with labeled axes and a title

import matplotlib.pyplot as plt

readings = [72, 68, 75, 80, 63, 71, 77, 85, 69, 74, 78, 82, 66, 70]


def info(readings):
    minimum_t = min(readings)
    maximum_t = max(readings)
    avg = round(sum(readings)/len(readings), 2)
    temp_range = max(readings) - min(readings)
    print(f""" 
        Minimum temperature: {minimum_t}
        Maximum temperature: {maximum_t} 
        Average temperature: {avg}
        Range:               {temp_range}""")


info(readings)


def above_average(readings):
    avg = round(sum(readings)/len(readings), 2)
    above_list = []
    above = 0
    for i in readings:
        if i > avg:
            above_list.append(i)
            above += 1
    print(f""" {above} readings are above average ({avg}):
          {above_list}""")


above_average(readings)


def plot_data(readings):
    days = list(range(1, len(readings) + 1))
    avg = round(sum(readings) / len(readings), 2)

    plt.figure(figsize=(10, 5))
    plt.plot(days, readings, color="blue", marker="o", label="Temperature")
    plt.axhline(y=avg, color="red", linestyle="--", label=f"Average ({avg}°F)")
    plt.title("Temperature Readings Over 14 Days")
    plt.xlabel("Day")
    plt.ylabel("Temperature (°F)")
    plt.legend()
    plt.grid(True)
    plt.show()


plot_data(readings)
