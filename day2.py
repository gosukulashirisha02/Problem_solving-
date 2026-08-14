# 1.🧙‍♂️ The Magic Number
n=int(input("enter number:"))
digit_sum=0
while n>=10:
    digit_sum=0
    while n>0:
        last_digit=n%10
        digit_sum=digit_sum+last_digit
        n=n//10
    n=digit_sum
print("the magic number is:",n)

# 2.🚗 Lucky Car Number
n=int(input("enter the car number:"))
digit_sum=0
while n>=10:
    digit_sum=0
    while n>0:
        last_digit=n%10
        digit_sum=digit_sum+last_digit
        n=n//10
    n=digit_sum
    print(n)
if n==7:
    print("lucky number")
else:
    print("not lucky number")

# 3. 🏆 Tournament Player ID
n=int(input("enter the number ID:"))
digit_sum=0
while n>=10:
    digit_sum=0
    while n>0:
        last_digit=n%10
        digit_sum=digit_sum+last_digit
        n=n//10
    n=digit_sum
print("players rank code:",n)
    
# 4. 🔐 Secret Door Code
n=int(input("enter the secret number:"))
digit_sum=0
while n>=10:
    digit_sum=0
    while n>0:
        last_digit=n%10
        digit_sum=digit_sum+last_digit
        n=n//10
    n=digit_sum
if n%2==0:
    print("Door open")
else:
    print("Door locked")
    
    
# 5. 💰 Treasure Hunter
n=int(input("enter the gold amount:"))
digit_sum=0
while n>=10:
    digit_sum=0
    while n>0:
        last_digit=n%10
        digit_sum=digit_sum+last_digit
        n=n//10
    n=digit_sum
if n==9:
    print("Special Treasure")
else:
    print("not a Special Treasure")
    
#   6. 🐉 Dragon Energy  

n=int(input("enter enery:"))
digit_sum=0
while n>=10:
    digit_sum=0
    while n>0:
        last_digit=n%10
        digit_sum=digit_sum+last_digit
        n=n//10
    n=digit_sum
print(n)

# 7. 🎟️ Lucky Ticket — Good Interview Problem
n=int(input("enter ticket number:"))
k=int(input("enter lucky number:"))
digit_sum=0
while n>=10:
    digit_sum=0
    while n>0:
        last_digit=n%10
        digit_sum=digit_sum+last_digit
        n=n//10
    n=digit_sum
if n==k:
    print("lucky ticket")
else:
    print("not a lucky ticket")