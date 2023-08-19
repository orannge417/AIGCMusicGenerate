# output Template: 
# | "A4" 4 | "C5" 4 | "E5" 4 | "D5" 4 | "E5" 4 | "F5" 4 | "E5" 4 | "D5" 4 | "C5" 4 | "B4" 4 | "A4" 4 | "G4" 4 | "F4" 4 | "E4" 4 | "A4" 4 | "C5" 4 | "D5" 4 | "E5" 4 | "F5" 8 | "G5" 8 | "A5" 4 | "G5" 4 | "F5" 4 | "E5" 4 | "D5" 4 | "C5" 4 | "B4" 4 | "A4" 4 | "G4" 4 | "F4" 4 | "E4" 4 | "D4" 4 | "C5" 4 | "E5" 4 | "F5" 4 | "G5" 4 | "A5" 4 | "G5" 4 | "E5" 4 | "D5" 4 | "C5" 4 | "B4" 4 | "A4" 4 | "C5" 4 | "E5" 4 | "D5" 4 | "E5" 4 | "A5" 4 | "F5" 4 | "E5" 4 | "D5" 4 | "C5" 4 | "B4" 4 | "A4" 4 | "G4" 4 | "F4" 4 | "E4" 4 | "A4" 4 | "C5" 4 | "D5" 4 | "E5" 4 | "F5" 8 | "G5" 8 | "A5" 4 | "G5" 4 | "F5" 4 | "E5" 4 | "D5" 4 | "C5" 4 | "B4" 4 | "A4" 4 | "G4" 4 | "F4" 4 | "E4" 4 | "D4" 4 | "C5" 4 | "E5" 4 | "F5" 4 | "G5" 4 | "A5" 4 | "G5" 4 | "E5" 4 | "D5" 4 | "C5" 4 | "B4" 4 | "A4" 4 | "C5" 4 | "E5" 4 | "D5" 4 | "E5" 4 | "A5" 4 | "F5" 4 | "E5" 4 | "D5" 4 | "C5" 4 | "B4" 4 | "A4" 4 | "G4" 4 | "F4" 4 | "E4" 4 | "A4" 4 | "C5" 4 | "D5" 4 | "E5" 4 | "F5" 8 | "G5" 8 | "A5" 4 | "G5" 4 | "F5" 4 | "E5" 4 | "D5" 4 | "C5" 4 | "B4" 4 | "A4" 4 | "G4" 4 | "F4" 4 | "E4" 4 | "D4" 4 |


from outputToArray import outputToArray
from music21Midi import outputMidi
from demo import demo
import os
from time import sleep

dictKey = {1: "C", 2:"C#", 3:"Db", 4:"D", 5:"D#", 6:"Eb",
           7:"E", 8:"F", 9:"F#", 10:"Gb", 11:"G", 12:"G#",
           13:"Ab", 14:"A", 15:"A#", 16:"Bb", 17:"B"}


if __name__ == '__main__' :
    output = input("Please input the abc-Notation outputted from chatGPT\n")
    folderName = input("Name of the folder: \n")
    inputDir = "MIDI//inputs//" + folderName + "//melody.mid"

    try:
        new_dir_path = 'MIDI/inputs/' + folderName
        os.mkdir(new_dir_path)
    except(FileExistsError):
        pass

    print("Select the corresponding number for the key of the generated song:")
    for key in (dictKey):
        print(key,dictKey[key])
    inputKey = dictKey[int(input())]
    print(inputKey, type(inputKey))

    keyArray, rhythmArray = outputToArray(output)

    outputMidi(rhythmArray, keyArray, inputDir)
    sleep(3)

    demo(folderName, inputKey)
    
