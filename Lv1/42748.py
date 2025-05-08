#K번째 수
def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k= command
        array_new = sorted(array[i-1:j])
        answer.append(array_new[k-1])
    return answer