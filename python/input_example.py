
a = int(input("하나 숫자 입력"))
print(a, type(a))

a, b = map(int, input("두개 숫자 입력").split())
print(a, b, type(a), type(b))

arr = list(map(int, input("여러 숫자 입력").split()))

print(arr, type(arr))

# 몇 줄을 입력받을 지 모를 때 사용

answer3 = []
while True:
    try:
        temp = list(map(int, input().split()))
        answer3.append(temp)
    except:
        break

print(answer3, type(answer3))