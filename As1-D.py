'''Write a program to calculate sum of the following series: 1+2+3+...+n'''

sum=0
n=int(input("Enter number of terms : "))
for i in range(1,n+1):
    sum+=i

print(sum)