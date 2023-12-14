# Generate Fibonaaci Series

n = int(input("Enter a number: "))

n1, n2 = 0,1
count = 0

# check number is valid or not
if n<=0:
    print("Please enter a valid number")
elif n==1:
    print("Fibonacci upto:",n,"is",n1)
else:
    print("Fibonaaci series: ")
    while count<n:
        print(n1, end=" ")
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1