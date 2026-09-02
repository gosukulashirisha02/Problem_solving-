# 1. Area of Square
side=int(input("enter side:"))
AOS=side*side
print(AOS)

# 2. Area of Rectangle
length=int(input("enter side:"))
bredth=int(input("enter side:"))
AOR=length*bredth
print(AOR)

# 3. Area of Triangle
base=int(input("enter base:"))
height=int(input("enter base:"))
AOT=(1/2)*base*height
print(AOT)

# 4.perimeter of square
side=int(input("enter side:"))
perimeter=4*side
print("perimeter of square:",perimeter)

# perimeter of triangle

side1=int(input("enter side:"))
side2=int(input("enter side:"))
side3=int(input("enter side:"))
perimeter=side1+side2+side3
print("perimeter if trianle:",perimeter)


# 7. Break Amount into 1000s, 500s, and Remaining Change.3700

amount=int(input("enter amount:"))  
a=amount//1000
b=amount-(a*1000)
c=b//500
d=b-(c*500)
e=d//200
f=d-(e*200)
g=f//100
h=f-(g*100)
i=h//50
j=h-(i*50)
k=j//20
l=j-(k*20)
m=l//10
n=l-(m*10)
print("1000's:",a)
print("500's:",c)
print("200's:",e)
print("100's:",g)
print("50's:",i)
print("20's:",k)
print("10's:",m)
print("change:",n)


# 8. Convert Seconds into Hours, Minutes, and Seconds
total_second=int(input("enter seconds:"))
hours=total_second//3600
remaining_min=total_second%3600
mintues=remaining_min//60
remaining_sec=remaining_min%60
print(hours)
print(mintues)
print(remaining_sec)

# 9. Sum ,avg of Marks (Maths, Physics, Chemistry)
n1=int(input("enter math marks:"))
n2=int(input("enter physics marks:"))
n3=int(input("enter chem: marks:"))
total_marks=n1+n2+n3
# print(total_marks)
avg=total_marks/3
print(avg)