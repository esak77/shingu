import urllib
file=urllib.urlopen('http://www.shingu.ac.kr')
htmlcontents = file.read()
print htmlcontents
