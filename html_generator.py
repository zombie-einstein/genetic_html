import xml.etree.ElementTree as ET
import random as rnd
import genetics as gen
from bs4 import BeautifulSoup as BS

testPage = open("Test.html",'w')

htmlA = '''<html><body><h1 style="color:#ff00ff;background-color:#a5e109;width:50%;">Header A</h1><div style="color: #ff0000">DIV 1A<div style="background-color: #1099aa">SUB-DIV 1A</div></div><div style="background-color: #ff0000">DIV 2B</div></body></html>'''

htmlB = '''<html><body><h1 style="color: #ffff00">Header B</h1><div style="color: #00f000">DIV 1B</div><div style="background-color: #ff00ff">DIV 2B</div></body></html>'''

soupTestA = BS(htmlA, "lxml")
soupTestB = BS(htmlB, "lxml")

testPage.write(str(soupTestA))
testPage.write(str(soupTestB))

for i in xrange(1000):
    gen.recMateSoup(soupTestA.body,soupTestB.body,0.5)
    gen.mutate(soupTestA,0.01)
    gen.mutate(soupTestB,0.01)
    testPage.write(str(soupTestA)+"\n")

testPage.write(str(soupTestA)+"\n")

testPage.close()