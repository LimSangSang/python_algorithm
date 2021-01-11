# 문제 : 8 X 8 좌표에 다음과 같은 두 가지 경우에만 움직일 수 있다.

# 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
# (1, 1)부터 시작하고 이동하면서 칸을 넘길 수는 없다.
# [이것이 코딩테스트다] 실전문제02, p.115

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row+step[0]
    next_column = column+step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <=8 and next_column>=1 and next_column<=8:
        result += 1

print(result)

# 풀이 및 해설: https://ddura2.tistory.com/27