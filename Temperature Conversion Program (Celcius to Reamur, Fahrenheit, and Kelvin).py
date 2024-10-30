# This program can convert the celcius' value to 
# fahreinheit, reamur, and kelvin

import os 

while True:

    # This code for cleaning the terminal. 
    os.system('cls')

    print(f"{'TEMPERATURE CONVERSION PROGRAM':^55}")
    print(55*'-')
    print('Notes:')
    print('r=reamur f=fahrenheit k=kelvin')

    # This code for taking input from user. 
    celcius = float(input("Enter the celcius'value: "))
    convert = input('Choose type of temperature (r,f,k): ')

    print('-'*55)

    # This code for choosing the temperature options. 
    if convert == 'r': #convert to reamur 
        reamur = (4/5) * celcius 
        print(f'{celcius}C to Reamur = {reamur:.2f}R')
    elif convert == 'f': #convert to fahreinheit 
        fahrenheit = (9/5 * celcius) + 32
        print(f'{celcius}C to Fahreinheit = {fahrenheit:.2f}F')
    elif convert == 'k': #convert to kelvin 
        kelvin = celcius + 273
        print(f'{celcius}C to Kelvin = {kelvin:.2f}K')
    else:  
        print("You're just allowed to choose these options: r,f,k!")
    
    # This code for ending the program. 
    is_done = input('Do you want to do the converting again? (y/n):')
    if is_done == 'n':
        print('This is the end of the program!')
        break
    

