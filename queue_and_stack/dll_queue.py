import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # a Queue is a good choice to store our elements as it allows for fast inserts and removals without having to re-organize the entire section of memory. Also means we don't have to resize allocated space.
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size+=1
        self.storage.add_to_head(value)

    def dequeue(self):
        if self.size==0:
            return None
        else:
            self.size-=1
            return self.storage.remove_from_tail()

    def len(self):
        return self.size
