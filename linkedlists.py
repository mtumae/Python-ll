
class node:
    def __init__(self, data):
        self.data=data
        self.next=None


    def insert_beginning(self, data):
        newNode = node(data)
        if self.head == None:
            var = self.head == newNode
            return
        else:
            newNode.next = self.head
            self.head=newNode


