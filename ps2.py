##########################################
#   
#   Author:  Noah Haskell
#   Date Created: 10-19-2015
#   Date Last Modified
#   Program Name: ps2.py
#
##########################################
import os            ##You will want these for access
import os.path       ##to the file system. See the documentation 
import re

#1
def fibToMe(l):
	"""precondition: l is an integer
postcondition: return the number in the fibonacci series which is the first 
with l or more digits.
fibonacci number: 0 1 1 2 3 5 8 13 21 34 55 89 144
number in series: 0 1 2 3 4 5 6 7  8  9  10 11 12
fibToMe(2) -> 7
fibToMe(3) -> 12
"""
	fibsum = 1
	fibsumprev = 0
	pos = 1
	while (len(str(fibsum)) <= l-1):
		temp = fibsum
		fibsum = fibsum + fibsumprev
		fibsumprev = temp
		pos +=1
	return pos
#test for 1
print("pass fibToMe(2) == 7" if (fibToMe(2) == 7) else "fail fibToMe(2) == 7 returns " + str(fibToMe(2)) )
print("pass fibToMe(3) == 12" if (fibToMe(3) == 12) else "fail fibToMe(2) == 12 returns " + str(fibToMe(3)) )


#2
def specialSum(n):
	"""precondition: n is a positive integer.
postconditions: return the sum of all integers 1 to n (inclusive) divisible by 
2 or 3, but not 5.
specialSum(10) -> 32
specialSum(20) -> 92
"""
	summe = []
	for num in range(1, n+1):
		if (num%2 == 0 or num%3 == 0) and num%5 != 0:
			summe.append(num)
	#print(summe)
	return sum(summe)

print("pass specialSum(10) == 32" if (specialSum(10) == 32) else "fail specialSum(10) == 32 returns " + str(specialSum(10)))
print("pass specialSum(20) == 92" if (specialSum(20) == 92) else "fail specialSum(20) == 92 returns " + str(specialSum(20)))
print("pass specialSum(12) == 44" if (specialSum(12) == 44) else "fail specialSum(12) == 44 returns " + str(specialSum(12)))
#3
def fileContains(filename, word, recurse=False):
	"""precondition:  filename and word are strings.
postcondition:  If the file filename is a directory, inspect the contents of 
all files in the directory and return True if word appears in any of them.
If the filename is a regular file and if the string word is found in the 
file return True
If the file filename does not exist, return False
Otherwise, return False
##Challenge: implement the recurse option to recursively check files in 
subdirectories if recurse is True
"""
	pattern = re.compile(word)
	
	if os.path.isdir(filename):
		#inspect all files in the directory
		for item in os.listdir(filename):
			try:
				if (pattern.match(line) for line in open(filename + '/' + item))!= None:
					return True
				
			except IsADirectoryError:
				if recurse:
					if fileContains(item, word, True) == True:
						return True
	else:
		try:
			if (pattern.match(line) for line in open(filename))!= None:
				return True
		except FileNotFoundError:
			return False	
	
print("word found" if fileContains(".", "precondition:") else "failure to find ")
print("word found recursivly" if fileContains("..", "precondition:", True) else "failure to find")
#print("word that wasn't supposed to be found not found recursivly" if fileContains("/tmp", "turkeychickenfdfdsale", True) else "failure to not find")
#That last test case didn't work on the cs server

#4
def countFilesWithExtension(directory, extension):
	"""prec: directory is a string, extension is a string.
postc:  return a -1 if the directory does not exist.
Otherwise return a count of all files in the directory with extension
.extension (be nice to the user...  prepend a '.' if they omit it.  if they 
include it, do not double it)
"""	
	count = 0
	if extension[0] != ".":
		extension = "." + extension
	if os.path.isdir(directory):
		for item in os.listdir(directory):
			if item.endswith(extension) == True:
				count +=1
	else:
		return(-1)
	return count

print(str(countFilesWithExtension(".", ".py")) + " .py file found in the current directory")
print(str(countFilesWithExtension(".", "py")) + " py file found in the current directory. I added a dot for you")

#5
def assort(counts):
	"""prec:  counts is a dictionary whose keys are words
and whose values are positive integers.
postc:  return a dictionary whose keys are integers
and whose values are lists containing all words paired
with the integers, sorted alphbeticallly.  Here is an example
d = {"cat":3, "dog":1, "pig":1, "horse":3, "lemur":4}
assort(d) -> {1: ["dog", "pig"], 3:["cat", "dog"], 4:["lemur"]}
"""
	assorted = {}
	
	keylist = list(counts.keys())
	for key in keylist:
		assorted[counts[key]] = []
	for key in keylist:
		assorted[counts[key]].append(key)
		assorted[counts[key]].sort()
	return assorted
d = {"cat":3, "dog":1, "pig":1, "horse":3, "lemur":4}
print( "Passorted" if assort(d) == {1: ["dog", "pig"], 3:["cat", "horse"], 4:["lemur"]} else "Failoreted:" + str(assort(d)))

#6
#helper function
def ratecloseness(str1, str2):
	"""Precon: str1 and str2 are strings
postcon: returns the number of characters in str2 that are in str1, unless they are the same string, then return -1
"""
	closeness= 0
	if str1 == str2:
		return -1
	for char in str1:
		i = str2.find(char)
		if i >=0:
			str2 = str2[:i] + str2[i+1:]
			closeness += 1
	return closeness
	
def aMatchMadeAtNCSSM(username):
	"""precondition: username is a valid username on the cs server (you can use
your username to test)
postcondition: return a list containing 1 or more valid usernames that share
the most characters (apositionally) with the given username (duplicate letters
should only boost the count if they are duplicated in both names)
You may use home directory names as a valid proxy for usernames.  Remember that
user home directories live in: /home/ and associated subdirectories
""" 
	closenessdict = {}
	for uname in os.listdir("/home/"):
		if uname[:2] ==  "20" and os.path.isdir("/home/" + uname):
			try:
				for uname2 in os.listdir("/home/" + uname):
					closenessdict[uname2] = ratecloseness(username, uname2)
			except PermissionError:
				closenessdict[uname] = ratecloseness(username, uname)
		else:
			closenessdict[uname] = ratecloseness(username, uname)
	matchbook = assort(closenessdict)
	for i in range(len(username), 0, -1):
		try:
			return matchbook[i]
		except KeyError: #If we get keyerror then there isn't a value there
			pass
if 'nsh' in os.uname()[1]:
	print("Noah Haskell's Computer, unable to test")
else:
	print(aMatchMadeAtNCSSM("haskell16n"))

#7
def ionics(filename, gimmieGimmie, delim=","):
	"""precondition: filename is a valid filename.  filename's contents are 
columnar data delimited by a character, delim (by default ',').  The columns 
are numbered from 0 to n-1 (with n being the number of columns).
gimmieGimmie is a list of integers that are valid column numbers in the file.
postcondition: create a file with the same name as the original with a ".out" 
extension.  This file should contain the columns requested via gimmieGimmie,
delimited by delim.
Note: Text of opensampelfile.csv moved to seperate file

ionics(sampleFile.csv, [2,4,6])
will create this file
sampleFile.csv.out
,1,
3,5,7
5,3,1
bird,rat,cow
other,else,farther
"""	
	outputfile = open(filename + ".out", 'w')
	for line in open(filename):
		output = []
		for gim in gimmieGimmie:
			output.append(line.split(",")[gim])
		outputfile.write(','.join(output))
		
ionics("sampleFile.csv", [2,4,6])
index = 0
whatitshouldbe =[ ",1,",
"3,5,7",
"5,3,1",
"bird,rat,cow",
"other,else,farther"
]
for line in open('sampleFile.csv.out'):
	if line.strip() != whatitshouldbe[index]:
		print("Failure, " + line.strip() + " != " + whatitshouldbe[index])
	else:
		print("Pass on line "+ str(index))	
	index +=1
#7 Bonus
def autoDetectDelimitor(filename):
    """precondition: filename is a columnar file as above.
postcondition: autodetect and return the single character delimitor to the best of your ability.
if you are unable to detect, return None
"""
    return None


