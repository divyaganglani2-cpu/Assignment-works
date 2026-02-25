import math
import geometry_tools as g
radius=float(input("Enter the radius of the circle: "))
area=g.area_circle(radius)
print(f"The area of the circle is {math.ceil(area)}")
#checking other functions
# print(g.hypo(3,5))
# print(g.perimeter_rect(4,5))
#task B-
num=int(input("Enter a integer for factorial: "))
print(f"factorial of {num} is {math.factorial(num)}")
#gcd-greatest common divisor(hcf)
print(f"gcd of 24 and 54 is : {math.gcd(24,54)}")
#power logic
x=int(input("Enter the base number: "))
y=int(input("Enter the power no: "))
print(f"if {x} is multiplied {y} times by itself ,the result is {math.fabs(math.pow(x,y))}")
# scientific round function
def Scientific_round(n):
    deci=n-math.floor(n)
    if deci>0.5:
        return math.ceil(n)
    else: 
        return math.floor(n)
i=float(input("Enter a decimal value to be rounded off: "))
print(f"Rounding number {i} gives : {Scientific_round(i)}")