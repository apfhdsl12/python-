"""
논리식
"""

# name = input("이름을 입력하세요 : ")

# if name == "jin":
#     print( "외상값 내놔!")
# elif name == "jack":
#     print( "매일 먹던 거?")
# else:
#     print("처음 오셨어요?")

"""
체중 kg
신장 m 
bmi = 체중 / (신장*신장)

체중 80
신장 1.8

bmi 80 / (1.8*1.8)

25이하 정상
25초과는 비만


"""

# weight = float(input("체중을 입력하세요(kg) : "))
# height = float(input("신장을 입력하세요(m) : "))

# bmi = weight / (height*height)

# if bmi <= 25:
#     print("정상")
# else:
#     print("비만")



"""

while - 특정 신호 받을때 대기 , 무한정 반복 해야 될 때


for - Iterable하다는 것은 아이템을 하나씩 꺼낼 수 있다.                 

"""

#case 1.특정 신호 받을 때(외부로 부터 어떤 시그널을 받아야 될 때)



#message 가 "Hi" -> "Nice to meet you" 출력
#message 가 "Bye" -> "Bye!"를 출력하고 프로그램 종료
#message 가 "Hi 또는 Bye"가 아니다 그러면 message를 그래도 출력



# while True:
#     message = input("메시지를 입력하세요 : ")
#     if message.lower() == "hi":
#         print("Nice to meet you")
#     elif message.lower() == "bye":
#         print("Bye!")
#         break
#     else:
#         print(message)
        


# user = [{"name":"jack" },{"name":"joi"},{"name":"jin"}]

# for index in range(len(user)):
#     print("{0}번 유저는 {1}".format(index+1, user[index]["name"])) #1번째 유저는 {name}입니다.


# for i in range(1,10):
#     print(i)


# 구구단

# for i in range(1,10):
#     for j in range(1,10):
#         print("{0} X {1} = {2}".format(i,j,i*j))


# for i in range(5):
#     print("*****")

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()
