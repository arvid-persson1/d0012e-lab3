from math import nextafter
from typing import Iterator, Optional, Sequence

UNBALANCED = nextafter(1, 0)
FULLY_BALANCED = nextafter(0.5, 1)


class BST[T]:
    key: T
    left: Optional["BST[T]"] = None
    right: Optional["BST[T]"] = None
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
        self.c = c

    def insert(self, key: T) -> bool:
        inserted = False

        if key < self.key:
            if self.left:
                inserted = self.left.insert(key)
            else:
                self.left = BST(key, self.c)
                inserted = True

        elif key > self.key:
            if self.right:
                inserted = self.right.insert(key)
            else:
                self.right = BST(key, self.c)
                inserted = True

        if inserted:
            self.size += 1

        allowed = self.size * self.c
        left_unbalanced = self.left is not None and self.left.size > allowed
        right_unbalanced = self.right is not None and self.right.size > allowed
        if left_unbalanced or right_unbalanced:
            self.balance()

        return inserted

    def traverse_inorder(self) -> Iterator[T]:
        if self.left:
            yield from self.left.traverse_inorder()

        yield self.key

        if self.right:
            yield from self.right.traverse_inorder()

    def from_inorder(nodes: Sequence[T], c: float) -> "BST[T]":
        def go(start: int, end: int) -> "BST[T]":
            if end == start:
                return None

            mid = (start + end) // 2

            root = BST(nodes[mid], c)
            root.size = end - start
            root.left = go(start, mid)
            root.right = go(mid + 1, end)

            return root

        return go(0, len(nodes))

    # TODO: optimize with tree rotations?
    def balance(self):
        inorder = tuple(self.traverse_inorder())
        balanced = BST.from_inorder(inorder, self.c)
        # We can't reassign `self` in Python.
        self.key = balanced.key
        self.left = balanced.left
        self.right = balanced.right

    def contains(self, key: T) -> bool:
        if key < self.key:
            return self.left and self.left.contains(key)
        elif key > self.key:
            return self.right and self.right.contains(key)
        else:
            return True
