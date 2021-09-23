class Stack:
    def __init__(self):
        self.items = []    
    
    def push(self, item):
        """Accepts an item as a parameter and appends it to the end of the list.
        Returns nothing.
        
        The runtime for this method is O(1), or constant time.
        """
        self.items.append(item)

    def pop(self):
        """Removes and returns the last item in the list which is also top item of the stack.
                
        The runtime for this method is O(1), or constant time because all it does is index the 
        last item.
        """
        if self.items:
            self.items.pop()
        return None

    def peek(self):
        """this method returns the last item in the list or the top item in the list
        This method runs in constant time --indexing is done in constant time
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """returns the length of the list that is representing the Stack
        The runtime is constant time
        """

        return len(self.items)

    
    def is_empty(self):
        """This method returns Boolean value describing whether or not Stack is empty.
        The runtime is constant.
        """
        return self.items == []