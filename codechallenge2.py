#ph denomination

a = 1000
b = 500
c = 200
d = 100
e = 50
f = 20
g = 10
h = 5
i = 1

money = eval (input("Enter Money to Deposit --> "))

dif = money

sum = dif // a
dif = dif % a

sum2 = dif // b
dif = dif % b

sum1 = dif // c
dif = dif % c 

sum3 = dif // d
dif = dif % d

sum4 = dif // e
dif = dif % e

sum5 = dif // f
dif = dif % f

sum6 = dif // g
dif = dif % g

sum7 = dif // h
dif = dif % h

sum8 = dif // i
dif = dif % i

print()
print("====================PH DENOMINATION====================")
print("MONEY TO DEPOSIT --------- > ", money)


print("\t1000:",sum)
print("\t500:",sum2)
print("\t200:",sum1)
print("\t100:",sum3)
print("\t50 :",sum4)
print("\t20 :",sum5)
print("\t10 :",sum6)
print("\t5 :",sum7)
print("\t1 :",sum8)
print("====================END OF BREAKDOWN====================")
