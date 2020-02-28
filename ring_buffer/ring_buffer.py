from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:                 # if cap hasn't been reached, add to tail
            self.storage.add_to_tail(item)
            self.current = self.storage.head                    # consistently the LRU will be the head until cap is reached


        else:                                                   # third attempt: moving MRU to tail of list is not working

            self.current.value = item                           # instead, maybe try cycling thru list with an independent current value
            if self.current is self.storage.tail:               # when you reach end of list
                self.current = self.storage.head                # set current back to head
            else:
                self.current = self.current.next                # otherwise move to the right

                                                                # it works!


            # initial plan was to keep the head of the list current
            # and move it to the tail everytime it was overwritten
            # could not get it to work

            # forward = self.storage.head.next
            # self.current.value = self.storage.remove_from_head
            # self.current.value = item
            # self.storage.add_to_tail(self.current)

            # forward = self.head.next
            # self.storage.delete(self.storage.head)

            # self.storage.head = self.current.next
            # self.storage.move_to_end(self.current)            # not working for some reason
            # # if self.current is self.storage.tail:
            # #     self.current = self.storage.head
        #     # # else:
        # self.current = self.storage.head
        
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.head                            # init node at the first node

        while node:                             # checking for None
            list_buffer_contents.append(node.value)         # add the node.value to the list
            node = node.next                                # and move onto the next Node

        return list_buffer_contents














# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
