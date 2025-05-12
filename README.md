### Python Singly linked list
*Dsa classwork 09/05/2025*

Group members:
- Shekinah Gloria - 182989
- Mutwiri Joypraise Kendi - 189539
- Emmanuel Githaiga - 189225
- Kayla Biwott - 190382
- Benjamin Wahothi - 
- Mtume Owino - 188916

---

```class node:```
used as a blueprint for nodes which contain data and references to other nodes

```class slist:```
used as a blueprint for the singly linked list containing various methods allowing us to update and delete as well as traverse through the linked list.

**Functions**

```python
def insertbeginning(self, data):
        print(f"Inserting node with data:{data}...")
        newnode = node(data)#creates a new node from the class data from the argument passed in the function.
        newnode.next=self.head #sets the reference of the new node to the head of the list
        self.head=newnode#sets the head of the list to the node that we created
```

```python
    def insertend(self, data):
        new_node = node(data)
        #creates a new node from the class data from the argument passed in the function.

        if self.head is None:
            print("List is empty! Setting node to new head...")
            self.head = new_node #Sets node to head if list is empty 
            return
       
        
        last = self.head
        while last.next:  
            last = last.next #loops over list if the current head.next is True
        last.next = new_node # if False sets the current head to the new node 
```

```python 
    def updateNode(self, data, index):
            print(f"Updating {data} at position {index}...")
            current_node = self.head
            position = 0 #Initializes a variable to remember the position 
            if position == index:
                current_node.data = data 
                # if the current position is eequal to the value that we passed as index
                # we update the node at that postiion with the data passed as an argument
            else:
                while(current_node != None and position != index):
                    position = position + 1
                    current_node = current_node.next
                
                # Otherwise we keep looping throught the list

                if current_node != None:
                    current_node.data = data
                else:
                    print("Index not present!")
                
```


```python 
    def deletebeg(self):
            print("Deleting first node...")
            if self.head is None:
                return "List is empty!"
            #Checks if list is empty
            self.head = self.head.next 
```

