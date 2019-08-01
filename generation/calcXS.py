#!/usr/bin/python

import sys
import fnmatch
import os


def findXS (filename):
    objFile = open (filename, 'r')
    fileContent = objFile.read ().split ()
    return fileContent[-4]



if __name__ == '__main__':

    if len (sys.argv) < 2:
        print ('base folder of the sample missing')
        sys.exit ()
        
    matches = []
    myfilenames = []
    for root, dirnames, filenames in os.walk (sys.argv[1]):
        for filename in fnmatch.filter(filenames, '*banner.txt'):
            matches.append (os.path.join (root, filename))
            myfilenames.append (filename)

   
    XS = [float (findXS (file)) for file in matches]
    print sum (XS) / len (XS)


    if len (sys.argv) > 2:
    	print ('\n')
    	for i in range (len(XS)):
    		print (myfilenames[i] + ':\t' + str (XS[i]) + ' pb')
        print ('\n')
        print ('average XS: ' + str (sum (XS) / len (XS)) + ' pb')


