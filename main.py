class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10))))))))))


def print_list(current):
    while current:
        print(current.data, end=' -> ' if current.next else '')
        current = current.next
    print()


print_list(head)


def reverse_linked_list(current, previous=None):
    while current:
        current.next, previous, current = previous, current, current.next
    return previous


print_list(reverse_linked_list(head))
