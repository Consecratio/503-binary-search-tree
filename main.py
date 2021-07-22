from BinaryTree import Node
from BinaryTree import BinaryTree

my_node = Node('hello')
# print(my_node)

my_BST = BinaryTree()

my_BST.insert(7)
my_BST.insert(3)
my_BST.insert(11)
my_BST.insert(1)
my_BST.insert(5)
my_BST.insert(4)
my_BST.insert(6)
my_BST.insert(11)
my_BST.insert(9)
my_BST.insert(13)
my_BST.insert(8)
my_BST.insert(12)
my_BST.insert(14)

print('Search for 21: ', my_BST.search(21))
print('Get Max: ', my_BST.get_max())
print('Get Min: ', my_BST.get_min())
print('Get Height: ', my_BST.height())