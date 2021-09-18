
# Defines a node in the singly linked list
class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node


# Defines the singly linked list 
class LinkedList:
    # Initialize (self)
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):  
        if self.head != None:
            return self.head.value

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):  
        first_node = Node(value)
        first_node.next = self.head
        self.head  = first_node
        return first_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    ## Time Complexity: O(n)
    # Space Complexity: O(1) 
    def search(self, value):
        current = self.head
        while current !=None:
            if current.value == value:
                return True
            current = current.next
        return False
  
    # method that returns the length of the singly linked list
    # Time Complexity:  O(n)
    # Space Complexity: O(1) 
    def length(self):  
        if self.head == None:
            return 0
        current = self.head
        count = 0
        while current !=None:
            count  +=1
            current = current.next
        return count

    # method returns value at a given index in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):  
        # if list is empty
        if not self.head:
            return None
        current = self.head
        current_i = 0
        while current and current_i < index:
            if index != current_i:
                current_i +=1
                current = current.next
        return current.value

    # method returns value of last node in linked list
    # returns None if linked list is empty
    # Time Complexity: O(n) - Would be O(1) if I added tail
    # Space Complexity: O(1)?
    def get_last(self):  
        if self.head == None:
            return None
        current = self.head
        while current.next != None:
            current = current.next
        return current.value

    # method - inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    #  trying add last
    def add_last(self, value):  
        last_node = Node(value)
        # if list is empty, add and node becomes head (can I call add first, if so how?)
        if self.head == None:
            # last_node = Node(value)
            last_node.next = self.head
            self.head = last_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = last_node

    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def find_max(self): 
        if self.head == None:
            return None
        current_node = self.head
        max_value = current_node.value  
        while current_node != None: 
            if max_value < current_node.value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value): 
        if not self.head:
            return
        current = self.head
        next_node = current.next

        # if value is at the head
        if current.value == value:
            self.head = next_node
            return 
        
        # if value is from second node to end
        while next_node !=None:
            if next_node.value == value:
                current.next = next_node.next
            current = current.next
            next_node = next_node.next
        return

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))
  
    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        if self.head == None:
            return None

        last = None
        current = self.head
        next_node = current.next

        while next_node !=None:
            current.next = last # last = none

            last = current
            current = next_node
            next_node = next_node.next

        current.next = last 
        self.head = current
        
        return

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?

    def find_middle_value(self):
        pass

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        pass

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        pass


    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
