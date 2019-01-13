
"""
인덱싱과 슬라이싱
"""

# userlist = [1,2,3,4,5,6]
# #inde   0  1  2  3  4
# ages = [11,22,31,43,51]

# print(ages[0]) #첫번쨰 요소 인덱싱(출력)
# print(ages[-1]) #마지막 요소 인덱싱(출력)

# #슬라이싱은 기존 배열로부터 부분 배열을 만드는 작업.

# subAges = ages[1:2] #슬라이싱 #index. [:]의 뜻은 두번째껏은 포함하고 세번째껏은 포함하지 않는다.

# print(ages[1:3])

# print(ages[:]) #[:] :좌우로 입력하지 않으면 처음부터 끝까지 (fromTwoToLast)


"""배열 더하기, 배열 곱하기, 배열 길이(갯수) 확인
"""

# arr1 = [1,2,3]
# arr2 = [4,5,6]
# arr = arr1+arr2 #배열합침 (배열이 합쳐서 출력)
# print(arr)

# print(arr1 * 3) #반복하기 (배열이 여러번 반복되서 출력)

# numberOfArr = len(arr1) #arr1번의 []안에 갯수 확인
# print(numberOfArr)

"""
배열 수정 및 삭제
"""

# arr = [1,2,4,4,5,6,7]

# arr[2] = 3 #수정하는것. 1,2,4,4,5,6,7 에서 2다음 3으로 수정하고 싶을 때.

# print (arr)

# del arr[2] #삭제하는것. 1,2,4,4,5,6,7 에서 2다음 4숫자를 삭제 하고 싶을 때.

# print(arr)

"""
배열 append
"""

# arr = [1,2,3,4,5]

# arr.append(6) #배열뒤에 추가. 1,2,3,4,5 뒤에 6을 추가 하고 싶을 때.

# print(arr)

"""
배열 sort , reverse
"""

# arr = [5,4,7,2,1]

# arr.sort() #배열의 순서를 앞에서 부터정렬 하고 싶을 때.

# print(arr) 

# arr.reverse()#배열의 순서를 뒤에서 부터 정리하고 싶을 때.

# print(arr)

"""
배열 index, insert, remove
"""

# arr = [2,1,7,4,8,5,6,99] #반복되는 숫자는 추가됨. 삭제는 앞에서부터 삭제됨.

# print(arr.index(7)) #index는 배열의 몇 번째에 있는지 알려줌.

# arr.insert(3,99) #insert는 (3,99) 4번째 자리에 99를 추가하는 것.

# print(arr)

# arr.remove(99) #배열의 원하는 숫자를 지우는 기능. 99가 삭제됨.

# print(arr)

"""
배열 pop, count, extend
"""

# arr = [1,2,3,4,5,6,3,3]

# # print(arr.pop()) #배열에 pop()하면 배열에서 마지막 숫자를 꺼낼 수 있음. (last = arr.pop()로도 할수 있음.)

# # print(arr)

# count = arr.count(3) #배열안에 3이라는 숫자가 몇개 있는지 알려줌. (갯수)
# print("3의 개수"+ str(count))
# count = arr.count(8)
# print("8의 개수" + str(count))


# print("현재배열 : " +str(arr))
# arr.extend([1,2,3,4])
# print("extend이후 배열" + str(arr))
