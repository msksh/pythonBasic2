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
          
# #순열의 공식 (순열:nPc)
# from itertools import permutations
# data = ["A", "B", "C"]
# result = list(permutations(data,3))    #모든수열구하기
# print(result)

# #조합의 공식
# from itertools import combinations
# data = ["A", "B", "C"]
# result = list(combinations(data,2))    #2개를 뽑는 모든조합구하기
# print(result)


# #그리드 함수문제
# 거슬름돈문제:
# 당신은 음식점의 계산을 도와주는 점원입니다. 카운터에는 거스름돈으로 사용할
# 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정합니다.
# 손님에게 거슬러 주어야 할 돈이 N원 일때 거슬러 주어야 할 돈전의
# 최소 개수를 구하세요. 단,거슬러줘야 할 돈 N은 항상 10의 배수입니다.

#거스름돈:문제해결 아이디어
#최적의 해를 빠르게 구하기 위해서는 가장큰 화폐단위부터 돈을 거슬러주면 됩니다.
# N원 거슬러 줘야 할때, 가자 먼저 500원으로 거슬러 줄수 있을만큼 거슬러줍니다.
# 이후에 100원,50원,10원 짜리 차례대로 거슬러 줄수 있을만큼 거슬러 주면 됩니다.
# N = 1260원 일때의 예시 확인

# #코딩
# n = 1260
# count = 0
# array = [500, 100, 50, 10]

# for coin in array:
#     count += n // coin
#     n %= coin
# print(count)


#10818
# n = int(input())
# a = list(map(int,input().split()))
# print(max(a),min(a))

#2562번
# n = []
# for i in range(9):
#     n.append(int(input()))
# print(max(n))
# print(n.index(max(n))+1)

#2577번
# a = int(input())
# b = int(input())
# c = int(input())
# n = list(str(a*b*c))
# for i in range(10):
#     print(n.count(str(i)))

#3052번
# n = []
# for i in range(10):
#     n.append(int(input()) % 42)
# print(len(set(n)))

#1526번
# n = int(input())
# score = list(map(int,input().split()))
# m = max(score)
# ave = []
# for i in range(n):
#     ave.append(score[i]/m*100)
# print(sum(ave)/n)

#8959번
n = int(input())

for i in range(n):
    s = input()

    score = 0
    cnt = 0
    for j in range(len(s)):
        if s[j]=="o":
            cnt += 1
            score += cnt
        elif s[j]=="x":
            score += 0
            cnt = 0
        print(score)








