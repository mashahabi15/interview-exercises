# Method 1 => It iterates linked list more than once.
from linked_list import Node, LinkedList


class MyLinkedList(LinkedList):

    def find_middle_element_iterative(self) -> Node:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # Don't use another list(auxiliary space=O(1))
        tmp: Node = self.head
        length: int = 0
        while tmp:
            tmp = tmp.next_node
            length += 1

        tmp: Node = self.head
        mid: int = length // 2
        while mid:
            tmp = tmp.next_node
            mid -= 1

        return tmp

    def find_middle_element_non_iterative(self) -> Node:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        slow: Node = self.head
        fast: Node = self.head

        while fast and fast.next_node:
            slow = slow.next_node
            fast = fast.next_node.next_node

        return slow

    def delete_middle_node(self):
        """
         Time Complexity: O(n)
         Space Complexity: O(1)
         """

        middle_node: Node = self.find_middle_element_non_iterative()

        tmp = self.head
        while tmp.next_node != middle_node:
            tmp = tmp.next_node

        tmp.next_node = middle_node.next_node


n1 = Node(data=1)
n2 = Node(data=2)
n3 = Node(data=3)
# n4 = Node(data=4)
n1.next_node = n2
n2.next_node = n3
# n3.next_node = n4
my_linked_list = MyLinkedList(head=n1)
print(my_linked_list.find_middle_element_non_iterative())
print(my_linked_list.find_middle_element_iterative())
