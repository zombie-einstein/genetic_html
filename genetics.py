import random as RD
from bs4 import BeautifulSoup as BS
import cssutils as CS

def recMateSoup(a,b,rate):
    "Recursicve mating algorithm based on DFS"
    if not (hasattr(a,'contents') and hasattr(b,'contents')): return
    d = max(len(a.contents),len(b.contents))
    # Want to compare equal number of elements so append with empty elements
    a.contents = a.contents+[None for i in xrange(d-len(a.contents))]
    b.contents = b.contents+[None for i in xrange(d-len(b.contents))]
    for i in xrange(d):
        if RD.random() < rate: a.contents[i],b.contents[i] = b.contents[i],a.contents[i] # Swap elements
        else: recMateSoup(a.contents[i],b.contents[i],rate) # Continue down tree

def mutate(a,rate):
    "DFS iterate over all elements of tree, mutate tags and attributes"
    for i in a.attrs:
        if i == 'style': a.attrs[i] = mutate_style(a.attrs[i],rate)
    if not hasattr(a,'contents'): return
    for i in a.contents: 
        if hasattr(i,'attrs'): mutate(i,rate)
    
        
def mutate_style(a,rate):
        styles = CS.parseStyle(a)
        ret = ""
        for j in styles:
            if RD.random() < rate:
                if "color" in j.name: j.value = randomHexColor()
                elif "px" in j.value: j.value = str(RD.randint(0,1000))+"px"
                elif "%%" in j.value: j.value = str(RD.randint(0,100))+"%%"
            ret += j.name+":"+j.value+";"
        return ret

def randomHexColor():
    r = lambda: RD.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())