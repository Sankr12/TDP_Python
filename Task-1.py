# Calculate area with conditions

def calculate_area(a,b):
    if a==b:
        print("This is a square!")
    else:
        print("Area of rectangle:", a*b)

length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))
calculate_area(length, breadth)