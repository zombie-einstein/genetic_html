import genetics as gen
from bs4 import BeautifulSoup as BS
from urllib2 import urlopen as URL

testPage = open("Test.html",'w')

testURLA = URL("https://en.wikipedia.org/wiki/Physics")
testURLB = URL("https://en.wikipedia.org/wiki/Cellular_automaton")

htmlA = '''<html><head><title>Sample "Hello, World" Application</title></head><body bgcolor=white><table border="0" cellpadding="10">#<tr><td><img src="images/springsource.png"></td><td><h1>Sample "Hello, World" Application</h1></td></tr></table><p>This is the home page for the HelloWorld Web application. </p><p>To prove that they work, you can execute either of the following links:<ul><li>To a <a href="hello.jsp">JSP page</a>.<li>To a <a href="hello">servlet</a>.</ul></body></html>'''

htmlB = '''<html><head><title>Example</title></head><body><h1 style="color: #ffff00">Header B</h1><div style="color: #00f000">DIV 1B</div><div style="background-color: #ff00ff">DIV 2B</div></body></html>'''

soupTestA = BS(testURLA, "lxml-xml")
soupTestB = BS(testURLB, "lxml-xml")

testPage.write(str(soupTestA)+"\n")
testPage.write(str(soupTestB)+"\n")

for i in xrange(1):
    gen.recMateSoup(soupTestA,soupTestB,0.5)
    gen.mutate(soupTestA,0.001)
    gen.mutate(soupTestB,0.001)
    #testPage.write(str(soupTestA)+"\n")
#   testPage.write(str(soupTestB)+"\n")
#testPage.write("<html><body>--------------------------------------------</body></html>")
#testPage.write(str(soupTestA)+"\n")
#testPage.write(str(soupTestB)+"\n")

testPage.close()