#
# Megan Dubowski
# 05/19/23
# CSC-121.0001
# This program converts a user-entered number of feet and
# converts it to meters.
#
# Note: The number of feet entered could be a floating point
# number.
#

# Get the number of feet.
feet = float(input('Enter number of feet:'))

# Calculate the meter equivalent.
meters = feet / 3.281

# Display the number of meters.
print("That is equal to", f'{meters:.2f}', "meters.")
