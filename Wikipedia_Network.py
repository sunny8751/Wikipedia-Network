'''
This code tries to loop through wikipedia pages and create a network 
using the hyperlinks. 

So far, I'm trying to look at the format of each Wikipedia page to
determine a way to find each hyperlink
'''

import urllib.request
import re

#create a file called 'wikipage' to store one example page
#this is just to see what the page looks like when you import it with python
f = open('wikipage.txt', 'w')

def getPage (target):
  #open the page at specified URL
  url = 'https://en.wikipedia.org/wiki/'+target
  #page = urllib.request.urlopen('https://en.wikipedia.org/wiki/Network_theory')
  page = urllib.request.urlopen(url)
  #what are you doing between ^^ and line 22 (does the page url matter here?)??
  #convert it to a string
  string = page.read().decode('utf-8')
  #search string for: title="
  #locations = [pos+7 for pos, char in enumerate(string) if char == 'title="']
  #locations = [m.start() for m in re.finditer('title="', string)]
  l1 = string.split('title="')
  neighbors = []
  s=''
  for i in l1:
    page = i.split('"')[0]
    #neighbors.append(page)
    s += page
  return s

#print (getPage('computer_science'))
#this code tries to fi1l some unicode error when you try to write the string to the file
#was working on this, and probably doesn't work lol
s = getPage('computer_science')
f.write(s)
f.close()
