import csv
import os
import errno

def readDeckList(fileNameIN, fileNameOUT):
    cards = {}    
    try:
        with open(fileNameIN, 'r') as decks:
            for line in decks:
                line = line.replace("\n", "").replace(",","")
                if(line == "" or line == "Sideboard" or line == "Deck"):
                    continue    
                elif(line[2:] not in cards):
                    cards[line[2:]] = int(line[0])
                else:
                    cards[line[2:]] += int(line[0]) 
            decks.close()
    except IOError:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), fileNameIN)

    try:
        with open(fileNameOUT, 'w') as f:
            for key in cards.keys():
                f.write("%s,%s\n"%(key,cards[key]))
        f.close()
    except IOError:
        raise IOError("Failed to create file {}".format(fileNameOUT))


'''
    for i in range(16):
        line = ""
        while line != "Deck":
            line = decks.readline().strip('\n').replace(',', '')
            if(line == "" or line == "Sideboard" or line == "Deck"):
                continue    
            elif(line[2:] not in cards):
                cards[line[2:]] = int(line[0])
            else:
                cards[line[2:]] += int(line[0]) 
''' 
readDeckList("4decks.txt", "cards2.csv")