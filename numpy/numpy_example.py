import numpy as np

# 1차원 배열 생성
a = np.array([1,2,3]) # [1,2,3]
# 2차원 배열 생성
b = np.array([[1,2,3],[4,5,6]]) # [[1,2,3],[4,5,6]]
print(b)
# 배열의 참조
print(b[0,0]) # 1
print(b[0][1]) # 2

# 배열의 형상
# 배열의 차원 및 항목 수는 형상(shape)으로 확인
# 형상이란 배열의 각 차원의 크기를 튜플로 표시한 것

print(a.shape) # (3,)
print(b.shape) # (2,3)

# ndim: 배열의 차원
print(a.ndim) # 1
print(b.ndim) # 2

# size: 배열의 요소들의 총 개수
print(a.size) # 3
print(b.size) # 6

# zeros(): 모든 요소가 0인 배열 생성
print(np.zeros(3)) # [0. 0. 0.]

# ones(): 모든 요소가 1인 배열 생성
print(np.ones((2,3))) # [[1. 1. 1.]
                      # [1. 1. 1.]]
# full(): 모든 요소가 지정한 값인 배열 생성
print(np.full((2,2), 9)) # [[9 9]
                         # [9 9]]

# eye(): 단위 행렬 생성
print("np.eye():", np.eye(2)) # [[1. 0.]
                 # [0. 1.]]

# arange(): 연속된 값의 배열 생성
print("arange():", np.arange(3)) # [0 1 2]

# arange(start, stop, step)
# start부터 stop 전까지 step만큼 증가하는 배열 생성
print("arange(start, stop, step): ",np.arange(1, 5, 0.5)) # [1.  1.5 2.  2.5 3.  3.5 4.  4.5]

# linspace(start, stop, num)
# start부터 stop까지 num개로 나눈 배열 생성
print("linspace():", np.linspace(0, 10, 5)) # [ 0.   2.5  5.   7.5 10. ]
print("linspace():", np.linspace(0, 4, 5)) #  [0. 1. 2. 3. 4.]
                        

# concatenate(): 2개의 배열 합치기
x = np.array([[1,2], [3,4]])
y = np.array([[5,6], [7,8]])
print("concatenate():", np.concatenate((x,y), axis=0)) # [[1 2]
                                                       # [3 4]
                                                       # [5 6]
                                                       # [7 8]]

print("concatenate():", np.concatenate((x,y), axis=1)) # [[1 2 5 6]
                                                       #  [3 4 7 8]]


