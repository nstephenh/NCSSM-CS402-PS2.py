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
    return False


#4
def countFilesWithExtension(directory, extension):
    """prec: directory is a string, extension is a string.
postc:  return a -1 if the directory does not exist.
Otherwise return a count of all files in the directory with extension
.extension (be nice to the user...  prepend a '.' if they omit it.  if they 
include it, do not double it)
"""
    return 0


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
    return {}


#6
def aMatchMadeAtNCSSM(username):
    """precondition: username is a valid username on the cs server (you can use
your username to test)
postcondition: return a list containing 1 or more valid usernames that share
the most characters (apositionally) with the given username (duplicate letters
should only boost the count if they are duplicated in both names)
You may use home directory names as a valid proxy for usernames.  Remember that
user home directories live in: /home/ and associated subdirectories
""" 
    return []


#7
def ionics(filename, gimmieGimmie, delim=","):
    """precondition: filename is a valid filename.  filename's contents are 
columnar data delimited by a character, delim (by default ',').  The columns 
are numbered from 0 to n-1 (with n being the number of columns).
gimmieGimmie is a list of integers that are valid column numbers in the file.
postcondition: create a file with the same name as the original with a ".out" 
extension.  This file should contain the columns requested via gimmieGimmie,
delimited by delim.
sampleFile.csv:
0,0,,1,1,0,
1,2,3,4,5,6,7
7,6,5,4,3,2,1
cat,dog,bird,fish,rat,horse,cow
this,that,other,another,else,further,farther

ionics(sampleFile.csv, [2,4,6])
will create this file
sampleFile.csv.out
,4,
3,5,7
5,3,1
bird,rat,cow
other,else,farther
"""
    pass


#7 Bonus
def autoDetectDelimitor(filename):
    """precondition: filename is a columnar file as above.
postcondition: autodetect and return the single character delimitor to the best of your ability.
if you are unable to detect, return None
"""
    return None


