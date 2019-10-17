from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit=limit
        self.current=0
        self.dict={}
        self.contents = DoublyLinkedList()
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.dict:
            self.contents.move_to_front(self.dict.get(key))
            return self.contents.head.value[1]
        else:
            return None
        
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):

        if key in self.dict:
            self.dict.get(key).value=(key,value)
            self.contents.move_to_front(self.dict.get(key))

        else:
            self.contents.add_to_head((key,value))
            self.dict[key]=self.contents.head

            if self.current>=self.limit:
                self.dict.pop(self.contents.remove_from_tail()[0])
            else:
                self.current+=1

        '''
        elif self.current >= self.limit:
            to_remove = self.contents.tail
            self.contents.remove_from_tail()
            self.dict.pop(to_remove.value[0])

            self.contents.add_to_head((key,value))
            self.dict[key] = self.contents.head

        else:
            self.current+=1
            self.contents.add_to_head((key,value))
            self.dict[key] = self.contents.head
        '''