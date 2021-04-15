import sys
from collections import deque

def solution():
    queue = deque()
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):

        s = sys.stdin.readline().rstrip().split(' ')

        if s[0] == 'push': queue.append(s[1])
        elif s[0] == 'pop':
            if len(queue) != 0:
                print(queue[0])
                queue.popleft()
            else: print(-1)
        elif s[0] == 'size': print(len(queue))
        elif s[0] == 'empty':
            if len(queue) == 0: print(1)
            else: print(0)
        elif s[0] == 'front':
            if len(queue)==0: print(-1)
            else: print(queue[0])
        elif s[0] == 'back':
            if len(queue)==0: print(-1)
            else: print(queue[-1])

solution()
