#Write a Python code to keep accepting integer values from user until 0 is entered.
#Display sum of the values

sum=0
s=input("enter an integer value,.")
n=int(s)
while n!=0:
    sum=sum+n
    s=input("enter an integer value..")
    n-int(s)
print("sum of given value is ", sum)
