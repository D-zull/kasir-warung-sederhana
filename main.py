#!/usr/bin/env python3

import os;
from time import sleep;

#column = int(os.system("stty size|cut -d' ' -f2"))
print("=" * 50)
print("\033[1;36mhi, welcome ngab\033[m".center(62))
print("=" * 50 + "\n")
print("menu\n".center(50))
print("1. cashier")
print("2. calculator")
print("0. quit")

a = str()
b = int()
sleep(1)


pilihan = int(input("\nchoose menu: "))

def cashier():
    print("="* 50)
    print("\033[1;36mcashier menu\033[m".center(62))
    print("=" * 50 + "\n")
    print()
    sleep(1)
    item = str(input("enter item name: "))
    item_total = int(input("enter item amount: "))
    give_money = int(input("pay: "))

    if item == "Mancis":
        item_price = 2000
    elif item == "Rokok":
        item_price = 10000
    else:
        print("\nItem", item, "currently unavailable!")
        exit(1)

    price = (item_price * item_total)
    money_back = (give_money - price)

    print("-" * 50)
    print("item name: ", item)
    print("item amount: ", item_total)
    print("money:", give_money, "idr")
    print("total item price: ", price, "idr")
    print("\ncounting the change...\n")
    sleep(3)
    print("money back:", money_back, "idr")
    counter_cashier()
    
def counter_cashier():
	counter = input("back to cashier menu? (y/n)")
	if counter == "y":
		cashier()
	elif counter == "n":
		print("program exited")
		exit()
		

def calculator():
	print("="* 50)
	print("\033[1;36mcalculator menu\033[m".center(62))
	print("=" *50 + "\n")
	sleep(1)
	first_number = int(input("enter first number: "))
	two_number = int(input("enter two number: "))
	operator = str(input("choose operator (+ - * /): "))
	hasil = 0
	
	if operator == "+":
		hasil = first_number+two_number
	elif operator == "-":
		hasil = first_number-two_number
	elif operator == "*":
		hasil = first_number*two_number
	elif operator == "/":
		hasil = first_number/two_number
	else:
		print("undefine operator")
		
	print("counting...")
	sleep(3)
	print("hasil: ", hasil)
	counter_calculator()
	
def counter_calculator():
	counter = input("back to calculator menu? (y/n) :")
	if counter == "y":
		calculator()
	elif counter == "n":
		print("program exited")
		exit()
	
		
		

#
# INI KAYAKNYA GAK ADA YANG SALAH!!!
#

if pilihan == int(1):
    cashier()
    exit()
elif pilihan == int(2):
    calculator()
    exit()
else:
    print("exited")
    exit(0)