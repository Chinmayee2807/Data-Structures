def isBalanced(s):
    for char in s:
        if char not in ['(',')','{','}','[',']']:
            return 'Invalid input '
    stack=[]
    pair={'(':')','{':'}','[':']'}
    for char in s:
        if char in list(pair.keys()):
            stack.append(char)
        elif char in list(pair.values()):
            if not stack or pair[stack.pop()]!=char:
                return "NO"
    return "YES" if not stack else "NO"        
    

n=int(input())
for i in range(n):
    s=input()
    print(isBalanced(s))
