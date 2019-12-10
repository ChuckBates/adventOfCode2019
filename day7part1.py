import math
import sys
import itertools

def function( input ):
    ampInputs = [0,1,2,3,4]
    bestOutput = 0
    for possibleCombo in itertools.permutations(ampInputs, 5):
        ampOutput = 0
        for ampInput in possibleCombo:
            ampOutput = intCodeComputer( input,[ampInput,ampOutput])
        if ampOutput > bestOutput:
            bestOutput = ampOutput   
            print(bestOutput)                         
    return bestOutput

def intCodeComputer( inputProgram,inputInts ):
    programMain = inputProgram
    position = 0
    output = 0
    while position < len(programMain):
        first = programMain[position]
        length = 4
        if int(str(first)[-1]) == 3 or int(str(first)[-1]) == 4:
            length = 2
        if int(str(first)[-1]) == 5 or int(str(first)[-1]) == 6:
            length = 3
        opCodeInstruction = []
        for index in range(length):
            if position + index < len(programMain):
                opCodeInstruction.append(programMain[position + index])      
        mode = int(str(opCodeInstruction[0])[-1])
        if mode == 1:
            firstMode = str(opCodeInstruction[0])[-3:-2]
            first = programMain[programMain[position + 1]] if len(firstMode) == 0 or int(firstMode) == 0 else programMain[position + 1]
            secondMode = str(opCodeInstruction[0])[-4:-3]
            second = programMain[programMain[position + 2]] if len(secondMode) == 0 or int(secondMode) == 0 else programMain[position + 2]
            index = programMain[position + 3]
            programMain[index] = first + second
            position += length
        elif mode == 2:
            firstMode = str(opCodeInstruction[0])[-3:-2]
            first = programMain[programMain[position + 1]] if len(firstMode) == 0 or int(firstMode) == 0 else programMain[position + 1]
            secondMode = str(opCodeInstruction[0])[-4:-3]
            second = programMain[programMain[position + 2]] if len(secondMode) == 0 or int(secondMode) == 0 else programMain[position + 2]
            index = programMain[position + 3]
            programMain[index] = first * second
            position += length
        elif mode == 3:
            indexMode = str(opCodeInstruction[0])[-3:-2]
            index = programMain[position + 1] if len(indexMode) == 0 or int(indexMode) == 0 else position + 1
            newInput = int(inputInts.pop(0))
            programMain[index] = newInput
            position += length
        elif mode == 4:
            indexMode = str(opCodeInstruction[0])[-3:-2]
            index = programMain[position + 1] if len(indexMode) == 0 or int(indexMode) == 0 else position + 1
            # print("output: " + str(programMain[index]))
            output = programMain[index]
            position += length
        elif mode == 5:
            firstMode = str(opCodeInstruction[0])[-3:-2]
            first = programMain[programMain[position + 1]] if len(firstMode) == 0 or int(firstMode) == 0 else programMain[position + 1]
            secondMode = str(opCodeInstruction[0])[-4:-3]
            second = programMain[programMain[position + 2]] if len(secondMode) == 0 or int(secondMode) == 0 else programMain[position + 2]            
            if first != 0:
                position = second
            else:
                position += length
        elif mode == 6:
            firstMode = str(opCodeInstruction[0])[-3:-2]
            first = programMain[programMain[position + 1]] if len(firstMode) == 0 or int(firstMode) == 0 else programMain[position + 1]
            secondMode = str(opCodeInstruction[0])[-4:-3]
            second = programMain[programMain[position + 2]] if len(secondMode) == 0 or int(secondMode) == 0 else programMain[position + 2]            
            if first == 0:
                position = second
            else:
                position += length
        elif mode == 7:
            firstMode = str(opCodeInstruction[0])[-3:-2]
            first = programMain[programMain[position + 1]] if len(firstMode) == 0 or int(firstMode) == 0 else programMain[position + 1]
            secondMode = str(opCodeInstruction[0])[-4:-3]
            second = programMain[programMain[position + 2]] if len(secondMode) == 0 or int(secondMode) == 0 else programMain[position + 2]            
            index = programMain[position + 3]
            value = 0
            if first < second:
                value = 1
            programMain[index] = value
            position += length
        elif mode == 8:
            firstMode = str(opCodeInstruction[0])[-3:-2]
            first = programMain[programMain[position + 1]] if len(firstMode) == 0 or int(firstMode) == 0 else programMain[position + 1]
            secondMode = str(opCodeInstruction[0])[-4:-3]
            second = programMain[programMain[position + 2]] if len(secondMode) == 0 or int(secondMode) == 0 else programMain[position + 2]            
            index = programMain[position + 3]
            value = 0
            if first == second:
                value = 1
            programMain[index] = value
            position += length
        elif mode == 9:
            return output
        else:
            raise ValueError('Unknown opcode')
    return output

if __name__ == "__main__":
    input = [int(code) for code in open("input.txt").read().split(",")]
    print(function(input))
    