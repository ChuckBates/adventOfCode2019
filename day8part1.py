import math
import sys

def function( input ):
    width = 25
    height = 6
    image = [[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
                [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
                [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
                [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
                [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
                [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]]
    index = 0
    layers = {}
    counter = 0
    while index < len(input):
        layer = [[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
                [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
                [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
                [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
                [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
                [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]]
        for y in range(height):
            for x in range(width):
                image[y][x] = input[index]
                layer[y][x] = input[index]
                index += 1
        layers[counter] = layer
        counter += 1
    
    layerCounts = {}
    for index in layers:
        layerCounts[index] = sum(r.count(0) for r in layers[index])
    lowest = min(layers, key=layerCounts.get)

    return (sum(l.count(1) for l in layers[lowest])) * (sum(s.count(2) for s in layers[lowest]))

if __name__ == "__main__":
    input = [int(code) for code in open("input.txt").read()]
    print(function(input))
    