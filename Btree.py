class btnode():
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class tree():
    def __init__(self,root=None):
        self.root = root
    def inorder (self,root):
        if self.root is None:
            return
        else:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    def postorder(self,root):
         if self.root is None:
            return
         else:
             self.postorder(root.left)
             self.postorder(root.right)
             print(root.data)
    def preorder(self,root):
        if self.root is None:
            return
        else:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
class nodebst():
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

    def searchBst(self, k):
        if self is None or self.key == k:
            return self
        elif k < self.key:
            return self.left.searchBst(k) if self.left else None
        else:
            return self.right.searchBst(k) if self.right else None
    def insertBst(self, k):
        if self is None:
            return nodebst(k)
        else:
            self.right = self.right.insertBst(k) if self.right else nodebst(k)
        return self
    def minvalueBst(root):
        if root is None:
            return root
        while (root.left is not None):
            root=root.left
        return root.key
    def minWithRE(self):
        if self.left is None:
            return self
        else:
            return self.left.minWithRE()
    def heapify(a, k):
     left = 2 * k + 1
     right = 2 * k + 2
     s = k  

     if left < len(a) and a[left] < a[s]:
        s = left
     if right < len(a) and a[right] < a[s]:
        s = right

     if s != k:
        a[k], a[s] = a[s], a[k]
        heapify(a,s)

    def min_heap(a):
        n=int((len(a)//2)-1)
        for i in range(n,-1,-1):
          heapify(a,i)
