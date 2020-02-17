#!/usr/bin/env python3

def countPattern(shortPattern, longString):
    """Computes number of times short string pattern occurs in long string."""
    counter = 0
    for index in range(len(longString)):
        if longString[index:index + (len(shortPattern))] == shortPattern:
            counter = counter + 1
    return counter


print(countPattern('aha', 'haha!aha.'))
print(countPattern('zzz', 'hi there!'))
print(countPattern('aa', 'aaabaaa'))
