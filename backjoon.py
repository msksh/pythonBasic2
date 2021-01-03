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
# n = int(input())

# for i in range(n):
#     s = input()

#     score = 0
#     cnt = 0
#     for j in range(len(s)):
#         if s[j]=="o":
#             cnt += 1
#             score += cnt
#         elif s[j]=="x":
#             score += 0
#             cnt = 0
#     print(score)


#4344
# C = int(input())
# for _ in range (C):
#     cnt = 0
#     score = list(map(int,input().split()))
#     N = int(score[0])
#     avg = sum(score[1:])/N
#     for i in range (1, N+1):
#         if score[i] > avg :
#             cnt += 1
#     print("%.3f%%"%round(cnt/N*100,3))
#4673
# self_num = set(range(1, 10001))
# generated_num = set()
# for i in range(1, 10001):
#     for j in str(i):
#         i += int(j)
#     generated_num.add(i)
# self_num = self_num - generated_num
# for i in sorted(self_num):
#     print(i)
# 1065
# n = int(input())
# hansu = 0
# for i in range(1, n + 1):
#     if i < 100:
#         hansu += 1
#     else:
#         ns = list(map(int, str(i)))
#         if ns[0] - ns[1] == ns[1] - ns[2]:
#             hansu += 1
# print(hansu)

#11654번 아스키 코드
# a = input()
 
# print (ord(a))

#11720번
# a = int(input())
# n = list(input())
# sum = 0
# for i in n:
#     sum += int(i)
# print(sum)

#10809번 알바벳찾기
# S = str(input())
# Alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #a-z 리스트
# num = [-1 for i in range(26)] #-1로 구성된 리스트
# for i in range(len(S)): #입력된 단어에 있는 문자 갯수만큼 반복
#     for j in range(len(Alpha)):  #알파벳 갯수만큼 반복
#         if S[i] == Alpha[j]: #입력된 문자랑 알파벳이 같다면
#             if num[j] == -1: #처음 등장하는 위치를 아직 모른다면
#                 num[j] = i #해당 알파벳의 자리에 위치 넣는다
# for i in range(len(num)):
#     print(num[i], end=' ')

#2675번
# n = int(input())
# for _ in range(n):
#     cnt, word = input().split()
#     for x in word:
#         print(x*int(cnt), end='')  # end='' 옆으로 붙임
#     print()  # 줄넘김

#1157번
word = input().lower()
word_list = list(set(word))
cnt = []
for i in word_list:
    count = word.count(i)
    cnt.append(count)
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper())

