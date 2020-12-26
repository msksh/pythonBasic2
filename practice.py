'''
station = "인천공항" 
print(station+"행 열차가 들어오고있습니다.")
'''
'''
#연산자
print(1+1)#2
print(3-1)#2
print(2*5)#10
print(6/3)#2
print(2**3) #2^3=8
print(5%3) #나머지구하기 2
print(10%3) #1
print(5//3) #1
print(10//3) #3

print( 10 > 3) #True
print(4 >= 7)#False
print(10 < 3) #False
print(5 <= 5) #True

print(3 == 3)#true
print(4 == 2)#False
print(3+4 == 7) #True
print( 1!=3)#True
print(not(1!=3))#False

print((3>0) and (3<5)) #True
print((3>0)&(3<5)) #True

print((3>0) or (3<5)) #True
print((3>0)|(3<5)) #True

number =  2 + 3 *4 #14
print(number)
number = number + 2 #16
print(number)
number += 2 #18
print(number) 
number *= 2 #36
print(number) 
number /= 2 #18
print(number)
number -= 2 #16
print(number)
number %= 5 #1
print(number)
'''
'''
#숫자처리함수
print(abs(-5)) #5 절대값
print(pow(4, 2)) #4^2 = 4*4 =16 제곱
print(max(5, 12)) #12 최댓값
print(min(12, 5))#5 최솟값
print(round(3.14))#3 반올림
print(round(4.99))#5 반올림

from math import *
print(floor(4.99)) #내림. 4 
print(ceil(3.14)) #올림 4
print(sqrt(16)) #루트 4
'''
'''
#랜덤함수
from random import *

#print(random()) # 0.0~1.0 미만의 임의의 값 생성
#print(int(random()*10))  #0~10미만의 임의의 값 int : 소수점 제외
#print(random()*10) #0.0~10.0미만의 임의의 값 
#print(int(random()*10)+1)  #1~10미만의 임의의 값
#print(int(random()*10)+1)  #1~10미만의 임의의 값
#print(int(random()*10)+1)  #1~10미만의 임의의 값
#print(int(random()*10)+1)  #1~10미만의 임의의 값


#print(randrange(1, 46)) #1 ~ 45 미만의 임의의 값 생성
#print(randrange(1, 46)) #1 ~ 45 미만의 임의의 값 생성
#print(randrange(1, 46)) #1 ~ 45 미만의 임의의 값 생성
#print(randrange(1, 46)) #1 ~ 45 미만의 임의의 값 생성
#print(randrange(1, 46)) #1 ~ 45 미만의 임의의 값 생성
#print(randrange(1, 46)) #1 ~ 45 미만의 임의의 값 생성

print(randint(1, 45)) #1~45이하의 임의의값 생성
print(randint(1, 45)) #1~45이하의 임의의값 생성
print(randint(1, 45)) #1~45이하의 임의의값 생성
print(randint(1, 45)) #1~45이하의 임의의값 생성
print(randint(1, 45)) #1~45이하의 임의의값 생성
print(randint(1, 45)) #1~45이하의 임의의값 생성
'''
'''
#퀴즈 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다. 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로
#하기로 했습니다. 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오

#조건1 : 랜덤으로 날짜를 뽑아야함
#조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
#조건3 : 매월1~3일은 스터디 준비를 해야함으로 제외

#(출력문 예제)
#오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

from random import *
offlinestudy = randint(4,28)

print("오프라인 스터디 모임 날짜는 매월" ,offlinestudy,"일로 선정되었습니다.")
'''


#문자열
#sentence = '나느 소년입니다'
#print(sentence)
#sentence2 = "파이썬은 쉬워요"
#print(sentence2)
#sentence3 = '''
#나는 소년이고,
#파이썬은 쉬워요
#'''
#print(sentence3)



'''
#슬라이싱
jumin = "990120-1234567"

print("성별:" + jumin[7])
print("연:" + jumin[0:2]) # 0 부터 2 직전까지 (0,1)
print("월 : " + jumin[2:4])
print("일 :" + jumin[4:6])
print("생년월일 :" + jumin[:6]) #처음부터 6 직전까지
print("뒤 7자리:" + jumin[7:])
print("뒤 7자리 (뒤에서부터):" + jumin[-7:]) #맨 뒈엇 7번째 끝까지
'''
 
'''
#문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)

print(python.find("Java"))
#print(python.index("Java"))
print("hi")

print(python.count("n"))
'''


#문자열 포멧
#방법1
#print("나는 %d살입니다." %20)
#print("나는 %s을 좋아해요." % "파이썬")
#print("Apple 은 %c로 시작해요." % "A")
# %s 각 출력을 할수 있다.
#print("나는 %s 살입니다." %20)
#print("나는 %s색과 %s색을 좋아해요" % ("파란","빨간"))


#방법2
#print("나는 {}살 입니다.".format(20))
#print("나는 {}색과 {}색을 좋아해요" .format("파란","빨간"))
#print("나는 {0}색과 {1}색을 좋아해요" .format("파란","빨간"))
#print("나는 {1}색과 {0}색을 좋아해요" .format("파란","빨간"))

#방법3
#print("나는 {age}살이며,{color}색을 좋아해요".format(age=20,color="빨간"))
#print("나는 {age}살이며,{color}색을 좋아해요".format(color="빨간",age=20))

#방법4
#age = 20
#color = "빨간"
#print(f"나는 {age}살이며,{color}색을 좋아해요")


#\n : 줄바꿈
#print("백문이 불여일견 \n 백견이 불여일타")

#\" \' : 문장 내에서 따옴표.
#저는 "나도코딩" 입니다.
#print('저는 "나도코딩" 입니다.')
#print("저는 \"나도코딩\" 입니다.")

# \\ : 문장내에서\
#print("C:\\Users\\kim\\Desktop\\PythonWorkSpace")

# \r : 커서를 맨 앞으로 이동 Apple : str 이동
#print("Red Apple\rPine")


# \b : 백스페이스 (한 글자 삭제)
#print("Redd\bApple")

# \t : 탭
#print("Red\tApple")




#Quiz)사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
#예)http://naver.com
#규칙1 : http://부분은 제외 => naver.com
#규칙2 : 처음 만나는점(.)이후  부분은 제와 => naver
#규칙3 : 남는 글자중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#예)생성된 비밀번호: nav51!


#url = "http://naver.com"
#my_str = url.replace("http://","") #규칙1
#my_str = my_str[:my_str.index(".")] #규칙2
#my_syr[0:5]->0~5직전까지.(0,1,2,3,4)
#password =my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" #규칙3
#print("{0}의 비밀번호는 {1}입니다.".format(url,password))

#리스트[]

#지하철 칸별로 10명, 20명, 30명
#subway = [10 ,20 ,30]
#print(subway)


#subway = ["유재석", "조세호", "박명수"]
#print(subway)

#조세호씨가 몇 번째 칸에 타고 있는가?
#print(subway.index("조세호"))

#하하씨가 다음 정류장에서 다음 칸에 탐
#subway.append("하하")
#print(subway)

#정형돈씨를 유재석씨와 조세호씨 사이에 
#subway.insert(1,"정형돈")
#print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
#print(subway.pop())
#print(subway)

#print(subway.pop())
#print(subway)

#print(subway)
#print(subway.pop())

# 같은 이름의 사람이 몇 명 있는지 확인
#subway.append("유재석")
#print(subway)
#print(subway.count("유재석"))

# 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# #순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

#모두 지우기
# num_list.clear()
# print(num_list)

#다양한 자료형 함께 사용
#num_list=[5,2,4,3,1]
#mix_list=["조세호", 20 , True]
#print(mix_list)

#리스트 확장
#num_list.extend(mix_list)
#print(num_list)

#사전
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))
# print(cabinet[5])
# print(cabinet.get(5))
# print(cabinet.get(5, "사용 가능"))
# print("hi")

#print(3 in cabinet) #True
#print(5 in cabinet) #False

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])


# #새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# #간 손님
# del cabinet["A-3"] 
# print(cabinet)

# # key 들만 출력
# print(cabinet.keys())

# # value 들만 출력
# print(cabinet.values())

# # key, value 쌍으로 출력
# print(cabinet.items())

# #목욕탕 폐점
# cabinet.clear()
# print(cabinet)

# 튜플
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name , age, hobby) =( "김종국", 20, "코딩")
# print(name,age,hobby)

# 집합 (set)
# 중복 안됨, 순서없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합(java와 python을 모두 할수 있는 개발자)
# print(java&python)
# print(java.intersection(python))

# #합집합(java 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# #차집합(java는 할수 있지만python은 할 줄 모른느 개발자)
# print(java - python)
# print(java.difference(python))

# #python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊었어요
# java.remove("김태호")
# print(java)

# 자료구조의 변경
# 커피숍
# menu = {"커피","우유","주스"}
# print(menu,type(menu))

# menu = list(menu)
# print(menu,type(menu))

# menu = tuple(menu)
# print(menu,type(menu))

# menu =set(menu)
# print(menu,type(menu))

# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추천 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복불가
# 조건3: random 모듈의 shuffle과 sample 을 활용
# (출력 예제)
# --당첨자 발표--
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# --축하합니다--

# (활용예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))

#내가한답 틀림 ㅠㅠ
# from random import *
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# #print(lst)
# shuffle(lst)
# print(sample(lst,1))


#정답 ------------------
# from random import *
# users = range(1,21)
# users = list(users)
# #print(users)
# shuffle(users)
# winners = sample(users ,4) #4명 중에서 1명은 치킨, 3명은 커피
# print("--당첨자 발표--")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("--축하합니다--")