
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertbeg(head, data):
    new_node = node(data)
    new_node.next = head
    return new_node



def deletebeg(head):
    if head is None:
        print("List is empty")
        return None

    del(head)


def traverse(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


