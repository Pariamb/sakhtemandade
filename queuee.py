# کلاس خطی
class queue :
    def __init__(self,k):
        self.k = k
        self.queue = [None] * k 
        self.front = -1
        self.rear = -1
    def disqueue (self):
        if self.front == -1 : 
            print("Empty")
        for i in range(self.front,self.rear+1):
            print(self.queue[i])
    def insqueue(self,data):
        if self.rear == -1 :
            self.front = 0 
            self.rear = 0
            self.queue[0] = data
        elif self.rear + 1  == self.k : 
            print("is full") 
            return
        else : 
            self.rear+=1
            self.queue[self.rear] = data
    def delqueue(self):
        if self.front == -1 : 
            print("Empty")
        elif self.front == self.rear : 
            t = self.queue[self.front]
            self.front = -1 
            self.rear = -1 
            return t 
        else : 
            t = self.queue[self.front]
            self.front += 1
            return t 
q = queue(3)
q.insqueue(2)
q.insqueue(1)
q.insqueue(4)
q.insqueue(1)
# q.disqueue()
# q.delqueue()
# q.disqueue()

#------------------------------------

# کلاس حلقوی 

class queue_c :
    def __init__(self,k):
        self.k = k
        self.queue = [None] * k 
        self.front = -1
        self.rear = -1
    def insqueue_c(self,data):
#وقتی پره
        if ((self.rear+1) % self.k == self.front):
            print("full")
#وقتی خالیه
        elif self.front == -1 :
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
#وقتی مقداری وجود دارد
        else :
            self.rear =(self.rear+1) % self.k 
            self.queue[self.rear] = data
    def delqueue_c(self):
        #هیچ عضوی وجود ندارد
        if self.front == -1 :
            print("Empty")
        #فقط یک عضو وجود دارد 
        elif self.front == self.rear :
            t = self.queue[self.rear]
            self.front = -1 
            self.rear = -1 
            return t
        #بیش از یک عضو وجود دارد 
        else : 
            t = self.queue [self.front]
            self.front = (self.front + 1) % self.k
            return t
    def disqueue_c(self):
        if self.front or self.rear == -1 :
            print("Empty")
        elif self.front <= self.rear :
            for i in range(self.front, self.rear+1):
                print(self.queue[self.front])
        else:
            for i in range(self.front,self.k):
              print(self.queue[i])
            for j in range(self.rear+1):
                print(self.queue[j])
            