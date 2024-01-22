class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linklist:
    def __init__(self) :
        self.head = None
    def display(self):
        t = self.head
        while (t != None) : 
            print(t.data,end=" --> ")
            t = t.next
        print("None")
    def addinstart(self,data):
        n = node(data)
        n.next = self.head
        self.head = n
    def addinend(self,data):
        n = node(data)
        t = self.head
        if t == None:
            self.head = n 
        else:
            while t.next != None : 
                t = t.next
        t.next = n 
    def addafter(self,m,data):
        n = node(data)
        t = self.head
        while t.data != m :
            t = t.next 
        n.next = t.next
        t.next = n
    def delfirst(self):
        if self.head == None:
            return " empty"
        else:
            self.head = self.head.next
    def dellast(self):
        t = self.head
        while t.next.next != None : 
            t = t.next
        t.next = None
        
    def delafter(self,m):
        t = self.head
        while t.data != m :
            t = t.next
        t.next = t.next.next

# link = linklist()
# link.addinstart(5)
# link.addinstart(7)
# link.addinstart(2)
# link.addinstart(10)
# link.display()
# link.delfirst()
# link.display()
# link.dellast()
# link.display()
#----------------------------------
#لیست پیوندی دو طرفه
class dnode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class dlinkedlist:
    def __init__(self):
        self.head = None
    def display(self):
        t = self.head 
        while t != None:       
            print(t.data,end=" <----> ") 
            t = t.next
        print(None)
    def addinstart(self,data):
        n = dnode(data)
        if self.head != None:
            n.next = self.head
            self.head.prev = n
        self.head = n 
    def addinend(self,data):
        n = dnode(data)
        if self.head != None:
            t = self.head
            while t.next != None : 
                t = t.next
            t.next = n 
            n.prev = t
        else :
            self.head = n
    def addafter(self,m,data):
        n = dnode()
        t = self.head
        while t.data != m :
            t = t.next
        n.next = t.next
        n.prev = t   
        t.next = n
        n.next.prev = n 
    def delfirst(self):
        if self.head == None:
            return -1
        self.head = self.head.next
        self.head.prev = None
    def dellast(self):
        if self.head == None : 
            return -1
        t = self.head 
        while t.next != None :
            t = t.next
        t.prev.next = None
        t.prev = None
    def delete(self,data):
        t = self.head
        while t.data != data :
            t = t.next
        t.next.prev = t.prev
        t.prev.next = t.next
        t.next = None
        t.prev = None

#تابعی بنویسید که عنصر وسط را حذف کند 
    def delmid(self):
        t = self.head
        count = 0 
        while t.next != None :
            t = t.next
            count+=1
        t = self.head
        if count%2 == 0 : 
            for i in range(count // 2 ):
                t = t.next
        else: 
            for i in range(count // 2 + 1 ):
                t = t.next
        t.next.prev = t.prev
        t.prev.next = t.next
        t.next = None
        t.prev = None
        
dlink = dlinkedlist()
dlink.addinstart(2)
dlink.addinstart(6)
dlink.addinstart(1)
dlink.addinstart(4)
dlink.addinstart(8)
dlink.addinstart(45)

dlink.display()
dlink.delmid()
dlink.display()
