class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, value):
        self.__val = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    def __str__(self):
        return f'{self.val}, {self.next}'


class AddTwoNumbers:

    # 1
    # 3 4 2 -> [2,4,3]
    # 4 6 5 -> [5,6,4]
    # 8 0 7 -> [7,0,8]
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        acc = 0
        node1 = l1
        node2 = l2
        temp_node = None
        solution_node: ListNode = ListNode(0, ListNode())
        solution_node_tail: ListNode = solution_node.next
        while True:
            if temp_node is None:
                temp_node = node1 if node1 is not None and node2 is None \
                            else node2 if node2 is not None and node1 is None \
                            else None

            if temp_node is not None:
                res = temp_node.val + acc
                if res >= 10:
                    acc = res // 10
                    res = res % 10
                else:
                    acc = 0

                solution_node_tail.val = res

                if temp_node.next is None:
                    if acc != 0:
                        solution_node_tail.next = ListNode()
                        solution_node_tail = solution_node_tail.next
                        solution_node_tail.val = acc
                    break

                solution_node_tail.next = ListNode()
                solution_node_tail = solution_node_tail.next
                temp_node = temp_node.next
                continue

            if node1 is not None and node2 is not None:
                res = node1.val + node2.val + acc
                if res >= 10:
                    acc = res // 10
                    res = res % 10
                else:
                    acc = 0

                solution_node_tail.val = res

                if node1.next is None and node2.next is None:
                    if acc != 0:
                        solution_node_tail.next = ListNode()
                        solution_node_tail = solution_node_tail.next
                        solution_node_tail.val = acc
                    break

                solution_node_tail.next = ListNode()
                solution_node_tail = solution_node_tail.next
                node1 = node1.next
                node2 = node2.next

        return solution_node.next







