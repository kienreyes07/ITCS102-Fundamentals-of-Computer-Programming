#first import program!!!

import getpass

account = "Kien Reyes"
password = "sikret po"

a = input("Please Enter Account Name: ")
p = getpass.getpass("Input Password: ")

if a == account or p == password:
	print("Account Found")

else: 	
	print("No Account Found", (getpass.getpass))