class stack():
    def __init__(self,limit = 10) :
        self.stack = []
        self.limit = limit
    #بالاترین استک رو نمایش میده 
    def peek(self):
        if len(self.stack) <= 0:
            return -1 
        else:
            return self.stack[len(self.stack) - 1]
    #حذف میکنه
    def pop(self):
        if len(self.stack) <= 0 :
            return -1
        else:
            return self.stack.pop()
    #اضافه میکنه
    def push(self,data):
        if len(self.stack) >= self.limit :
            return -1
        else:
            self.stack.append(data)
    def display(self) :
        if len(self.stack) <= 0 :
            return -1
        else:
            for i in self.stack():
                print(i)
    def is_empty(self):
        if len(self.stack) <= 0:
            return True
        else:
            return False
st = stack()
# st.push(12)
# st.push(11)
# st.push(5)
# st.push(3)
# st.push(2)
# print(st.peek())
# ------------------------------------------------- 

# با استفاده از ساختمان داده پشته تابعی بنویسید که عددی را از مبنای 10 به 2 ببرد 

# def dec2bin(number):
#     s = stack()
#     while number > 0 :
#         r = number % 2
#         s.push(r)
#         number = number // 2
#     b = ""
#     while not s.is_empty():
#         b = b + str(s.pop())
#     return b 

#-------------------------------------------
#با استفاده از ساختمان داده استک تابعی بنویسید که محتوای یک لیست را معکوس کند 

# def reverse(lst):
#     s = stack()
#     for i in lst:
#         s.push(i)
#     for j in range(len(lst)):
#         lst[j] = s.pop()


#------------------------------------
#با استفاده از ساختمان داده تابعی بنویسید که محتوای یک پشته را معکوس کند 
# s=stack()
# s.push('a')
# s.push('b')

# def reversestack(s):
#     s1 = stack()
#     s2 = stack()
#     while not s.is_empty():
#         s1.push(s.pop())
#     while not s1.is_empty():
#         s2.push(s1.pop())
#     while not s2.is_empty():
#         s1.push(s2.pop())
# reversestack(s)
# s.display()

#----------------------------------
# با استفاده از ساختمان داده پشته حاصل یک عبارت postfix  را محاسبه کنید
# 7 4 -3 * 1 5 + / * 
#1 - ایجاد استک 
#2 - وقتی عملوند را دیدیم ان را درون پشته  push  می کنیم 
#3 - وقتی عملگری را دیدیم دوباره عمل pop  را انجام داده و سپس عملگر را بر روی انها اعمال می کنیم و در نهایت push  می کنیم

# def respost(lst):
#     s = stack(len(lst) // 2)
#     for e in lst:
#         if e == '*':
#             t2 = s.pop()
#             t1 = s.pop()
#             t = t1*t2
#             s.push(t)
#         #elif + / - .
        
#         else:
#             s.push(e)
#             return s.stack[0]
#----------------------------------------
#تابعی بنویسید که باز و بسته بودن پرانتز - اکولاد و کروشه را در یکه رشته چک کند اگر تنظیم بود ترو در غیر اینصورت فالس را برگرداند این کار را با ساختمان داده پشته - استک+ بنویسید 

def match_s(strr):
    s = stack()
    for i in strr:
        if i in "({[" :
            s.push(i)
        elif i in ")}]" :
            if s.peek() == i : 
                s.pop()
            else:
                return False
    if s.is_empty():
        return True
    else:
        return False
striing = "([])"
print(match_s(striing))