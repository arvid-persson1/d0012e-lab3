import random
from itertools import product
from time import time

from bst import BST
from bst_balanced import BST as BSTBalanced

# 1500 is fairly safe from reaching max recursion depth.
INSERTIONS = 1500
LOOKUPS = INSERTIONS
UNIQUE_VALUES = INSERTIONS // 2
ITERATIONS = 1000

BARELY_BALANCED = 0.98
LIGHTLY_BALANCED = 0.9
SEMI_BALANCED = 0.75
HEAVILY_BALANCED = 0.6
STRICTLY_BALANCED = 0.52

INSERTIONS_LARGE = 1_000_000
ITERATIONS_LARGE = 1


def randint():
    return random.randint(0, UNIQUE_VALUES)


_counter = 0


# Produces mostly increasing values.
def count():
    global _counter
    _counter += random.randint(-1, 3)
    return _counter


def reset_count():
    global _counter
    _counter = 0


def make_tree(root, c):
    if c:
        return BSTBalanced(root, c)
    else:
        return BST(root)


def main():
    print(f"small trees (n = {INSERTIONS}):")
    print("\trandom........\tincreasing....")
    print("c\tinsert\tlookup\tinsert\tlookup")

    for c in (
        None,
        BARELY_BALANCED,
        LIGHTLY_BALANCED,
        SEMI_BALANCED,
        HEAVILY_BALANCED,
        STRICTLY_BALANCED,
    ):
        print(c or "N/A", end="\t")

        time_insert_random = 0
        time_lookup_random = 0
        time_insert_inc = 0
        time_lookup_inc = 0

        for _ in range(ITERATIONS):
            tree = make_tree(randint(), c)

            start = time()
            for _ in range(INSERTIONS):
                tree.insert(randint())
            end = time()

            time_insert_random += end - start

            start = time()
            for _ in range(LOOKUPS):
                tree.contains(randint())
            end = time()

            time_lookup_random += end - start

            tree = make_tree(-1, c)

            start = time()
            for _ in range(INSERTIONS):
                tree.insert(count())
            end = time()
            reset_count()

            time_insert_inc += end - start

            start = time()
            for _ in range(LOOKUPS):
                tree.contains(count())
            end = time()
            reset_count()

            time_lookup_inc += end - start

        t1 = time_insert_random * 1000 / ITERATIONS
        t2 = time_lookup_random * 1000 / ITERATIONS
        t3 = time_insert_inc * 1000 / ITERATIONS
        t4 = time_lookup_inc * 1000 / ITERATIONS
        print(f"{t1:#.5g}\t{t2:#.5g}\t{t3:#.5g}\t{t4:#.5g}")

    print(f"large tree (n = {INSERTIONS_LARGE}):")
    print("c\tinsert\t\tlookup")

    for c in (LIGHTLY_BALANCED, SEMI_BALANCED, HEAVILY_BALANCED):
        tree = BSTBalanced(randint(), c)

        start = time()
        for _ in range(INSERTIONS_LARGE):
            tree.insert(randint())
        end = time()

        time_insert_large = end - start

        start = time()
        for _ in range(INSERTIONS_LARGE):
            tree.contains(randint())
        end = time()

        time_lookup_large = end - start

        t5 = time_insert_large * 1000 / ITERATIONS_LARGE
        t6 = time_lookup_large * 1000 / ITERATIONS_LARGE

        print(f"{c}\t{t5:#.8g}\t{t6:#.8g}")


if __name__ == "__main__":
    main()
