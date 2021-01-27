#!/usr/local/bin/python3
#
#
# score = int(input())
#
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")
#
# #백준문제
# x ,y = map(int,input().split())
# a = list(map(int,input().split()))
# for i in a :
#     if y > i:
#         print(i,end=" ")
#
#
#
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs = []
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
#
#         # 팰린드롬 여부 판별
#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():
#                 return False
#
#         return True
#
# import collections
# from typing import Deque
#
#
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # 자료형 데크로 선언
#         strs: Deque = collections.deque()
#
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
#
#         while len(strs) > 1:
#             if strs.popleft() != strs.pop():
#                 return False
#
#         return True
#
#
# from typing import List
#
#
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         left, right = 0, len(s) - 1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1

# 스택 구현 예제
# stack=[]
# # 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()
#
# print(stack[::-1]) #최상단 원소부터 출력
# print(stack) #최하단 원소부터 출력

# # 큐 구현 예제
# from collections import deque
# #큐 구현을 위해 deque 라이브러리 사용
# queue = deque()
#
# # 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()
#
# print(queue) # 먼저 들ㅇ러온 순서대로 출력
# queue.reverse() #역순으로 바꾸기
# print(queue)# 나중에 들어온 원소부터 출

# 팩토리얼 구현 예제
# 반복적으로 구현한 n!
# def factorial_iterative(n) :
#     result = 1
#     # 1 부터 n 까ㅣ의 수를 차례대로 곱하기
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# # 재귀적으로 구현한 n!
# def factorial_recursive(n):
#     if n <= 1:# n이 1이하인 경우 1을 반함
#         return 1
# # n! = n * (n-1)!를 그대로 코드로 작성하기
#     return n * factorial_recursive(n-1)
# # 각각의 방식으로 구현한 n! 출력(n=5)
# print('반복적으로 구현:', factorial_iterative(5))
# print('재귀적으로 구현:', factorial_iterative(5))

# dfs 소스코드 예제
# dfs 매서드 정의
# def dfs(graph, v, visited):
# # 현재 노드르르 방문처리
#     visited[v] = True
#     print(v, end='')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
# # 각 노드가 연결된 정보를 표현(2차원 리스트)
# graph = [
# [],
# [2, 3, 8],
# [1, 7],
# [1, 4, 5],
# [3, 5],
# [3, 4],
# [7],
# [2, 6, 8],
# [1, 7]
# ]
# # 각 노드가 방문된 정보를 표현(1차원리스트)
# visited = [False] * 9
# # 정의된 dfs 함수 호출
# dfs(graph, 1, visited)

# from collections import deque
# # bfs 매서드 정의
# def bfs(graph, start, visited):
# # 큐 구현을 위해 deque 라이브러리 사용
#     queue = deque([start])
#     # 현재 노드를 방문 처리
#     visited[start] = True
#     # 큐가 빌 때까지 반복
#     while queue:
#         # 큐에서 하난의 원소를 뽑아 출력하기
#         v = queue.popleft()
#         print(v, end='')
#         # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
# # 각 노드가 연결된 정보를 표현(2차원 리스트)
# graph = [
# [],
# [2, 3, 8],
# [1, 7],
# [1, 4, 5],
# [3, 5],
# [3, 4],
# [7],
# [2, 6, 8],
# [1, 7]
# ]
# # 각 노드가 방문된 정보를 표현(1차원리스트)
# visited = [False] * 9
# # 정의된 dfs 함수 호출
# bfs(graph, 1, visited)

# <문제>음료수 얼려 먹기:문제설명
# N x M 크기의 얼음 틀이 있습니다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
# 구멍이 뚫려 있는 부분끼리 상,하 ,좌,우로 붙어있는 경우 서로 연결되어 있는 것으로 간주합니다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
# <답안>
# dfs로 특정 노드를 방문하고 연결된 모든 노드들도 방문
# def dfs(x, y):
#     # 주어진 범위를 벗어나는 경우에는 즉시 종료
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     # 현재 노드를 아직 방문하지 않았다면
#     if graph[x][y] == 0:
#         # 해당 노드 방문 처리
#         graph[x][y] = 1
#         # 상, 하,좌, 우의 위치들도 모두 재귀적으로 호출
#         dfs(x - 1, y)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True
#     return False
#     # N,M을 공백을 기준으로 구분하여 입력 받기
# n, m = map(int, input().split())
#
# # 2차원 리스트이ㅡ 맵 정보 입력 받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
# # 모든 노드(위치)에 대하여 음료수 채우기
# result = 0
# for i in range(n):
#     for j in range(m):
#         현재 위치에서 DFS 수행
#         if dfs(i, j) == True:
#             result += 1
# print(result) #정답 출력


# <문제>미로탈출:문제설명
# 성훈이는 N x M 크기의 직사각형 형태의 미로에 갇혔습니다.미로에는 여러마리의 괴물이 있어 이를 피해 탈출해야합니다.
# 성훈이의 위치는 (1,1)이며 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수있습니다. 이때 괴물이 있는 부분은 0으로 ,괴물이 없는 부분의 1로 표시되어 있습니다. 미로는 반드시 탈출할 수 있는 형태로 제시됩니다.
# 이때 성훈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요.칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.

# <답안예시>
# bfs 소스코드 구현
# def bfs(x,y):
#     # 큐 구현을 위해 deque 라이브러리 사용
#     queue = deque()
#     queue.append((x, y))
#     # 큐가 빌 때까지 반복하기
#     while queue:
#         x, y = queue.popleft()
#         # 현재 위치에서 4가지 방향으로의 위치 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 미로 찾기 공간ㅇ르 벗어난 경우 무시
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#                 # 벽인 경우 무시
#             if graph[nx][ny] == 0:
#                 continue
#                 # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#                 # 가장오른쪽 아래까지의 최단 거리 반환
#     return graph[n - 1][m - 1]
# from collections import deque
# # N,M을 공백을 기준으로 구분하여 입력 받기
# n,m = map(int, input().split())
# # 2차원 리스트의 맵 정보 입력 받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
# # 이동할 네가지 방향 정의 (상, 하, 좌, 우)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# # BFS를 수행한 결과 출력
# print(bfs(0,0))
