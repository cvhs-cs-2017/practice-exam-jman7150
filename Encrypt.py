"""Write a code that will take (AnyString) and substitute all vowels with
character's like $#%^&* etc..... but DO NOT USE ' or " as any of your characters."""
def encryption(e):
    a = "aeiouAEIOU"
    b = ""
    for q in e:
        if q in a:
            q = "#"
        b += q
    return b
print(encryption("AP"))
