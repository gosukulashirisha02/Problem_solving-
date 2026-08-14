
amount=int(input("enter amount:"))
chocolate_cost=int(input("enter chocolate cost:"))
chocolate_buyed=amount//chocolate_cost
remaining_money=amount%chocolate_buyed
print(chocolate_buyed)
print(remaining_money)


units=int(input("enter units:"))
bill=0
if units<=10:
    bill=units*5
  
elif units<=50:
    bill=(10*5)+(units-10)*10
   
else:
    bill=10*5+40*10+(units-50)*12
print(bill)

# Automorphic number
num=int(input("enter number:"))
square=num*num
count=0
n=num
while n>0:
    n=n//10
    count +=1
if square%(10**count)==num:
    print("Automorphic number")
else:
    print("Not  an Automorphic number")
    
#sum of digits
n=int(input("enter number:"))
digit_sum=0

while n>0:
    last_digit=n%10
    digit_sum=digit_sum+last_digit
    n=n//10
print(digit_sum)



