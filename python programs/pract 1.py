# i)calculate the area of triangle

a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  

s = (a + b + c) / 2  
   
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)

# ii) calculate the area of circle

PI=3.14
r=float(input("Enter the radius of a circle:"))
area=PI*r*r
print("Area of a circle= %.2f"%area)

#calculate the area of the rectangle

l=float(input('Enter the length of a Rectangle:'))
b=float(input('Enter the breadth of a Rectangle:'))
Area=l*b
print("Area ofaRectangle is: %.2f"%Area)
           
