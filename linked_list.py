class Node(object):
    def __init__(self, object):
        self.val = object
        self.next_node = None

class DoublyLinkedListNode(object):
    def __init__(self,object):
        self.val = object
        self.next_node = None
        self.prev_node = None