Here is a Python console application that checks if a binary tree is a valid binary search tree:

```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    if not min_val <= node.val <= max_val:
        return False
    return is_bst(node.left, min_val, node.val) and is_bst(node.right, node.val, max_val)

def main():
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    if is_bst(root):
        print("This is a binary search tree")
    else:
        print("This is not a binary search tree")

if __name__ == "__main__":
    main()
```

In this code, we first define a Node class for the binary tree. Then we define a function `is_bst` that checks if a binary tree is a binary search tree. This function works by recursively checking that all nodes in the left subtree are less than the root and all nodes in the right subtree are greater than the root. The `main` function creates a binary tree and checks if it is a binary search tree using the `is_bst` function.