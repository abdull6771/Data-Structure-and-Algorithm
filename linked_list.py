class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_beg(self,data):
        node = Node(data,self.head)#Contain element and the next element of the data
        self.head = node
    
    def print(self):
        if self.head == None:
            print("Linked list is empty")
            return
        itr = self.head
        listr = ""
        while itr:
            listr += str(itr.data)+ "-->"
            itr = itr.next
        print(listr)    

    def insert_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)   
    def insert_values(self,data_list):
        self.head = None 
        for data in data_list:
            #self.insert_beg(data)
            self.insert_end(data)

    def lenght(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next

        return count
    def remove(self,index):
        if index <  0 or index > self.lenght():
            raise Exception("Invalid Index")
        if index ==0:
            self.head = self.head.head
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    def insert_at(self,index,data):
        if index < 0 or index > self.lenght():
            raise Exception("INVALID INDEX")
        if index ==0:
            self.insert_beg(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr=itr.next
            count +=1
    def remove_by_value(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next= itr.next.next
                break
            itr = itr.next
    def inser_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break
            itr = itr.next
li = LinkedList()
#li.insert_beg(4)
#li.insert_beg(8)
# li.insert_end(7)
# li.insert_end(9)
# li.insert_end(0)
# li.insert_end(70)
# li.insert_end(1)
li.insert_values(["a","b","c","d"])
li.inser_after_value("a","abba")
li.print()
# li.remove(2)
# li.insert_at(2,"remove")
li.remove_by_value("b")
li.print()
print("Lenght",li.lenght())