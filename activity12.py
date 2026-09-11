#if, elif and else project

name = input("Enter Name: ")
age = int(input("Enter Age: "))


if age >= 0 and age <= 5 : 
	print("You are classified as an INFANT")

elif age >= 6 and age <= 12 :
	print("You are classified as a KID")

elif age >= 13 and age <= 15 :
	print("You are classified as PRE-TEEN")

elif age >= 16 and age <= 19 :
	print("You are a TEENAGER")

elif age >= 20 and age <= 29:
    print("You are a ENTERING ADULTHOOD")

elif age >= 30 and age <= 50:
    print("You are a ADULT")

elif age >= 51 and age <= 80:
    print("You are a SENIOR ")

else:
	print("Age not classified")

