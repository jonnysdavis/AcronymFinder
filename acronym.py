__author__ = 'Jonny'

shorthand = ""
expanded = ""
cofidence = False

class acronym:

    def acronymLength():
        return shorthand.len()

def expandedLength():
    return expanded.len()

def acronym(shorthanded, expand):
    shorthand = shorthanded
    expanded = expand
    confidence = True


def acronym(isAcronym, text):
    if(isAcronym == True):
        shorthand = text
        expanded = "?"
    else:
        expanded = text
        shorthand = "convert to acronym"


