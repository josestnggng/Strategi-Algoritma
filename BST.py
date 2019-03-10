
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def add(node, val):
    if node is None:
        return Node(val)

    if val < node.val:
        node.left = add(node.left, val)
    elif val > node.val:
        node.right = add(node.right, val)

    return node


def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.val)
        in_order(node.right)


if __name__ == "__main__":
    root = Node(4)
    add(root, 2)
    add(root, 5)
    add(root, 1)
    add(root, 3)
    in_order(root)
