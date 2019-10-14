import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Allows for easier inserts and deletes when we don't know how large the object will be
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size+=1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size < 1:
            return None
        else:
            self.size-=1
            temp = self.storage.remove_from_head()
            return temp

    def len(self):
        return self.size
