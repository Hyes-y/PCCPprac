# 문제 설명
# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

# 제한 조건
# s는 길이 1 이상 200 이하인 문자열입니다.
# s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
# 숫자는 단어의 첫 문자로만 나옵니다.
# 숫자로만 이루어진 단어는 없습니다.
# 공백문자가 연속해서 나올 수 있습니다.

def solution(s):
    answer = ''
    
    for a in s.split(" "):
        answer += a.capitalize()
        answer += " "
    return answer[:-1]


def solution2(s):
    answer = ''
    
    isFirst = True
    for i in s:
        if i == " ":
            answer += i
            isFirst = True
        elif isFirst:
            answer += i.upper()
            isFirst = False
        else:
            answer += i.lower()
    
    return answer


# string.capitalize() : 맨 앞글자를 대문자로 변경
# string.title() : 알파벳 외 문자로 나눠져있는 영단어의 첫번째 글자를 대문자로 변경
# 공백이 연속해서 나올 경우에 대비해서 solution 2로 짰는데, 어차피 위에서 split할때 공백처리 ㅋㅋ