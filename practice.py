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

# #조건문
#날씨
# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

#기온
# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨예요")
# elif 0 <= temp  <10 :
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요.나가지 마세요")

#반복문 for문
# for waiting_no in range(1,6): # 1,2, 3, 4, 5
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0},커피가 준비되었습니다.".format(customer))

#반목문 while문
# customer = "토르"
# index =5
# while index >= 1:
#     print("{0},커피가 준비 되었습니다. {1} 번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

#문한루프
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0},커피가 준비되었습니다.호출 {1} 되었습니다.".format(customer,index))
#     index += 1

#조건이 충족됬을때 루프 탈출
# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{0},커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게되세요? ")

#continue 는 밑에 문장을 실행하지 않고 계속 다음 문장을 실행 break는 바로 반복문을 끝냄
# absent = [2, 5] #결석
# no_book =[7]#책을 깜빡했음
# for student in range(1, 11): #1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지.{0}는 교무실로 따라와".format(student))
#         break
#     print("{0},책을 읽어봐".format(student))

# 한 줄 for
#출석번호가 1 2 3 4 , 앞에 100을 붙이기로 함 -? 101, 102, 103, 104, 105
# students= [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변화
# students = ["Iron man","Thor", "I am groot"]
# students = [len(i) for i in students] #len은 문자열의 길이를 설명함
# print(students)

#학생 이름을 대문자로 변환
# students = ["Iron man","Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)


# Quiz) 당신은 Cocoa 서비스를 이요하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을때, 총 탑승 승객 수를 구하는 프로그램을 작성하시요
# 조건1 : 승객별 운행소요 시간은 5분~50분 사이의 난수로 정해집니다.
# 조건2: 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [o] 1번째 손님 (소요시간 :15분)
# [ ]2번째 손님 (소요시간 : 50분)
# [o]3번째 손님 (소요시간:5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승승객 : 2분

# from random import *
# cnt = 0 #총 탑승 승객수
# for i in range(1,51): #1~50이라는 수(승객)
#     time = randrange(5,51)
#     if 5<= time <= 15: #5분 ~ 15분 이내의 손님(매칭성공), 탑승 승객 수 증가 처리
#         print("[o]{0}번째 손님(소요시간 : {1}분)".format(i,time))
#         cnt += 1
#     else:#매칭 실패한 경우
#         print("[ ]{0}번째 손님(소요시간 : {1}분)".format(i,time))

# print("총 탑승 승객 : {0}분".format(cnt))


#함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance,money): #입금
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
#     return balance + money

# def withdraw(balance, money): #출금
#     if balance >= money: #잔액이 출금보다 많은면
#         print("출금이 완료되었습니다.잔액은 {0} 원 입니다.".format(balance-money))
#         return balance-money
#     else:
#         print("출금이 완료되지 않았습니다.잔액은 {0} 원 입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money): #저녁에 출금
#     commission = 100 #수수료100원
#     return commission, balance - money - commission

# balance = 0 #잔액
# balance = deposit(balance,1000)
# #balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1}원 입니다.".format(commission, balance))

# 함수 기본값
# def profile(name,age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어{2}".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

#같은 학교 같은 학년 같은 반 같은 수업
# def profile(name, age=17, main_lang="파이썬"):
#      print("이름 : {0}\t나이 : {1}\t주 사용 언어:{2}".format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# def profile(name,age, main_lang):
#         print(name, age, main_lang)

# profile(name = "유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")
#가변인자
# def profile(name,age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name,age,*language):
#      print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#      for lang in language:
#         print(lang, end="")
#      print()

# profile("유재석", 20, "python", "java", "c", "c++", "c#", "javascript")
# profile("김태호", 25, "kotlin", "swift")

#전역변수

# gun = 10

# def checkpoint(soldiers):
#     global gun #전역 공간에 있는 gun사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun
# print("전체 총 : {0}".format(gun))
# #checkpoint(2)# 2명이 경계근무 나감
# gun = checkpoint_ret(gun,2)
# print("남은 총 : {0}".format(gun))

# Quiz) 표준 체중을 구하는 프로그램을 작성하시오
# *표준체중: 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#     *함수명 : std_weight
#     *전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력예제)
# 키 175cm 남자의 표준 체중은 67.38kg입니다.

#내답 (틀림)
# height = 100
# man = height*height*22
# girl = height*height*21

# def std_weight(height,gender):  
#     height = height /= 10
#     return height, gender

# print("키{0}\t {1}의 표준체중은{2}입니다.".format(height,gender,std_weight))

# #정닶
# def std_weight(height,gender):  #키는 m 단위 (실수), 성별 "남자"/"여자"
#     if gender == "남자":
#         return height * height * 22
#     else :
#         return height * height * 21

# height = 175 #cm단위
# gender = "남자"
# weight = round(std_weight(height / 100, gender),2)
# print("키 {0}cm {1}의 표준체중은 {2}kg입니다.".format(height, gender, weight))

#표준 입출력
# print("Python", "Java", sep=",", end="?") #end 는 문장의 끝부분을 ?로 바꾸어달라
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) #표준출력으로 찍히는것 ->로그처리를 따로 할때 표준처리로 해서 크게상관없는데
# print("Python", "Java", file=sys.stderr) #에러 같은경우는 따로 로깅을 확인을해서 프로그램코드를 수정

#시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")  #왼쪽으로정렬을 하는데 총 8칸의 공간을 확보 #score는 오른쪽4칸

#은행 대기순번표
#001,002,003,...
# for num in range(1,21):
#     print("대기번호:" + str(num).zfill(3)) #zfill 뒤에 숫자만큼의 크기를 값을 0으로 채운다.

#표준입력
#answer = input("아무 값이나 입력하세요 : ")
# answer = 10
# print(type(answer))
#print("입력하신 값은 " +answer+ "입니다.")  #!!주의 : 사용자 입력을 통해서 받게되면 항상 문자열 형태로 저장됨

# #다양한 출력 포멧
# #빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일때는 +표시 음수일때는 -로표시
# print("{0: >+10}".format(500))
# print("{0: >10}".format(-500))
# #왼쪽정렬을 하고 빈칸을 밑줄로 채우기
# print("{0:_<10}".format(500))
# # 3자리마다 콤마를 찍어주기
# print("{0:,}".format(100000000))
# # 3자리마다 코마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(100000000))
# print("{0:+,}".format(-100000000))
# # 3자리마다 콤마를 찍어주기,부호도 붙이고, 자릿수도 확보하고 #돈이 낳으면 행복하니 빈자리는^로 채우기
# print("{0:^<+30,}".format(100000000))
# #소수점 출력
# print("{0:f}".format(5/3))
# # 소수점을 특정 자리수 까지만 표시(소수점 3째자리에서 반올림)
# print("{0:.2f}".format(5/3))


#파일 입출력

#파일 쓰기
# score_file = open("score.txt", "w", encoding="utf=8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

#파일 덮어쓰기
# score_file = open("score.txt", "a", encoding="utf=8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

#파일 읽기
# score_file = open("score.txt", "r", encoding="utf=8")
# print(score_file.read())
# score_file.close()

#파일 읽기2
# score_file = open("score.txt", "r", encoding="utf=8")
# print(score_file.readline(), end="") #줄별로 읽기, 한 줄 읽고 커서는 다음주로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

#파일 읽기3
# score_file = open("score.txt", "r", encoding="utf=8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

#파일 읽기4
# score_file = open("score.txt", "r", encoding="utf=8")
# lines =score_file.readlines() #list 형태로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()

#pickle
# import pickle
# profile_file = open("profile.pickle","wb")
# profile = {"이름":"박병수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #proflie에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file)  #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

#with - close가 필요없음
# import pickle

# with open("profile.pickle", "rb")as profile_file:
#     print(pickle.load(profile_file))

#with 을 이용한 일반적인 파일생성
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open ("study.txt","r", encoding="utf8") as study_file:
#     print(study_file.read())

# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야합니다. 

# -X 주차 주간보고-
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건 : 파일명은 '1주차.txt','2주차.txt',...와 같이 만듭니다.

#with open("i 주차.txt","w", encoding="utf8") as report_file:

# #내답 까비 거의다 맞았는데 ㅠㅠ 
# for i in range(1,51):
#     report_file = open("i 주차.txt", "w", encoding="utf=8")
#     print("-i 주차 주간보고-", file=report_file)
#     print("부서 : ", file=report_file)
#     print("이름 : ", file=report_file)
#     print("업무요약 : ", file=report_file)
#     report_file.close()

#모범답안
# for i in range(1,51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("-{0} 주차 구간보고-".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")

#class <- 보통 붕어빵틀이라고 비유함 틀만 있으면 무한생산가능

# #마린 : 공격 유닛, 군인.총을 쓸 수 있음
# name="마린" #유닛의 이름
# hp = 40 #유닛의 체력
# damage = 5 #유닛의 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp,damage))

# #탱크 : 공격 유닛, 탱크.포를 쏠 수 있는데, 일반모드/시즈모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

# def attack(nmae, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력 {2}]".format(\
#         name, location, damage))
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# #레이스 : 공중 유닛, 비행기.클로킹(상대에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# #마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

#메소드
# #일반 유닛
# class Unit:
#     def __init__(self, name, hp): #damage):
#         self.name = name
#         self.hp = hp
#         #self.damage = damage
#         #print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         #print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
# #공격유닛
# class AttackUnit(Unit): #class AttackUnit 안에 Unit를 상속받음
#     def __init__(self, name, hp, damage):
#         # self.name = name
#         # self.hp = hp
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))


# #매딕 : 의무병

# #파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# #공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)


#다중상속

# #일반 유닛
# class Unit:
#     def __init__(self, name, hp): #damage):
#         self.name = name
#         self.hp = hp
#         #self.damage = damage
#         #print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         #print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
# #공격유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         # self.name = name
#         # self.hp = hp
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))


# # 드랍쉽 : 공중유닛, 수송기. 마린/파이엇뱃/탱크 등을 수송 공격불가
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):   #다중상속함
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

# #발키리 : 공중 공격유닛. 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")



# #메소드 오버라이딩

# #일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed): #damage):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
    
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다.[속도 {2}]".format(self.name, location, self.speed))
#         #self.damage = damage
#         #print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         #print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
# #공격유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         # self.name = name
#         # self.hp = hp
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))


# # 드랍쉽 : 공중유닛, 수송기. 마린/파이엇뱃/탱크 등을 수송 공격불가
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):   #다중상속함
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) #지상 스피드는 0으로처리
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중유닛이동]")
#         self.fly(self.name, location)

# #pass
# #건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#       # Unit.__init__(self, name, hp , 0)
#        super().__init__(name, hp, 0)
#        self.location = location



# #스타크래프트 

# from random import *


# #일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed): #damage):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))
    
#     def move(self, location):
#         print("{0} : {1} 방향으로 이동합니다.[속도 {2}]".format(self.name, location, self.speed))
#         #self.damage = damage
#         #print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         #print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

    
# #공격유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         # self.name = name
#         # self.hp = hp
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력 {2}]"\
#             .format(self.name, location, self.damage))

# #마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     #스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력10감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다.(HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


# #탱크
# class Tank(AttackUnit):
#     #시즈모드 : 탱크를 지상에 고정시켜, 더높은 파워로 공격 가능. 이동불가
#     seize_developed = False #시즈모드 개발여부

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return

#         #현재 시즈모드가 아닐때 -> 시즈모드
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True


#         #현재 시즈모드일 -> 시즈모드 해제
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False


# # 드랍쉽 : 공중유닛, 수송기. 마린/파이엇뱃/탱크 등을 수송 공격불가
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):   #다중상속함
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) #지상 스피드는 0으로처리
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         self.fly(self.name, location)

# #레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False #클로킹 모드 (해체 상태)

#     def clocking(self):
#         if self.clocked == True: #클로킹 모드 -> 모드 해제
#             print("{0} : 클로킹 코드 해제합니다.".format(self.name))
#             self.clocked = False
#         else: #클로킹 모드 해제 -> 모드 설정
#             print("{0} : 클로킹 코드 설정합니다.".format(self.name))
#             self.clocked = False

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다")

# def game_over():
#     print("Player : gg")#goodgame
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")



# # 실제 게임 진행
# game_start()

# #마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# #탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# #레이스 1기 생성
# w1 = Wraith()

# #유닛 일괄 관리(생성된 모든 유닛 append)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# #탱크 시즈몯 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 공격 모드 준비 ( 마린: 스팀팩, 탱크: 시즈모드, 레이스:클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit,Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()


# #전군 공격
# for unit in attack_units:
#     unit.attack("1시")


# #전군 피해

# for unit in attack_units:
#     unit.damaged(randint(5 ,20)) # 공격은 랜덤으로 받음 (5~20)

# #게임 종료
# game_over()




# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오
# (출력예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
# class House:
#     #매물초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     #매물 정보 표시
#     def show_detail(self):
#         print(self.location,  self.house_type, self.deal_type, self.price, self.completion_year)


# houses = []
# house1 =  House("강남", "아파트", "매매", "10억", "2010년")
# house2 =  House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 =  House("송파", "빌라", "월세", "500/50", "2000년")

# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()


#예외처리

# try:
#     print("나누기 전용 계산기 입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
#     # num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     # num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     #print("{0} / {1} = {2}".format(num1, num2 ,int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)


# 에러 발생시키기

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")


# #사용자 정의 예외처리
# class BigNumberError(Exception):
#     def __init__(self,msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 :{0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)



# #finally
# class BigNumberError(Exception):
#     def __init__(self,msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 :{0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")



# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올때는 ValueError로 처리
#         출력 메세지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생키기고 프로그램 종료
#         출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."


# [코드]
#내답
# class SoldOutError(Exception):
#      def __init__(self,msg):
#          self.msg = msg

#      def __str__(self):
#          return self.msg


# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작
# # try :
#     while(True):
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken : #남은 치킨보다 주문량이 많을때
#             raise ValueError
#             raise SoldOutError("남은 치킨 : {0}, 주문 할수 있는 치킨{1}".format(chicken, order))
#             print("재료가 부족합니다.")
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order


# except ValueError:
#      print("잘못된 값을 입력하였습니다.")
# except SoldOutError as err:
#      print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#      print(err)

#모법답안
# class SoldOutError(Exception):
#       pass
# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작
# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken : #남은 치킨보다 주문량이 많을때
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order

#         if chicken == 0:
#             raise SoldOutError


#     except ValueError:
#          print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break



#모듈
# import theater_module
# theater_module.price(3) #3명이서 영화 보러 갔을때 가격
# theater_module.price_morning(4) #4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5) #5명의 군인이 여화 보러 갔을때

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# price_soldier(7)

from theater_module import price_soldier as price