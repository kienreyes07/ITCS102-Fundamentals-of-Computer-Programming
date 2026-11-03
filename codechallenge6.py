#cc6 kien
num = int(input("Enter number ---> "))


for x in range (num):
    for y in range (num):
        if x==y or y+x == num -1: 
            print("*", end=" ")
        else: 
          print(" ", end=" ")
    print()
