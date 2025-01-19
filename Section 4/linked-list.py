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


    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail =  pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

# Purpose: Removes and returns the last node from the list.
# Logic: 
# If the list is empty, return None.
# Traverse the list to find the second-to-last node.
# Update the tail to the second-to-last node.
# Set the next pointer of the new tail to None.
# Decrement the length.
# If the list is empty, set head and tail to None.
# Return the value of the removed node.


    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

# Purpose: Adds a new node to the beginning of the list.
# Logic:
# If the list is empty, set the new node as both the head and tail.
# Otherwise, link the new node to the current head and update the head.
# Increment the length.

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail == None
        return temp

#Purpose: Remove the first node of the beginning of the list


    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    

my_linked_list = LinkedList(2)
my_linked_list.append(3)

my_linked_list.prepend(1)


# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length, '\n')

# print('Linked List:')
# my_linked_list.print_list()

# # (2) Items - Returns 2 Node
# print(my_linked_list.pop())

# # (1) Item - Returns 1 Node
# print(my_linked_list.pop())

# # (None) Item - Returns None (since the list is empty)
# print(my_linked_list.pop())

# # (2) Items - Return 2 Node
# print(my_linked_list.pop_first())

# # (1) Items - Return 1 Node
# print(my_linked_list.pop_first())

# # (0) Items - Return Node
# print(my_linked_list.pop_first())

# print(my_linked_list.get(0))

my_linked_list.set_value(1, 2)
my_linked_list.insert(1, 1)
my_linked_list.print_list()