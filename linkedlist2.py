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



my_list = LINKEDLIST()
first = NODE(10)
second = NODE(20)
third = NODE(30)
may_be = NODE(None)
fouth = NODE(40)


my_list.head = first
first.next = second
second.next = third
third.next = may_be
may_be.next = fouth

my_list.print()