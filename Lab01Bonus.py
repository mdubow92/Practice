#
# Megan Dubowski
# 05/21/23
# CSC-121.0001
# This program converts a user-entered number of meters and
# converts it to feet.
#

# Get the number of feet.
meters = float(input('Enter number of meters:'))

# Calculate the meter equivalent.
feet = meters * 3.281

# Display the number of meters.
print("That is equal to", f'{feet:.2f}', "feet.")
