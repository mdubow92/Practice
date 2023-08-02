# Megan Dubowski
# 05/19/23
# CSC-121.0001
# This program calculates what a customer should pay at Bargain Used Books.

# The input steps begin here.
workbook = int(input('Enter the number of workbooks: ')) * 8.50
textbook = int(input('Enter the number of textbooks: ')) * 24.00
magazine = int(input('Enter the number of magazines: ')) * 5.95

# The processing steps begin here.
subtotal = workbook + textbook + magazine
tax = int(subtotal) * 0.06
total = subtotal + tax

# The output steps begin here.
print(f'Cost before tax: ${subtotal:.2f}')
print(f'Sales tax: ${tax:.2f}')
print(f'Cost after tax: ${total:.2f}')
