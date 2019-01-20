
# content = 'i do not agree'


#indexing
# print(content[5])

# length
# print(len(content))

# test = "aaaa"+"bbbb"

# print(test)

#문자열 더하기 & 문자열 포멧

# name = "seongbin"
# age = 30

# # 문자열 더하기
# message = "your name is" +name+" and age is "+str(age)

# # Format 이용
# messageFormat = "your name is {0} and age is {1}".format(name,age)

# print(messageFormat)


# pie = 3.141592

# pieFormat = "pie = {0:0.3f}".format(pie)
# #pieFormat = "pie = {0:<10.3f} okay".format(pie) 왼쪽부터 정렬.
# print(pieFormat)

#가운데 왼쪽 오른쪽 정렬

# stars = "***"

# #starsFormat = "{0:>10}".format(stars)
# #print(starsFormat)

# print("{0:>10".format(stars))
# print("{0:<10".format(stars))
# print("{0:^10".format(stars))

#문자열 포멧 예시

# users = [("seongbin",0), ("jin", 100000000000), ("joi",24562)]

# message = "Hi! {0:15}, This is your balance {1:10}"

# for user in users:
#     name = user[0]
#     balance = [1]
#     print(message.format(name,balance))

#기타 문자열 함수들

# content = "banana banana orange banana apple"

#count banana 개수 확인
#print(content.count("banana"))

#find 찾고싶은 문자열의 index 가져오기
# print(content.find("orange"))

#index (find와 같다.)

# print(content.index("banana"))
# print(content.index("orange"))

#join 문자열 배열에 구분점을 넣어서 하나의 문자열로 변경

# char = ","
# names = ["seongbin", "jack","jin"]

# print(names)
# print(char.join(names))

#대문자 소문자
# englishName = "Lucas"

# print(englishName)

# print(englishName.upper())

# print(englishName.lower())

# #공백제거 strip(lstrip, rstrip , strip)
# message = "     hi my name is lucas         "

# print(message+".")
# print(message.lstrip()+".")
# print(message.rstrip()+".")
# print(message.strip()+".")

#replace 문자열에서 부분 문자열 변경

# content = "banana is good"

# print(content)
# newContent = content.replace("banana","orange")
# print(newContent)


#split
# arr = [1,2,3,4,5,6,7]
# newArr = arr[1:5]
# print(newArr)


# message = "hello user! you need a python"
# print(message[6:10])


