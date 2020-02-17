#!/usr/bin/env python3

def f(x):
    return 2 * x


print(f(10))
print(f(-1))


def f(x):
    """Takes a number x as input and returns 2*x."""
    return 2 * x


def sumOfSquares(x, y):
    """Computes the sum of squares of its two inputs."""
    return x ** 2 + y ** 2


def GCcontent4(DNA):
    """Computes the GC content of a DNA string of length4."""
    counter = 0
    if DNA[0] == 'G' or DNA[0] == 'C':
        counter = counter + 1
    if DNA[1] == 'G' or DNA[1] == 'C':
        counter = counter + 1
    if DNA[2] == 'G' or DNA[2] == 'C':
        counter = counter + 1
    if DNA[3] == 'G' or DNA[3] == 'C':
        counter = counter + 1
    return counter / 4.0


print(GCcontent4('CGAA'))


def GCcontent3or4(DNA):
    """Computes the GC content of a DNA string of length 3 or 4."""
    counter = 0
    if len(DNA) == 3:
        if DNA[0] == 'G' or DNA[0] == 'C':
            counter = counter + 1
        if DNA[1] == 'G' or DNA[1] == 'C':
            counter = counter + 1
        if DNA[2] == 'G' or DNA[2] == 'C':
            counter = counter + 1
        return counter / 3.0
    else:
        if DNA[0] == 'G' or DNA[0] == 'C':
            counter = counter + 1
        if DNA[1] == 'G' or DNA[1] == 'C':
            counter = counter + 1
        if DNA[2] == 'G' or DNA[2] == 'C':
            counter = counter + 1
        if DNA[3] == 'G' or DNA[3] == 'C':
            counter = counter + 1
        return counter / 4.0


print(GCcontent3or4('CGAA'))


def GCcontent1thru4(DNA):
    """Computes GC content of a DNA string of length 1 thru 4."""
    counter = 0
    if len(DNA) == 1:
        if DNA[0] == 'G' or DNA[0] == 'C':
            counter = counter + 1
        return counter / 1.0
    elif len(DNA) == 2:
        if DNA[0] == 'G' or DNA[0] == 'C':
            counter = counter + 1
        if DNA[1] == 'G' or DNA[1] == 'C':
            counter = counter + 1
        return counter / 2.0
    elif len(DNA) == 3:
        if DNA[0] == 'G' or DNA[0] == 'C':
            counter = counter + 1
        if DNA[1] == 'G' or DNA[1] == 'C':
            counter = counter + 1
        if DNA[2] == 'G' or DNA[2] == 'C':
            counter = counter + 1
        return counter / 3.0
    else:
        if DNA[0] == 'G' or DNA[0] == 'C':
            counter = counter + 1
        if DNA[1] == 'G' or DNA[1] == 'C':
            counter = counter + 1
        if DNA[2] == 'G' or DNA[2] == 'C':
            counter = counter + 1
        if DNA[3] == 'G' or DNA[3] == 'C':
            counter = counter + 1
        return counter / 4.0


print(GCcontent1thru4('AGAA'))


def GCcontentAny(DNA):
    """Computes GC content of a DNA string of length 1 thru 4."""
    counter = 0
    if len(DNA) == 1:
        if DNA[0] == 'G' or DNA[0] == 'C':
            counter = counter + 1
        return counter / 1.0
    elif len(DNA) == 2:
        if DNA[0] == 'G' or DNA[0] == 'C':
            counter = counter + 1
        if DNA[1] == 'G' or DNA[1] == 'C':
            counter = counter + 1
        return counter / 2.0
    elif len(DNA) == 3:
        if DNA[0] == 'G' or DNA[0] == 'C':
            counter = counter + 1
        if DNA[1] == 'G' or DNA[1] == 'C':
            counter = counter + 1
        if DNA[2] == 'G' or DNA[2] == 'C':
            counter = counter + 1
        return counter / 3.0
    elif len(DNA) == 4:
        if DNA[0] == 'G' or DNA[0] == 'C':
            counter = counter + 1
        if DNA[1] == 'G' or DNA[1] == 'C':
            counter = counter + 1
        if DNA[2] == 'G' or DNA[2] == 'C':
            counter = counter + 1
        if DNA[3] == 'G' or DNA[3] == 'C':
            counter = counter + 1
        return counter / 4.0
    else:
        return 'I cannot handle strings of this length'


print(GCcontentAny('CGAA'))
print(GCcontentAny('CCCCGAA'))


def length(myString):
    """Computes the length of its input string."""
    counter = 0
    for myCharacter in myString:
        counter = counter + 1
    return counter


print(length('CAT'))

myString = 'CAT'
print(len(myString))


def DNAtoRNA(DNA):
    """Returns the equivalent RNA for the given DNA string."""
    RNA = ''
    for nuc in DNA:
        if nuc == 'T':
            RNA = RNA + 'U'
        else:
            RNA = RNA + nuc
    return RNA


print(DNAtoRNA('AGTAC'))
print(DNAtoRNA('AGTTC'))
