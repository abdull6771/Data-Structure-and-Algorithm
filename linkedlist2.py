class NODE:
    def __init__(self,data):
        self.data = data
        self.next = None

class LINKEDLIST:
    def __init__(self):
        self.head = None
    def print(self):
        temp = self.head
        while(temp!= None):
            print(temp.data)
            temp = temp.next
    def push_beg(self,data):
        New_Node = NODE(data)
        New_Node.next = self.head
        self.head = New_Node
    def push_end(self,data):
        New_Node = NODE(data)
        if self.head == None:
            New_Node = self.head
            return
        temp = self.head
        while(temp.next != None):
            temp.next = temp
        temp.next = New_Node


my_list = LINKEDLIST()
first = NODE(10)
second = NODE(20)
third = NODE(30)
fouth = NODE(40)


my_list.head = first
first.next = second
second.next = third
third.next = fouth
my_list.push_beg(60)
my_list.push_end(100)
my_list.print()