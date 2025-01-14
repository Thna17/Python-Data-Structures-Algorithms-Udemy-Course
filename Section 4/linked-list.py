class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

# Purpose: Represents a single node in the linked list.
# Attributes:
# value: The data stored in the node.
# next: A pointer to the next node in the list (initially None).

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# Purpose: Manages the linked list structure.
# Attributes:
# head: Points to the first node of the list.
# tail: Points to the last node of the list.
# length: Tracks the number of nodes in the list.
# The constructor initializes the linked list with a single node.

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


# Purpose: Prints the values of all nodes in the linked list.
# Logic:
# Start at the head node.
# Iterate through the nodes using the next pointer until reaching the end (None).

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

# Purpose: Empties the linked list.
# Logic: Sets head, tail, and length to None or 0.

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


# Purpose: Adds a new node to the end of the list.
# Logic:
# If the list is empty (head is None), set the new node as both the head and tail.
# Otherwise, link the current tail node to the new node and update the tail.
# Increment the length.

my_linked_list = LinkedList(1)
my_linked_list.append(3)
my_linked_list.append(4)  
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()
