#가장 큰 수
def solution(numbers):

    numbers= list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = ''
    for num in numbers:
        answer += num

    return answer