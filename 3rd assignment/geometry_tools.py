#imports
import math
#this file would be imported as module in main file and these functions would be used there
#area of circle
def area_circle(r):
    return round(math.pi*r*r,2)
#func for hyppotenuse of right angle triangle
def hypo(l,b):
    #formula is sqrt of a square plus b square
    h=math.sqrt(math.pow(l,2)+math.pow(b,2))
    return round(h,2)
#func for perimeter of rectangle
def perimeter_rect(l,b):
    return round(2*(l+b),2)