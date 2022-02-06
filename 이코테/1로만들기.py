# 다이나믹 프로그래밍
# 못풀음
x = int(input())

# 앞서 계산된 결과(횟수)를 저장
d = [0] * 30001

# 다이나믹 프로그래밍 진행 (보텀업)
for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    # 1을 빼고 시작하는 이유 : 다음에 계산할 나누기에서 '1을 뺀 값'과 비교하여 횟수가 작은 것으로 교체될 것이기 때문에
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1) # 1을 더하는 이유 : d는 계산 횟수이기 때문, d[i]에 더하지 않는 이유는 위에서 1을 뺄 때 더해줬기 때문
    # 현재의 수가 3로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])