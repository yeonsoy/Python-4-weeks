# 텍스트 묶음

var = '''
컴퓨터 과학과 수학에서 정렬 알고리즘(sorting algorithm)이란 원소들을 번호순이나 사전 순서와 같이 일정한 순서대로 열거하는 알고리즘이다. 효율적인 정렬은 탐색이나 병합 알고리즘처럼 (정렬된 리스트에서 바르게 동작하는) 다른 알고리즘을 최적화하는 데 중요하다. 또 정렬 알고리즘은 데이터의 정규화나 의미있는 결과물을 생성하는 데 흔히 유용하게 쓰인다. 이 알고리즘의 결과는 반드시 다음 두 조건을 만족해야 한다.

출력은 비 내림차순(각각의 원소가 전 순서 원소에 비해 이전의 원소보다 작지 않은 순서)이다;
출력은 입력을 재배열하여 만든 순열이다.
컴퓨터의 초창기에, 정렬 알고리즘은 연구하기에 대단히 매력적인 주제였다. 
'''

splited = var.split(' ')
frequency = {} # 단어 : 등장횟수

for word in splited:
    # frequency.setdefault(word, 0) 과 frequency[word] = frequency.get(word, 0)는 동일
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)