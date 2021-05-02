import sys
from collections import deque

n,k = map(int, sys.stdin.readline().rstrip().split())
queue = deque()
for i in range(1, n+1):
    queue.append(i)
result = '<'

while queue:
    # rotate(): 음수일 경우 왼쪽으로 회전, 양수일 경우 오른쪽으로 회전
    queue.rotate(-k+1) # -k 하면 k번째도 이동해버리므로 +1 해줌
    temp = queue.popleft()
    result += str(temp) + ', '
print(result[:-2]+'>')
