# #10871
# x ,y = map(int,input().split())
# a = list(map(int,input().split()))
# for i in a :
#     if y > i:
#         print(i,end=" ")

# #2439
# n = int(input())
# for i in range(1 ,n+1):
#     print(" "*(n-i),end="")
#     print("*"*i)

# #2338
# n = int(input())
# for i in range(1 ,n+1):
#     for j in range(0,i):
#         print("*", end="")
#     print()

# #11021
# import sys
# n = int(input())

# for i in range(n):
#     x, y = map(int, sys.stdin.readline().rstrip().split())
#     print("Case #{0}: {1}".format(i+1,x+y))

# #11022
# import sys
# n = int(input())

# for i in range(n):
#     x, y = map(int, sys.stdin.readline().rstrip().split())
#     print("Case #{0}: {1} + {2} = {3}".format(i+1,x,y,x+y))

# #2742
# n = int(input())
# for i in range(n, 0, -1):
#     print(i)

# #2141
# n = int(input())
# for i in range(1 ,n+1):
#     print(i)

# #15552
# import sys
# n = int(input())

# for i in range(n):
#     x, y = map(int, sys.stdin.readline().rstrip().split())
#     print(x+y)

# #8393
# x = 0
# n = int(input())

# for i in range(1, n+1):
#     x += i 
# print(x)

# #10950
# n = int(input())

# for i in range(n):
#     x, y = map(int, input().split())
#     print(x+y)

#10952
# while True:
#     x , y =  map(int, input().split())
#     print(x+y)
#     if x==5 and y==2 :
#             break

#10951
# while True:
#     try:
#         x , y =  map(int, input().split())
#         print(x+y)
#     except:
#         break 

# 1110
# n = int(input())
# num = n
# count = 0
# while True:
#     a = num // 10
#     b = num % 10
#     c = (a + b) % 10
#     num = (b * 10) + c
#     count = count + 1
#     if(num == n):
#         break
# print(count)
          
    

