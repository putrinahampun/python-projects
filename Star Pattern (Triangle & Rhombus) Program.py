# This program can be used to create 
# star pattern (triangle and rhombus)

import os

while True:
    os.system('cls') 

    print(20*'=')
    print(f"{'WELCOME':^20}")
    print(20*'=')

    print("What kind of triangle you want to build?:")
    print("1. Half of triangle.")
    print("2. Full of triangle.")
    print("3. Rhombus.")
    print('-'*20)

     # This code for taking the data from user. 
    isShape = int(input('Input the option (1/2/3): '))
    isLength = int(input('Input the length:'))

    # This code for creating the triangle. 
    if isShape == 1: #code for option 1
        count = 1
        while True: 
            print("*"*count) 
            count +=1 

            if count > isLength:
                break 
    elif isShape == 2: #code for option 2
        count = 1 
        space = int(isLength/2)

        while True:
            if count % 2 == 0: #the even number will not be counted.
                count += 1
                continue 
            
            print(' '*space,'*'*count)
            space -= 1
            count += 1

            if count > isLength:
                break 
    elif isShape == 3: #code for option 3
        count = 1
        space = int(isLength/2)

        while True: #code for the top 
            if count % 2 == 0: #the even number will not be counted.
                count += 1
                continue
            
            print(" "*space,"*"*count)
            space -= 1 
            count += 1

            if count > isLength:
                break 

        count -= 2
        space += 2

        while True: #code for the bottom
            if count % 2 == 0: #the even number will not be counted.
                x = count 
                count -= 1
                continue
            else:
                print(" "*space,"*"*count)
                space += 1 
                count -= 1
            if count < 1:
                break   
    else:
        print("Please input the right option.")

    # This code for ending this program (y=yes, n=no)
    isNext = input('Wanna try it again? (y/n):')
    if isNext == 'n':
        print('This is the end of the program!')
        break  





