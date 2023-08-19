# https://qiita.com/iNomaG/items/16081daf103a042ea0fe

from music21 import *


def outputMidi(rhythmArray, keyArray, midiName):

    score = stream.Score()
    notes = []

    Duration_dic = {"1":"whole", "2":"half", "4":"quarter", "8":"eighth", "16":"16th"}

    for i,key in enumerate(keyArray):

        Duration = ""

        if(rhythmArray[i] != None):
            Duration = Duration_dic[rhythmArray[i]]
        
        n = chord.Chord(key)
        n.duration.type = Duration
        notes.append(n)

    score.append(notes)

    fp = score.write('midi', midiName)