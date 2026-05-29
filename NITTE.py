# num=int(input("enter:"))
# if num & 1==0:
#     print("Even")
# else:
#     print("Odd")

# num1=int(input("enter1:"))
# num2=int(input("enter2 :"))
# # temp=num1
# # num1=num2
# # num2=temp
#
# num1,num2=num2,num1
#
# num1=num1+num2
# num2=num1-num2
# num1=num1-num2
#
# num1=num1^num2
# num2=num1^num2
# num1=num1^num2
#
# print(num1)
# print(num2)


# num=int(input("enter:"))
# if num%4==0:
#     print(num)
# elif num%4==1:
#     print(1)
# elif num%4==2:
#     print(num+1)
# elif num%4==3:
#     print(0)

# num=int(input("enter:"))
# if num%3==0 and num%5==0:
#     print("FizzBuzz")
# elif num%3==0:
#     print("Fizz")
# elif num%5==0:
#     print("Buzz")

# w=int(input("enter:"))
# if w%2==0 and w>2:
#     x=w//2
#     if x%2==0:
#         print(x,x)
#     else:
#         print(x-1,x+1)
# else:
#     print("NO")

# x=int(input("enter position:"))
# if x%5==0:
#     print("steps:",x//5)
# else:
#     print("steps:",x//5+1)

# num=int(input("enter:"))
# flag=0
# for i in range(2,num):
#     if num%i==0:
#         flag+=1
# if flag==0:
#     print("prime")
# else:
#     print("Not prime")

# num=int(input("enter:"))
# sum=0
# for i in range(1,num//2+1):
#     if num%i==0:
#         sum+=i
# if sum==num:
#     print("Perfect number")
# else:
#     print("Not perfect")

# limak,bob=map(int,input("enter:").split())
# year=0
# while  limak<=bob:
#     limak=limak*3
#     bob=bob*2
#     year+=1
# print("Years taken:",year)

# num=int(input("enter:"))
# rev=0
# while num>0:
#     d=num%10
#     rev=rev*10+d
#     num//=10
# print("reverse:",rev)

# num=int(input("enter:"))
# while num>9:
#     sum=0
#     while num>0:
#         d=num%10
#         sum+=d
#         num//=10
#     num=sum
# if num==1:
#     print("Magic number")
# else:
#     print("Not magic")

# num=int(input("enter:"))
# # temp=num
# # sum=0
# # while num>0:
# #     fact=1
# #     d=num%10
# #     for i in range(1,d+1):
# #         fact*=i
# #     sum+=fact
# #     num=num//10
# # if sum==temp:
# #     print("Strong number")
# # else:
# #     print("Not strong")

# num=int(input("enter:"))
# temp=num
# sq=num*num
# dc=0
# while temp>0:
#     dc+=1
#     temp//=10
# po=10**dc
# if num==sq%po:
#     print("Automorphic")
# else:
#     print("Not automorphic")

# num=int(input("enter:"))
# if num & num-1==0:
#     print("power of two")
# else:
#     print("Not power of two")
#
# num=int(input("enter:"))
# while num:
#     if num==1:
#         print("power of two")
#         break
#     if num%2==0:
#         num=num//2
#     elif num%2!=0:
#         print("Not power of two")
#         break

# num=int(input("enter:"))
# i=int(input("enter:"))
# if num&1<<i!=0:
#     print("Set bit")
# else:
#     print("Not a setbit")

# def xor(num):
#     if num%4==0:
#         return num
#     elif num%4==1:
#         return 1
#     elif num%4==2:
#         return num+1
#     elif num%4==3:
#         return 0
# l,r=map(int,input("enter:").split())
# a=xor(r)
# b=xor(l-1)
# print(a^b)


# n=4
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()


# n=4
# for i in range(n):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

# n=4
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# n=4
# k=1
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(k,end=" ")
#             k+=1
#     print()

# n=4
# for i in range(n):
#     for j in range(0,n-i-1):
#         print(" ",end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

# n=4
# for i in range(n):
#     for j in range(0,i+1):
#         print(" ",end=" ")
#     for j in range(0,n-i):
#         print("*",end=" ")
#     print()