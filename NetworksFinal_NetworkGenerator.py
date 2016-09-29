#http://www.brokenairplane.com/2011/05/wikipedia-game-python-philosophy.html
'''
This code tries to loop through wikipedia pages and create a network 
using the hyperlinks. 

So far, I'm trying to look at the format of each Wikipedia page to
determine a way to find each hyperlink
'''

import urllib2

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

dict = {} #format: key : value => hyperlink : nodeNumber
#so we can assign new nodes a unique number, starting from 1
nodeCount = 1

#each element of this list is a line in the txt file
#we first edit this list, and then at the very end
#we put everything in the list into a txt file
fileList = []
dictList = []

#get a list of the hyperlinks at the specified url
def getPages (url):
  #print(url)
  #open the page at specified URL
  global dict
  global nodeCount
  global fileList

  #add this page to the dict if it doesn't already exist
  if not dict.has_key(url):
    dict[url] = nodeCount
    #write to the fileList
    fileList.append(str(nodeCount)+'\t')
    nodeCount += 1;

  #open the page
  #try:
  infile = opener.open(url)
  page = infile.read()
  #except urllib2.HTTPError as e:
    #print("error at:",url)
    #return []
  #Find the first <p> tag for the main body and the last </p>
  #this is to contain mainP to just the actual text we want to search
  mainP = page[page.find('<p>'):page.rfind('</p>')]
  #list of hyperlinked pages' urls
  pages = []
  indices = []
  index = 0
  #get a list of hyperlinks in pages[]
  #keep searching for hyperlinks while running the mainP.find() != -1

  #make list of indices on page
  while index < len(mainP) and index != -1:
    index = mainP.find('<a href="/wiki/',index + 15)
    if index != -1:
      indices.append(index + 15)

  #print('page')

  #find all page links
  for index in indices:
    page = mainP[index:mainP.find('"',index)] #Find the first href for the link)
    #add the page to the list pages[]
    if not ':' in page and not 'List' in page and not ' ' in page:
      pageURL = 'https://en.wikipedia.org/wiki/'+page
      #add the number the page is associated with
      #first make sure it isn't already defined in the dict
      if dict.has_key(pageURL):
        pages.append(dict[pageURL])
      else:
        dict[pageURL] = nodeCount
        pages.append(nodeCount)
        #write to the fileList
        fileList.append(str(nodeCount)+'\t')
        dictList.append(str(nodeCount)+'\t'+pageURL)
        nodeCount += 1;
    #get rid of this first part of the mainP so we can keep
    #searching for hyperlinks in the rest of the string
 #   mainP = mainP[index+1:]
  return pages

#since dictionaries are for searching for values based on keys,
#this function searches for keys based on values
#so basically makes the dictionary two-way
def getKey(value):
  #get the key at the specified value
  global dict
  return dict.keys()[dict.values().index(value)]

def writeToFiles(depth):
  global fileList, dictList
  #add 0s to make all the lines the same length
  length = -1
  for i in fileList:
    l = i.count('\t')
    if l > length:
      length = l
  print ('# of cols:', length)
  for i in range (0, len(fileList)):
    l = fileList[i].count('\t')
    for j in range(length-l):
      fileList[i] += '0\t'

  #WRITE EVERYTHING WE PUT IN FILELIST INTO A TXT FILE
  #create a file called 'wikipage' to store one example page
  #this is just to see what the page looks like when you import it with python
  f = open('network'+str(depth)+'.txt', 'w')
  for line in fileList:
    f.write(line+'\n')
  f.close()

  f = open('meaning'+str(depth)+'.txt', 'w')
  for line in dictList:
    f.write(line+'\n')
  f.close()

def doNetwork(page, iteration, maxIteration):
  #recursive function
  #finds all the neighbors at page and adds them to the fileList
  #we the run this function for each of the neighbors

  #for now, we want to stop after a certain depth, which is what
  #iteration and maxIteration does. 
  global fileList
  global dict
  pages = getPages(page)
  #write the neighbors in the file
  fileIndex = dict[page]
  for n in pages:
    fileList[fileIndex-1] += str(n)+'\t'
  #reiterate
  if iteration >= maxIteration:
    return;
  for n in pages:
    doNetwork(getKey(n), iteration+1, maxIteration)

#OK NOW FOR THE ACTUAL PROGRAMMMM
#NO MORE BS FUNCTIONS HAHA


#RUN THIS ENTIRE PROGRAM USING RECURSION
maxDepth = input('Max depth? (Integer): ')
doNetwork('https://en.wikipedia.org/wiki/Network_science', 1, maxDepth)

writeToFiles(maxDepth)
