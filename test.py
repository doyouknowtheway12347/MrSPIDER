import numpy

class Node:
    _nodes = {}

    def __init__(self, id=None, value=None):
        if id in self._nodes:
            # Return the existing node if the ID already exists
            return self._nodes[id]
        
        # Create a new node
        self.id = id
        self.value = value
        self._nodes[id] = self
    

# Usage example
node1 = Node("123", value=100)
node2 = Node("123", value=1)  # This will return the existing node1

print(node2.value)  
