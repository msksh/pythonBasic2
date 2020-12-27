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



