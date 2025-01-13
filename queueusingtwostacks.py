class Queue:
    def __init__(self):
        self.stack_1=[]
        self.stack_2=[]
        
    def enqueue(self,data):
        self.stack_2.append(data)
        
    def dequeue(self):
        if not self.stack_1:
            while self.stack_2:
                self.stack_1.append(self.stack_2.pop())
        if self.stack_1:
            self.stack_1.pop()
    
    def display(self):
        if not self.stack_1:
            print(self.stack_2[0])
        else:
            print(self.stack_1[-1])
        
q=Queue()
no_op=int(input())
for i in range(no_op):
    n=input()
    s=n.split()
    if s[0]=='1':
        q.enqueue(int(s[1]))
    elif s[0]=='2':
        q.dequeue()
    else:
        q.display()
