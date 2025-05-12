
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class slist:
    def __init__(self):
        self.head=None



    #Insert methods--------------------------------------------------------------------

    def insertbeginning(self, data):
        print(f"Inserting node with data:{data}...")
        newnode = node(data)
        newnode.next=self.head
        self.head=newnode
    

    def insertend(self, data):
        new_node = node(data)
        if self.head is None:
            print("List is empty! Setting node to new head...")
            self.head = new_node  
            return
        
        last = self.head 
        while last.next:  
            last = last.next
        last.next = new_node  

    def updateNode(self, data, index):
        print(f"Updating {data} at position {index}...")
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = data
        else:
            while(current_node != None and position != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.data = data
            else:
                print("Index not present!")
           
                

    #Delete methods-----------------------------------------------------------------------

    def deletebeg(self):
        print("Deleting first node...")
        if self.head is None:
            return "List is empty!"
        self.head = self.head.next


    def deletend(self):
        print("Deleting last node...")
        if self.head is None:
            return "List is empty!"
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None


    def getdelete(self, data):
        pass

        




    def gethead(self, data):
        print(f"Searching for {data}...")
        current = self.head
        while current.next:
            current = current.next
            if current.data==data:
                return f"{current.data} found!"
            else:
                return f"{data} not found!"


    def traverse(self):
        print("Traversing linked list...")
        current = self.head
        while current:
            print(current.data+"->", end=" ")
            current = current.next 



if __name__ == '__main__':
    new = slist()
    new.insertbeginning('Mtume')
    new.insertbeginning('Owino')
    new.insertbeginning('Mutere')
    new.insertend("Is")
    new.insertend("A")
    new.insertend("Cool")
    new.insertend("Person")

    new.traverse()
    print("\n")
    #new.deletebeg()
    new.deletend()
    new.traverse()



   
   