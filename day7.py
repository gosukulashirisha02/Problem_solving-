# n=5
# fact=1
# for i in range(n,1,-1):
#     fact*= i
    
# print(fact)


    


# n=6
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
        
        
# n=6
# i=1
# count=0
# while i<=n:
#     if n%i==0:
#         count +=1
#     i+= 1
# print(i)
        
        
# n=7
# count=0
# for i in range (1,n+1):
#     if n%i==0:
#         count +=1
#     i+=1
# print(i)


# n=5
# i=1
# count=0
# while i<=n:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("prime")
# else:
#     print("not prime")
    
# n=7
# count=0
# for i in range (1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("prime")
# else:
#     print("not a prime")
    
    
# n=7
# i=1
# sum=0
# while i<=n:
#     if n%i==0:
#         sum+=i
#     i+=1
# print(i)
        
# name="apple"
# print(name[-1,6,-1])

# name="ram"
# for i in range(len(name-1),-1,-1):
#     name+=len(name)
    
        

#--------- 1. Print Numbers from 1 to n------------------    
    
# n=5
# i=1
# while i<=n:
#     print(i)
#     i+=1
    
    
# n=5
# for i in range(1,n+1):
#     print(i)


#------------2. Print Numbers from m to n-----------

# m=3 
# n=7
# for i in range(m,n+1):
#     print(i)

# m=3
# n=7
# while m<=n:
#     print(m)
#     m+=1

#----------3. Print Numbers from n to 1 in Reverse-----------

# n=5
# while n>=1:
#     print(n)
#     n-=1

# n=5
# for i in range(n,0,-1):
#     print(i)
    
#----------4. Print Numbers from n to m in Reverse--------
# n=10
# m=6
# while n>=m:
#     print(n)
#     n -=1

# n=10
# m=6
# for i in range(n,m-1,-1):
#     print(i)


#---------5. Sum of n Natural Numbers---------
# n=5
# i=1
# sum=0
# while i<=n:
    
#     sum+=i
#     i+=1
# print(sum)

# n=5
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)
    
  
#-------------6. Factorial of a Number------------
# m=5
# i=1
# fact=1
# while i<=m:
#     fact*=i
#     i +=1
    
# print(fact)

# m=5
# fact=1
# for i in range(1,m+1):
#     fact*=i
# print(fact)

#---------6. Factorial of a Number---------
# m=3
# n=6
# sum=0
# while m<=n:
#     sum+=m
#     m +=1
# print(sum)

# m=3
# n=6
# sum=0
# for i in range(m,n+1):
#     sum+=i
# print(sum)

#----------8. Product of m to n Numbers----------
# m=2
# n=4
# prod=1
# while m<=n:
#     prod*=m
#     m +=1
# print(prod)
    
# m=2
# n=4
# prod=1
# for i in range(m,n+1):
#     prod*=i
    
# print(prod)
    
#----------9. ,10,Print Factors of a Number--------
# n=6
# i=1
# count=0
# while i<=n:
#     if n%i==0:
#         count +=1
#         print(i)
#     i +=1
# print(count)
        
        
# n=6
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count +=1
#         # print(i)
# print(count)

              
#-----11. Prime Number Check-----
# n=7
# i=1
# count=0
# while i<=7:
#     if n%i==0:
#         count +=1
#     i +=1
# if count==2:
#     print("prime")
# else:
#     print("np")

# n=7
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count +=1
# if count==2:
#     print("prime")
# else:
#     print("np")
        
#------12. Even ,0dd Numbers from m to n-------
# m=3
# n=10
# while m<=n:
#     if m%2==0:
#         print(m)
#     m +=1

# m=3
# n=10
# while m<=n:
#     if m%2!=0:
#         print(m)
#     m +=1

# m=3
# n=10
# for i in range(m,n+1):
#     if i%2==0:
#         print(i)
        
        
# m=3
# n=10
# for i in range(m,n+1):
#     if i%2!=0:
#         print(i)

#------------14. Count of Even and Odd Numbers--------
# m=3
# n=7
# even=0
# odd=0
# while m<=n:
#     if m%2==0:
#         even +=1
#     else:
#         odd +=1
#     m +=1
# print(even)
# print(odd)


# m=3
# n=7
# even=0
# odd=0
# for i in range(m,n+1):
#     if i%2==0:
#         even +=1
#     else:
#         odd +=1
# print(even)
# print(odd)

#----------15. Reverse a String--------
##using slicing
# word="hello"
# print(word[::-1])

# word="hello"
# for i in range(len(word)-1,-1,-1):
#     print(word[i])

# word="hello"
# rev=""
# for i in word:
#     rev=i+rev
# print(rev)

word="hello"
rev=""
i=len(word)-1
while i>=0:
    rev=rev+word[i]
    i-=1
print(rev)