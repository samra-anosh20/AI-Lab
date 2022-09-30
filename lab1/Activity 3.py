#Write a Python code to keep accepting integer values from user until 0 is entered.
#Display sum of the given values.

isPrime=True
i=2
n=int(input("enter a number"))
while i<n:
    remainder=n%i
    if remainder==0:
        isPrime=False
        break
    else:
        i+1
if isPrime:
    print("number is prime")
else:
    print("number is not prime")
