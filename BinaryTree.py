class Node:
    def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    
    def __str__(self):
        return f'{self.data}'

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        '''
            Insert(data: any) -> None:\n 
            creates a new Node from the data passed in and adds it to the tree
            If the data is already in the tree, does not insert it again
        '''
        # first, make a node from the data
        new_node = Node(data)

        # if there is no root, set node to be root
        if not self.root:
            self.root = new_node
            return

        # loop over the tree starting at the root and do comparisons
        current_node = self.root

        while current_node:
            # if the new_node.data < current_node.data
            if new_node.data < current_node.data:
                # if there is no left
                if not current_node.left:
                    # set the left to the new_node
                    current_node.left = new_node
                    return
                else:
                    current_node = current_node.left
            elif new_node.data > current_node.data:
                # if there is no right
                if not current_node.right:
                    # set the right to the new_node
                    current_node.right = new_node
                    return
                else:
                    current_node = current_node.right
            else:
                # return if duplicate num
                return
            

    def search(self, val):
        '''
            search(value: any) -> value or bool:\n 
            Performs depth first search
            Search the Tree for a node with the given value
            If the node exists, return it
            If the node doesn't exist, return false
        '''
        # loop through the tree starting at the root
        current_node = self.root
        while current_node:
            # if the value is less than the current node
            if val < current_node.data:
                # set current node to be the left
                current_node = current_node.left
            # else if the value is greater
            elif val > current_node.data:
                # set current node to be the right
                current_node = current_node.right
            # otherwise return the node
            else:
                return current_node
        
        return False


    def print(self, node=None):
        '''
            print(node=optional: Node) -> None:\n
            prints out all values recursively (in a breadth first search fashion)
            defualt start is at root node
        '''
        # check if this is the first recursion
        if not node:
            node = self.root

        # print the node
        print(node)

        # if there is a left node
        if node.left:
            # recursively invoke self.print on the left node
            self.print(node.left)

        # if there is a right node
        if node.right:
            # recursively invoke self.print on the right node
            self.print(node.right)

    def size(self, node=None):
        '''
            size(node=optional: Node) -> int:\n 
            performs breadth first search
            Calculate the number of nodes in the tree, starting from the given node
            If no node is provided, we can use the root as a sensible default
        '''
        pass

    def height(self, node=None):
        '''
            height(node=optional: Node) -> int:\n 
            perform breadth first search
            Calculate the maximum amount of nodes in any one path from the given node
            If not given a specific node, default to using the root node
        '''
        count_left = 0
        count_right = 0

        if not node:
            if not self.root: return 0

            node = self.root
            count_left += 1
            count_right += 1

        if node.left:
            count_left += 1 + self.height(node.left)
        
        if node.right:
            count_right += 1 + self.height(node.right)
        
        if count_left > count_right:
            return count_left
        else:
            return count_right


    def get_max(self):
        '''
            getMax() -> int:\n 
            perform depth first search
            Calculate the maximum value held in the tree
        '''
        if not self.root:
            return None

        current_node = self.root

        while current_node:
            current_node = current_node.right
        
        return current_node

    def get_min(self):
        '''
            getMin() -> int:\n 
            perform depth first search
            Calculate the minimum value held in the tree
        '''
        if not self.root:
            return None

        current_node = self.root

        while current_node:
            current_node = current_node.left
        
        return current_node