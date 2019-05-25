def insertion_sort(data):
    result = []
    for value in data:
        insert_value(result, value)
    return result

# 삽입 정렬의 핵심메커니즘은 각 데이터의 삽입 지점을 찾는 함수
# 아래는 극히 비효율적인 insert_value 함수로 입력 배열을 순차적으로 스캔

def insert_value(array, value):
    for i, existing in enumerate(array):
        if existing > value:
            array.insert(i, value)
            return
    array.append(value)

# insertion_sort와 insert_value를 프로파일하려고 난수로 구성된 데이터 집합을 생성하고, 프로파일러에 넘길 test 함수를 정의

from random import randint

max_size = 10 ** 4
data = [randint(0, max_size) for _ in range(max_size)]
test = lambda: insertion_sort(data)