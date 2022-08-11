class Node:
    def __init__(self, data: int, next_node=None):
        self.data: int = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head
