# This program can calculate two numbers  
# for adding, substracting, multiplying
# and dividing. 


import os 

while True:
    os.system('cls')

    print(20*'=')
    print(f'{"CALCULATOR":^20}')
    print(20*'=')
    
    # This code for taking data from user   
    number1 = float(input('Input the first number: '))
    number2 = float(input('Input the second number: '))
    operator = input('Operator (+,-,x,/) :')

    # This code is for each selected operator.  
    if operator == '+': # code for adding. 
        result = number1 + number2
        print(f'{number1} + {number2} = {result}')
    elif operator == '-': # code for substracting. 
        result = number1 - number2
        print(f'{number1} - {number2} = {result}')
    elif operator == '*' or operator =='x': # code for multiplying. 
        result = number1 * number2
        print(f'{number1} x {number2} = {result}')
    elif operator == '/': # code for dividing.
        result = number1 / number2
        print(f'{number1} / {number2} = {result}')
    else:
        print('Please input the correct operator!')
    
    # This code for ending the program (y=yes, n=no)
    print('-'*20)
    isNext = input('Do you want to try it again? (y/n)')  
    if isNext == 'n':
        print("This is the end of the program!")
        break 



