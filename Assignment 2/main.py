num=int(input("Enter a Number: "))
if num%2==0:
    print(num," is an Even Number")
else:
    print(num," is an Odd Number")


sum=0
for number in range(1,51):
    sum+= number
print('The Sum of the integer is: ',sum)