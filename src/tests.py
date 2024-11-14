from bst import *
from bst_balanced import *


def disp(root, indent=0):
    if root:
        disp(root.right, indent + 1)
        print("    " * indent, root.key)
        disp(root.left, indent + 1)


def main():
    test_unbalanced()
    test_balanced()
    test_semibalanced()


def test_unbalanced():
    t = BSTBalanced(8, UNBALANCED)
    assert t.size == 1

    assert t.insert(3)
    assert t.size == 2 and t.left.size == 1

    assert not t.insert(3)
    assert t.size == 2 and t.left.size == 1

    assert t.insert(1)
    assert t.size == 3 and t.left.size == 2 and t.left.left.size == 1

    assert t.insert(6)
    assert t.size == 4 and t.left.size == 3 and t.left.right.size == 1

    assert t.insert(10)
    assert t.size == 5 and t.right.size == 1

    assert t.insert(14)
    assert t.size == 6 and t.right.size == 2 and t.right.right.size == 1

    assert not t.insert(14)
    assert t.size == 6 and t.right.size == 2 and t.right.right.size == 1


def test_balanced():
    t = BSTBalanced(8, FULLY_BALANCED)
    assert t.size == 1

    assert t.insert(3)
    assert t.size == 2 and t.left.size == 1

    assert not t.insert(3)
    assert t.size == 2 and t.left.size == 1

    assert t.insert(1)
    assert t.key == 3
    assert t.size == 3 and t.left.size == 1 and t.right.size == 1

    assert t.insert(6)
    assert t.size == 4 and t.right.size == 2 and t.right.left.size == 1

    assert t.insert(10)
    assert t.key == 6 and t.left.key == 3 and t.right.key == 10
    assert t.size == 5 and t.left.size == 2 and t.right.size == 2

    assert t.insert(14)
    assert t.size == 6 and t.right.size == 3 and t.right.right.size == 1

    assert not t.insert(14)
    assert t.size == 6 and t.right.size == 3 and t.right.right.size == 1


def test_semibalanced():
    t = BSTBalanced(8, 0.7)
    assert t.size == 1

    assert t.insert(3)
    assert t.size == 2 and t.left.size == 1

    assert not t.insert(3)
    assert t.size == 2 and t.left.size == 1

    assert t.insert(1)
    assert t.size == 3 and t.left.size == 2 and t.left.left.size == 1

    assert t.insert(6)
    assert t.key == 6
    assert t.size == 4 and t.left.size == 2 and t.right.size == 1

    assert t.insert(10)
    assert t.right.size == 2 and t.right.right.size == 1

    assert t.insert(14)
    assert t.right.size == 3 and t.right.right.size == 2


if __name__ == "__main__":
    main()
