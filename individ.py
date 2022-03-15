# Создайте рекурсивную функцию, печатающую все подмножества множества

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def subsets(A):
    subs_A = [[]]
    for a in A:
        subs_A += [s + [a] for s in subs_A]
    return subs_A


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6]
    S = subsets(A)
    for s in S:
        if len(s):
            print(set(s))
        else:
            print("{}")
