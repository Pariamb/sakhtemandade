class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display(self, separator=" <-> "):
        current = self.head
        while current:
            print(current.data, end=separator)
            current = current.next
        print()

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
stack.push(5)
stack.push(7)
stack.push(3)


binary_lists = DoublyLinkedList()


while not stack.is_empty():
    current_data = stack.pop()

    binary_list = DoublyLinkedList()
    
    while current_data > 0:
        remainder = current_data % 2
        binary_list.append(remainder)
        current_data //= 2

    binary_lists.append(binary_list)
    


binary_lists.display()


current = binary_lists.head
while current:
    current_binary = current.data
    current_binary.display(" <-> ")
    current = current.next
    #  if first_max is None or t.data > first_max:
    #         second_max, first_max = first_max, t.data
    #     elif second_max is None or t.data > second_max:
    #         second_max = t.data
