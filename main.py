# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import matplotlib as matplotlib
import openpyxl as openpyxl
import pip

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel (r'C:\Users\Moshe\PycharmProjects\FM2007\English Premier Division Season 5 excel.xlsx', sheet_name='English Premier Division Season')
print (df)



