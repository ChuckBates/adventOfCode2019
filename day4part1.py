import math
import sys

def function( input ):
    validCount = 0
    for candidate in range(input[0], input[1]):
        if "".join(sorted(str(candidate))) != str(candidate):
            continue
        if len(set(str(candidate))) == 6:
            continue
        validCount += 1
    return validCount

if __name__ == "__main__":
    input = [130254,678275]
    print(function(input))
    