from math import nextafter
from typing import Optional

UNBALANCED = nextafter(1, 0)
FULLY_BALANCED = nextafter(0.5, 1)


class BSTBalanced[T]:
    key: T
    left: Optional["BSTBalanced[T]"] = None
    right: Optional["BSTBalanced[T]"] = None
    # It would be possible to model the data in such a way that not
    # every node has to store `c`, but this makes the code simpler,
    # especially for operations like extracting a subtree.
    c: float
    # As `size` will be read quite often, it's best to cache it
    # instead of performing an O(n) calculation every insertion.
    size: int = 1

    def __init__(self, key: T, c: float):
        assert 0.5 < c < 1

        self.key = key
        # self.left = None
        # self.right = None
        self.c = c
        # self.size = 1

    def insert(self, key: T) -> bool:
        inserted = False

        if key < self.key:
            if self.left:
                inserted = self.left.insert(key)
            else:
                self.left = BSTBalanced(key, self.c)
                inserted = True

        elif key > self.key:
            if self.right:
                inserted = self.right.insert(key)
            else:
                self.right = BSTBalanced(key, self.c)
                inserted = True

        if inserted:
            self.size += 1

        allowed = self.size * self.c
        left_unbalanced = self.left is not None and self.left.size > allowed
        right_unbalanced = self.right is not None and self.right.size > allowed
        if left_unbalanced or right_unbalanced:
            self.balance()

        return inserted

    def traverse_inorder(self) -> list[T]:
        res = []

        def go(node):
            if node:
                go(node.left)
                res.append(node.key)
                go(node.right)

        go(self)
        return res

    # TODO: optimize with tree rotations?
    def balance(self):
        balanced = from_inorder(self.traverse_inorder(), self.c)
        # We can't reassign `self` in Python.
        self.key = balanced.key
        self.left = balanced.left
        self.right = balanced.right

    def contains(self, key: T) -> bool:
        return (
            self.key == key
            or (self.left and self.left.contains(key))
            or (self.right and self.right.contains(key))
        )


def from_inorder[T](nodes: list[T], c: float) -> BSTBalanced[T]:
    if not nodes:
        return None

    n = len(nodes)
    mid = n // 2

    root = BSTBalanced(nodes[mid], c)
    root.size = n
    root.left = from_inorder(nodes[:mid], c)
    root.right = from_inorder(nodes[mid + 1 :], c)

    return root
