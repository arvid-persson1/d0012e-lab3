from typing import Optional


class BST[T]:
    key: T
    left: Optional["BST[T]"] = None
    right: Optional["BST[T]"] = None
    # `size` is cached to make benchmarks compared
    # to the balanced variant more fair.
    size: int = 1

    def __init__(self, key: T):
        self.key = key
        # self.left = None
        # self.right = None
        # self.size = 1

    def insert(self, key: T) -> bool:
        inserted = False

        if key < self.key:
            if self.left:
                inserted = self.left.insert(key)
            else:
                self.left = BST(key)
                inserted = True

        elif key > self.key:
            if self.right:
                inserted = self.right.insert(key)
            else:
                self.right = BST(key)
                inserted = True

        if inserted:
            self.size += 1
        return inserted

    def contains(self, key: T) -> bool:
        if key < self.key:
            return self.left and self.left.contains(key)
        elif key > self.key:
            return self.right and self.right.contains(key)
        else:
            return True
