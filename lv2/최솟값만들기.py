# 문제 설명
# 길이가 같은 배열 A, B 두개가 있습니다. 각 배열은 자연수로 이루어져 있습니다.
# 배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다. 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. (단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.)

def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]


    return answer


# a.sort() / a.sorted(reverse=True) => a를 정렬함
# sorted(a) / sorted(a, reverse=True) => a를 정렬해서 새로운 객체로 반환함
# sorted(a, key=func) func 함수에 a의 원소를 넣어서 대소비교