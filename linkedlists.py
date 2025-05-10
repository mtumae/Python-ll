
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class slist:
    def __init__(self):
        self.head=None



    #Insert methods--------------------------------------------------------------------

    def insertbeginning(self, data):
        newnode = node(data)
        newnode.next=self.head
        self.head=newnode
    

    def insertend(self, data):
        new_node = node(data)
        if self.head is None:
            print("List is empty! Setting node to new head...")
            self.head = new_node  # If the list is empty, make the new node the head
            return
        
        last = self.head 
        while last.next:  # Otherwise, traverse the list to find the last node
            last = last.next
        last.next = new_node  # Make the new node the next node of the last node


    def updateNode(self, data, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = data
        else:
            # Traverse the list to find the target index
            while(current_node != None and position != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.data = data
            else:
                print("Index not present!")
           
                

    #-------------------------------------------------------------------------------------






    def gethead(self, data):
        current = self.head
        while current.next:
            current = current.next
            if current.data==data:
                print(f"{current.data} found!")
                return 
            else:
                print(f"{data} not found!")
                return


    def traverse(self):
        current = self.head
        while current:
            print(current.data+"->", end=" ")
            current = current.next 



if __name__ == '__main__':
    new = slist()
    new.insertbeginning('Mtume')
    new.insertbeginning('Owino')
    new.insertbeginning('Mutere')
    new.insertend("test")
    new.traverse()

    new.gethead("Nope")

   