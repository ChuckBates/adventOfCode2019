import math
import sys
import itertools

def function( input ):
    ampInputs = [5,6,7,8,9]
    bestOutput = 0

    for possibleCombo in itertools.permutations(ampInputs, 5):
        ampStates = {}
        ampStates["A"] = [0, input.copy(), 0, 0]            
        ampStates["B"] = [0, input.copy(), 0, 0]            
        ampStates["C"] = [0, input.copy(), 0, 0]            
        ampStates["D"] = [0, input.copy(), 0, 0]            
        ampStates["E"] = [0, input.copy(), 0, 0]       
        first = True
        while True:
            aInputs = [possibleCombo[0],ampStates["E"][3]] if first else ampStates["E"][3]
            ampStates["A"] = intCodeComputer(ampStates["A"], aInputs)  

            bInputs = [possibleCombo[1],ampStates["A"][3]] if first else ampStates["A"][3]
            ampStates["B"] = intCodeComputer(ampStates["B"], bInputs)  

            cInputs = [possibleCombo[2],ampStates["B"][3]] if first else ampStates["B"][3]
            ampStates["C"] = intCodeComputer(ampStates["C"], cInputs)   

            dInputs = [possibleCombo[3],ampStates["C"][3]] if first else ampStates["C"][3]
            ampStates["D"] = intCodeComputer(ampStates["D"], dInputs)   

            eInputs = [possibleCombo[4],ampStates["D"][3]] if first else ampStates["D"][3]
            ampStates["E"] = intCodeComputer(ampStates["E"], eInputs)   
            
            if ampStates["E"][0] == 9:
                print("Amp E halted")
                break
            if first:
                first = False
        if ampStates["E"][3] > bestOutput:
            bestOutput = ampStates["E"][3]
    return bestOutput

def intCodeComputer( inputParams,inputInts ):
    programMain = inputParams[1].copy()
    position = inputParams[2]
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
            if isinstance(inputInts, list):
                newInput = int(inputInts.pop(0))
            else:
                newInput = inputInts
            programMain[index] = newInput
            position += length
        elif mode == 4:
            indexMode = str(opCodeInstruction[0])[-3:-2]
            index = programMain[position + 1] if len(indexMode) == 0 or int(indexMode) == 0 else position + 1
            # print("output: " + str(programMain[index]))
            output = programMain[index]
            position += length
            return [4, programMain.copy(), position, output]
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
            return [9, programMain.copy(), position, inputParams[3]]
        else:
            raise ValueError('Unknown opcode')
    # return output

if __name__ == "__main__":
    input = [int(code) for code in open("input.txt").read().split(",")]
    print(function(input))
    