import math
from random import random


def AddBinaryIntegers(A, B):
    # assumed tht len(a) = len(b)

    C = []
    carry = 0
    for itemA, itemB in zip(A, B):

        itemC = itemA+itemB+carry

        carry = itemC//2
        itemC = itemC % 2

        C.append(itemC)
    C.append(carry)
    return C


def get_dec(A):
    s = 0
    for i, a in enumerate(A):
        # 011001
        s += a*(2**i)
    return s


def run_tests(n, size=6):
    for i in range(n):

        sz = int(random()*size)
        A, B = [], []
        for j in range(sz):
            r1 = int(random()*2)
            r2 = int(random()*2)
            A.append(r1)
            B.append(r2)
        c = get_dec(A) + get_dec(B)
        C = AddBinaryIntegers(A, B)
        c_ = get_dec(C)
        print(f"test {i}", end=" ")
        if c == c_:
            print("✅passed")
        else:
            print(f"❌failed: needed {c} got {c_}, {A}, {B}, {C}")


def main():
    run_tests(23, 9)


if __name__ == "__main__":
    main()
