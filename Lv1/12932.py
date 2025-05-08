def solution(arr):
    answer = []
    arr.remove(min(arr))
    if not arr: #비어있을 때
        answer = [-1]
    else:
        answer = arr
    return answer