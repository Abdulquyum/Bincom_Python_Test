#!/usr/bin/env python3

import statistics
from collections import Counter

shirt_colors = [
    "green",
    "yellow",
    "blue",
    "brown",
    "pink",
    "orange",
    "red",
    "white",
    "cream",
    "black",
    "arsh"
]

tshirt_color_monday = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"]
tshirt_color_tuesday = ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"]
tshirt_color_wednessday = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"]
tshirt_color_thursday = ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"]
tshirt_color_friday = ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]

all_tshirt_colors = (
    tshirt_color_monday 
    + tshirt_color_tuesday 
    + tshirt_color_wednessday 
    + tshirt_color_thursday 
    + tshirt_color_friday
)

# Which color of shirt is the mean color?
# mean = sum(numbers) / len(numbers)

frequency = Counter(all_tshirt_colors)

mean_worn_color = statistics.mean(frequency.values())

print(f'mean_worn_color: {mean_worn_color}')

# Which color is mostly worn throughout the week?
mostly_worn_color = frequency.most_common(1)[0][0]

print(f'mostly_worn_color: {mostly_worn_color}')

# Which color is the median?
sorted_colors = sorted(all_tshirt_colors)
median_worn_color = statistics.median(sorted_colors)

print(f'median_worn_color: {median_worn_color}')

# BONUS Get the variance of the colors
variance_worn_color = statistics.variance(frequency.values())

print(f'variance_worn_color: {variance_worn_color}')

# BONUS if a colour is chosen at random, what is the probability that the color is red?
# probability = number of red shirts / total number of shirts

red_count = frequency.get("RED", 0)
total_count = sum(frequency.values())
red_probability = red_count / total_count if total_count > 0 else 0

print(f'red_probability: {red_probability}')

#   Save the colours and their frequencies in postgresql database

# conn = psycopg2.connect(
#     host="localhost",
#     database="mydb",
#     user="myuser",
#     password="mypassword"
# )

# cur = conn.cursor()

# for color, count in frequency.items():
#     cur.execute("INSERT INTO shirt_colors (color, frequency) VALUES (%s, %s)", (color, count))

# conn.commit()
# cur.close()
# conn.close()