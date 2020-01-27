import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue(DoublyLinkedList):
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        self.add_to_tail(value)

    def dequeue(self):
        self.remove_from_tail()

    def len(self):
        self.__len__()
        
