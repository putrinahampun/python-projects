# This program can convert the kelvin's value to fahrenheit,
# and vice versa. 

"""
    Fahrenheit  
    F = 9/5C + 32 
    F - 32 = 9/5C 
    C = 5/9(F-32)
    K = (5/9(F-32)) + 273

    Kelvin 
    K = C + 273 
    C = K - 273 
    F = 9/5(K - 273) + 32  
"""

import os 

while True:
    os.system('cls') 

    print(f"{'=== TEMPERATURE CONVERSION PROGRAM ===':^50}")
    print('-'*50) 
    print('Notes:')
    print('k=kelvin f=fahreinheit')

    # This code for taking the data from user. 
    print("Please choose these options:")
    print('1. Convert Kelvin to Fahrenheit.')
    print('2. Convert Fahrenheit to Kelvin.')
    option = int(input('Choose the option (1/2): '))
    value = float(input('Enter the value: ')) 

    if option == 1:
        n_F = (9/5)*(value - 273) + 32
        print(f"{value}K = {n_F}F")
    elif option == 2:
        n_K = ((5/9)*(value-32)) + 273
        print(f"{value}F = {n_K}K")
    else:
        print("Please input the right option!")

    isEnd = input('Do you want to try it again? (y/n): ')
    if isEnd == 'n':
        print('This is the end of the program!')
        break 


