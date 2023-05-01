# In this python program I plan to find the distance between the Earth and the Sun.
# I plan on doing this by first changing time t into a variable that we can use.
# One of the simplest ways of doing this is by using the equation for eccentricity
# and converting time t in terms of radians. Once this is done, I will substitute phi into the eccentricity
# formula for distance at a given day. Therefore, I can find the distance between the Earth and the Sun at any
# time in the year. However, if I wanted to find today’s distance I could use the datetime command to get today’s
# exact time and date. We then convert this to the number of days in the year. Once this is done,
# I would now be able to find the distance between the Earth and the Sun on today’s date.
# This code would be helpful for almost anyone. If I were to add more information about the distance between
# the Earth and Moon and Earth’s rotational speed, you could calculate just about anything
# related to eclipses and seasonal changes.

import math

# The average distance between the Earth and the Sun in kilometers
AU = 149597870.7


def distance(t):

# Convert time t in days to angle phi in radians
    phi = 2 * math.pi * t / 365.25
# Calculate the distance between the Earth and the Sun using the equation
# r = AU * (1 + e * cos(phi)) where e is the eccentricity of the Earth's orbit

    e = 0.01671022
    r = AU * (1 - e ** 2) / (1 + e * math.cos(phi))

    return r

print(distance(0))  # prints the distance between the Earth and the Sun at the beginning of the year
print(distance(365))  # prints the distance between the Earth and the Sun at the end of the year
print(distance(185))  # prints the distance between the Earth and the Sun at a given time selected

from datetime import datetime

# Get the current time as a datetime object
now = datetime.now()
time_str = now.strftime("%Y-%m-%d %H:%M:%S")

# Assign the time string to a variable z
z = time_str
print(z)

#from datetime import datetime

# Convert time_str to a datetime object
dt_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

# Convert datetime to a number of days since January 1
days = (dt_obj - datetime(2023, 1, 1)).days

print(days)

print(distance(days))  # prints the distance between the Earth and the Sun on today's date
