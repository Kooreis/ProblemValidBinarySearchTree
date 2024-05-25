def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    if not min_val <= node.val <= max_val:
        return False
    return is_bst(node.left, min_val, node.val) and is_bst(node.right, node.val, max_val)