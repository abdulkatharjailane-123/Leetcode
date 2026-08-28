class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def insert_position(self, data, position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for _ in range(position - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    def delete_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            self.head = self.head.next
            return

        temp = self.head

        for _ in range(position - 2):
            if temp is None or temp.next is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next

    def search(self, value):
        temp = self.head
        position = 1

        while temp:
            if temp.data == value:
                print("Element found at position", position)
                return
            temp = temp.next
            position += 1

        print("Element not found")

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


sll = SinglyLinkedList()

sll.insert_end(10)
sll.insert_end(20)
sll.insert_end(30)

sll.insert_beginning(5)

sll.display()

sll.insert_position(15, 3)
sll.display()

sll.delete_beginning()
sll.display()

sll.delete_end()
sll.display()

sll.delete_position(2)
sll.display()

sll.search(20)