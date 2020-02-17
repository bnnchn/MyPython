#!/usr/bin/env python3

def power(x, y):
    """
    Takes two non-negative integers x and y as input
    Returns the value x**y.
    """
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)


print(power(5, 2))
print(power(2, 8))
print(power(2, 0))


def dot(L, K):
    """
    Output the dot product of the lists L and K.
    Dot product of two lists is the sum of the products of the elements in the same position in the two lists.
    If these two lists are both empty, dot should output 0.0
    """
    if L == [] or K == []:
        return 0.0
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])


print(dot([], []))
print(dot([1, 2, 3], [4, 5, 6]))

def GCcount(DNA):
    """
    Takes DNA string as input and returns the number of G's and C's that appear in that string.
    """
    if DNA == '':
        return 0
    elif DNA[0] == 'C' or DNA[0] == 'G':
        return 1 + GCcount(DNA[1:])
    else:
        return 0 + GCcount(DNA[1:])


print(GCcount("TTGAC"))
print(GCcount("AGTCCCGGGTTT"))
print(GCcount("spam"))


def countStarts(DNA):
    """
    Takes a DNA string as input and returns the number of times 'ATG" appears in that string.
    """
    if len(DNA) < 3:
        return 0
    elif DNA[0:3] == 'ATG':
        return 1 + countStarts(DNA[1:])
    else:
        return 0 + countStarts(DNA[1:])


print(countStarts("ATTGCCTACGCCGATTTTATGACGGCGATGATGGCTTTTTTTCTGGTGATGTGGCTGATTTCCATCTCCA"))
print(countStarts("TGACCGGCGGACACCTTGGGGCACTCTATCAACCTGCTGAACTGGTCATCATTGGCGGCGCGGGGATAGG"))
print(countStarts("spam"))


def explode(S):
    """
    Takes a string S as input and return a list of the characters (each is a string of length 1) in that string.
    """
    if S == '':
        return []
    else:
        return [S[0]] + explode(S[1:])


print(explode("ThisIsAString"))
print(explode(""))


def removeAll(e, L):
    """
    Takes and element e and a list L.
    Return a another list that is identical to L except that all elements identical to e have been removed.
    """
    if L == []:
        return []
    elif e == L[0]:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])


print(removeAll("abc", ["abc", "def", "abc", "ghi"]))
print(removeAll("xyz", ["abc", "def", "abc", "ghi"]))
