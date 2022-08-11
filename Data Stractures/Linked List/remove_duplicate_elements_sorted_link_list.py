from linked_list import Node, LinkedList


class SortedLinkedList(LinkedList):
    def remove_duplicate_elements(self):
        """
        Removes duplicate elements from a sorted linked list

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        curr_node = self.head

        while curr_node:
            while curr_node.next and curr_node.data == curr_node.next.data:
                curr_node.next = curr_node.next.next

            curr_node = curr_node.next

        return self.head
