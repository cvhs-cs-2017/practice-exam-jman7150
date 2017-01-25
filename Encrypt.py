"""Write a code that will take (AnyString) and substitute all vowels with
character's like $#%^&* etc..... but DO NOT USE ' or " as any of your characters."""
# the example i got online
def removeVowels(AnyString):
    output = AnyString[0]
    for char in AnyString[1:]:
        if char.lower() not in 'aeiou':
            output += char
    return output
