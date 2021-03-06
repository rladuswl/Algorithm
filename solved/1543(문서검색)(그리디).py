## 백준 1543 문서 검색
# 그리디, 브루트포스

'''replace 함수 사용
import sys

str = input()
word = input()

str = str.replace(word, '0')

print(str.count('0'))
'''

'''replace 함수 없이 풀기'''
import sys

str = input()
word = input()

cnt = 0
i = 0
'''방법1
while i <= (len(str)-len(word)):
    if str[i:i+len(word)] == word:
        i = i+len(word)
        cnt += 1
    else:
        i += 1
'''
'''방법2'''
while True:
    if i == len(str):
        break
    if str[i:i+len(word)] == word:
        i = i+len(word)
        cnt += 1
    else:
        i += 1

print(cnt)