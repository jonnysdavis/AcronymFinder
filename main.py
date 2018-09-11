__author__ = 'jonnysdavis'
import re

textInput = """
We need to leave ASAP (As Soon As Possible) because
the CIA (Central Intel Agency) is here with the DoD to research RADAR tech
"""

def findAcro (docText):
    acroinput = docText
    #returns a tuple if all the acronyms but not the definitions
    acronyms = re.findall(r'\b(?:[A-Z][a-z]*){2,}', acroinput, re.MULTILINE)
    return acronyms

def findDef (acrolist):
        #Loop over each acronym
    entireList = []
    for acro in acrolist:
        #Look for answer in text
        define = textInput.find(acro)
        entireList.append(define)
    return entireList

if __name__ == '__main__':


    print "This program finds all the acronyms in a given String"
    acroResults = findAcro(textInput)
    print acroResults
    print "Find Acronym locations in String to make finding definition in document doable in future"
    print findDef(acroResults)


