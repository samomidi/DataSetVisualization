print("1 -------version 1")
'''
import csv
filename = 'sitka_weather_07-2014.csv'
with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)
    print(header_row)
    header_row = next(reader)
    print(header_row)

print("2-------version 2")
filename = 'sitka_weather_07-2014.csv'
with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index,column_header)

'''
print("3 -------version 3")

# Getting high tempreture from the file
import csv
from matplotlib import pyplot as plt

from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")

            high = int(row[1])

            low = int(row[3])

        except ValueError:
            print(current_date, 'Missing Data')
            # continue
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            
    print(highs)

plt.figure(dpi=128, figsize=(8, 4))

# Highlighting the area between two values of Y axe
plt.plot(dates, highs, c='red', alpha=0.7)
plt.plot(dates, lows, c='blue', alpha=0.7)
plt.fill_between(dates, highs, lows, alpha=0.1)


# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth=5, c='Red')

plt.xlabel('', fontsize=16)
# fig.autofmt_xdate() not working
plt.ylabel("Temperature F", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.title("Daily high and low tempretures - 2014", fontsize=24)

plt.show()


