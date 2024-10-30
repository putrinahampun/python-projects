# This program is simple shopping receipt program.

import os 

# Empty list for saving the data.
breads = []

# This code for taking data from user. 
isCustomerNumber = input("Enter customer number: ")
isCustomer = input("Enter customer's name: ")

while True:
    # This code for taking data from user.
    isBread = input("Enter the purchased bread: ")
    isCount = int(input("How much?: "))
    isCost = int(input("How much does it cost? (per unit): "))

    # This code for adding the data, from bread_list to breads
    bread_list = [isBread, isCount, isCost] 
    breads.append(bread_list) 

    # This code for ending the program and showing the receipt
    isEnd = input("Is there anything else you want to add? (y/n): ")
    os.system('cls')
    if isEnd == 'n':
        os.system('cls')
        print(f"{'BREAD SHOP':^50}")
        print(f"{'Jl. Kue Hangat No.123, Kota Kue':^50}")
        print(f"{'Telp:08xxxxxxxxx Email:breadshop@yahoo.id':^50}")
        print('-'*50)
        print(f"CODE: BSC-0{isCustomerNumber:<10} Customer's Name: {isCustomer}")
        print('-'*50)

        print(f"{'NO':<3} | {'BREAD NAME':<20} | {'QUANTITY':<2} | {'TOTAL COST'}")
        print('-'*50)
        total = 0
        for index, bread in enumerate(breads):
            total_cost = int(bread[2] * bread[1]) 
            print(f"{index+1:<2}  | {bread[0]:<19}  |  {bread[1]:<6}  | Rp.{total_cost}")

            total += total_cost 

        print('-'*50) 
        print(f"Total: Rp. {total}")

        print("Thank you!")
        print("Please Come Again!")
        break









