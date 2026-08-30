# num=int(input("enter the number:"))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count +=1
# if count==2:
#         print("prime number")
# else:
#         print("not a prime")


# n=int(input("enter limit:"))

# for num in range(2,n+1):
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count +=1
#     if count==2:
#         print(num)
    
    
# n=10
# a,b=0,1
# for i in range(10):
#     print(a,end="")
#     a,b=b,a+b
    
    
# s="shirisha"
# freq={}
# for char in s:
#     if char in freq:
#         freq[char]+=1
#     else:
#         freq[char]=1
# print(freq)

# nums=[10,20,20,30,30,40,40,50]
# unique=list(set(nums))
# print(sorted(unique))

# nums=[10,20,20,40,70,30,60,30,60,50]
# result=[]
# for num in nums:
#     if num not in result:
#         result.append(num)
# print(sorted(result))

# nums=[10,20,70,50,30,686,974]
# nums.sort()

# print("2nd highest number:",nums[-2])


# n=int(input("enter number:"))
# digit_sum=0
# while n>0:
#     last_digit=n%10
#     digit_sum=digit_sum+last_digit
#     n=n//10
# print(digit_sum)


# num=int(input("enter number:"))
# total=0
# for i in range(num):
#     # num=int(input("enter number:"))
#     total=total+num
# print("sum=",total)
    
    
# word="madam"
# rev=""
# for i in range(len(word)-1,-1,-1):
#     rev=rev+word[i]
# print(rev)
# if rev==word:
#         print("panlindrome")
# else:
#         print("not")

# a="apple"
# revstr=""
# for i in range(4,-1,-1):
#     # print(a[i])
#     revstr=revstr+a[i]
# print(revstr)

# a,b=map(int,input().split())
# max_sum=0
# ans=0
# for i in range (a,b+1):
#     n=i
#     s=0
    
#     while n>0:
#         s +=n%10
#         n//=10
#     if s>max_sum:
#         max_sum=s
#         ans=i
# print(ans)


# a, b = map(int, input("enter number:").split())

# max_sum = 0
# ans = 0

# for i in range(a, b + 1):
#     n = i
#     s = 0

#     while n > 0:
#         s += n % 10
#         n //= 10

#     if s > max_sum:
#         max_sum = s
#         ans = i

# print(ans)



# # reverse of number
# number=int(input("enter the number:"))
# result=0
# while number>0:
#     last_digit=number%10
#     result=result*10+last_digit
#     number=number//10
# print(result)
    
# #plaindrome
# number=int(input("enter number:"))
# result=0
# original=number
# while number>0:
#     last_digit=number%10
#     result=result*10+last_digit
#     number=number//10
# if original==result:
#     print("plaindrome")
# else:
#     print("not plaindrome")
    
# # Sum of Digits 
# number=int(input("enter number"))
# digit_sum=0
# while number>0:
#     last_digit=number%10
#     digit_sum=digit_sum+last_digit
#     number=number//10
# print(digit_sum)

# #digit root
# n=int(input("enter number:"))
# digit_root=0
# while n>10:
#     digit_root=0
#     while n>0:
#         last_digit=n%10
#         digit_root=digit_root+last_digit
#         n=n//10
#     n=digit_root
# print("the digit_root is:",digit_root)

# #count
# n=int(input("enter number:"))
# count=0
# while n>0:
#     n=n//10
#     count +=1
# print(count)

# # Product of Digits 
# number=int(input("enter number:"))
# digit_product=1
# while number>0:
#     last_digit=number%10
#     digit_product=digit_product*last_digit
#     number=number//10
# print(digit_product)


# #. Harshad Number 
# n=int(input("enter number:"))
# original=n
# digit_root=0
# while n >0:
#     last_digit=n%10
#     digit_root=digit_root+last_digit
#     n=n//10
# if original%digit_root==0:
#     print("Harshad Number ")
# else:
#     print("not Harshad Number ")
    
    
# #neon number
# number=int(input("enter number:"))
# square=number*number
# digit_sum=0
# original_number=number
# while square>0:
#     last_digit=square%10
#     digit_sum=digit_sum+last_digit
#     square=square//10
# if digit_sum==number:
#     print("neon number")
# else:
#     print("not a neon number")
    
    

#amstron number
# n=int(input("enter number:"))
# count=0
# original=n
# second=original
# while n>0:
#     count +=1
#     n=n//10
# print(count)
# result=0
# while original>0:
#     last_digit=original%10
#     result=result+last_digit**count
#     original=original//10
# if second==result:
#     print("amstrong")
# else:
#     print("not a amstrong")
    
#spy num1    
# num=int(input("enter number:"))
# sum_of_digits=0
# product_of_digits=1
# while num>0:
#     last_digit=num%10
#     sum_of_digits=sum_of_digits+last_digit
#     product_of_digits=product_of_digits *last_digit
#     num=num//10
# if sum_of_digits==product_of_digits:
#     print("spy")
# else:
#     print("not spy")
    
    
#perfect number
# num=int(input("enter number:"))
# res=0
# for i in range(1,(num//2)+1):
#     if num%i==0:
#         res +=i
# if res==num:
#     print("perfect number")
# else:
#     print("not a pn")

    
#swap of first and last
# n=int(input("enter number:"))
# last=n%10
# count=0
# original=n
# while n>10:
#     count +=1
#     n//=10
# first=n
# power=10**count
# middle=(original%power)//10
# result=last*power+middle*10+first
# print(result)



# print(*range(1,101))

n=int(input("enter number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum += i
if sum==n:
    print("perfect")
else:
    print("not a perfect")
    



  

    
