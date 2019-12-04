import math
import sys

def function( input ):
    validCount = 0
    for candidate in range(input[0], input[1]):
        digitCounts = {}
        for digit in str(candidate):
            if digit not in digitCounts:
                digitCounts[digit] = 1
            else:
                current = digitCounts[digit]
                digitCounts[digit] = current + 1
        if sum(1 for v in digitCounts.values() if v > 2) >= 1 and sum(1 for v in digitCounts.values() if v == 2) == 0:
            continue
        if len(set(str(candidate))) == 6:
            continue
        if "".join(sorted(str(candidate))) != str(candidate):
            continue
        validCount += 1
    return validCount

if __name__ == "__main__":
    input = [130254,678275]    
    print(function(input))