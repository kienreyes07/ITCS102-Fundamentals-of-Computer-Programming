import getpass

user = "Kien Reyes"
password = "backburger"

u = input("Enter Username ---> ")
p = getpass.getpass ("Enter Password ---> ")

if u == user or p == password:
    print("Correct Password*")
else:
    print("Incorrect Password Try Again", (getpass.getpass))

print("==============APPLICATION===============")
job = input("Enter Your Job: ")
age = int(input("Enter Your Age: "))
is_employed = bool(input("Currently Employed (yes/no): ") == "yes")
credit_score = eval(input("Enter Credit Score: "))
annual_income = eval(input("Enter Your Annual Income: "))
has_collateral = bool(input("Do You Have Any Collateral (yes/no): ") == "yes")
print("=======================================")


if age >= 21 and is_employed == True:
    print("Approved: Meets baseline criteria")

    if credit_score >= 750:
        print("Approved: Excellent credit score")

        if annual_income >= 100000:
            base_interest_rate = 4.5
            print("Hello, your base interest rate is:", base_interest_rate, "%")
        else:
            base_interest_rate = 5.0
            print("Hello, your base interest rate is:", base_interest_rate, "%")

    elif credit_score >= 600 and credit_score < 750:
        if has_collateral == True:
            base_interest_rate = 7.0
            print("Hello, your base interest rate is:", base_interest_rate, "%")
        elif annual_income < 40000:
            base_interest_rate = 9.5
            print("Hello, your base interest rate is:", base_interest_rate, "%")
        else:
            base_interest_rate = 8.0
            print("Hello, your base interest rate is:", base_interest_rate, "%")

    else:
        print("Rejected: Poor credit score")

else:
    print("Rejected: Fails baseline criteria")

    