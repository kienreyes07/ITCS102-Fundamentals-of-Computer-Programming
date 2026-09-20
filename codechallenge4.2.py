#kien cc4 sorry for the late submission sir i was absent 2 days due to sickness and diarrhea


import getpass

print("===============WELCOME===============")

username = input("Create Username ---> ")
pass1 = getpass.getpass ("Create Password ---> ")
pass2 = getpass.getpass ("Enter Password Again ---> ")

print("===============LOGGED IN===============")

if pass1 or pass2:
    print("Correct Password*")
else:
    print("Incorrect Password Try Again", (getpass.getpass)) 


loanee = input("What is your name? ---> ")
job_description = input("Input Job Description ---> ")
loan_ammount = input("How much loan do you need? ---> ")


print("==============APPLICATION===============")
job = input("Enter Your Job: ")
age = int(input("Enter Your Age: "))
is_employed = bool(input("Currently Employed (yes/no): ") == "yes")
credit_score = eval(input("Enter Credit Score: "))
annual_income = eval(input("Enter Your Annual Income: "))
has_collateral = bool(input("Do You Have Any Collateral (yes/no): ") == "yes")

what_collateral = "none"
value = "0.0"

if has_collateral:
    input("What Collateral? (e.g motorcycle, land, house): ")
    value = float(input("Enter Value:  "))

    if value < 30000:
        print("Insufficient Value: Must be Above 300.000 PHP.")
        has_collateral = False


base_rate = 5.0 
intest_rate = 0.0


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
        print("============Rejected============") 
        print("Rejected: Credit score too low.") 
        print("Requirements: Credit score must be at least 600.")
        print("Please try again. =======================================")
        exit()

else:
    print("============Rejected!============") 
    print("Rejected: Failed to meet the requirements.") 
    print("Requirements: Age between 21 and 75, and must be employed.")
    print("Please try again.")
    print("=======================================")
    exit()
    
print("You have been approved for a loan!! ")

print ("============RESULT============")
print("Age:", age)
print("Is employed:", is_employed)
print("Credit Score:", credit_score)
print("Annual Income:", annual_income)
print("Loan Ammount: ", loan_ammount)
print("Has Collateral:", has_collateral)
print("==============================")
    