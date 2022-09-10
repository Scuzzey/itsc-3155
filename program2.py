def prgm2(num1,num2):

    count = 0
    if num1 < num2:
        count = num1
    else: 
        count = num2

    while count in range(num1,num2):
        if count % 7 == 0 and count % 5 != 0:
            print (count)
        count += 1

num1 = input("Please Enter Your First Number ")
num2 = input("Please Enter Your Second Number ")

num1 = int(num1)
num2 = int(num2)

divBy = prgm2(num1,num2)
print(divBy)


