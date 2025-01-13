def twoStacks(maxSum, a, b):
    x, y , current_s, count = 0,0,0,0
    
    while x<len(a) and current_s +a[x]<= maxSum:
        current_s+=a[x]
        x+=1
        count+=1
        
    max_count=count
    
    while y <len(b) and (x>0 or current_s + b[y] <=maxSum):
        current_s +=b[y]
        y+=1
        count+=1
        
        while current_s> maxSum and x>0:
            x-=1
            current_s-=a[x]
            count-=1
        
        if current_s<=maxSum:
            max_count=max(max_count, count)
            
    return max_count

d=int(input())
result=[]

for _ in range(d):
    x, y, maxSum= map(int, input().split())
    a= list(map(int,input().split()))
    b= list(map(int, input().split()))
    result.append(twoStacks(maxSum, a, b))
    
for results in result:
    print(results)