from typing import Optional


class BST[T]:
    key: T
    left: Optional["BST[T]"] = None
    right: Optional["BST[T]"] = None

    def __init__(self, key: T):
        self.key = key

    def insert(self, key: T):
        if key < self.key:
            if self.left:
                self.left.insert(key)
            else:
                self.left = BST(key)
        elif key > self.key:
            if self.right:
                self.right.insert(key)
            else:
                self.right = BST(key)

    def contains(self, key: T) -> bool:
        if key < self.key:
            return self.left and self.left.contains(key)
        elif key > self.key:
            return self.right and self.right.contains(key)
        else:
            return True

    def size(self) -> int:
        s = 1

        if self.left:
            s += self.left.size()
        if self.right:
            s += self.right.size()

        return s
