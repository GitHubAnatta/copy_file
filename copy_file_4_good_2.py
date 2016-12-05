# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 17:05:07 2016

@author: anatta
"""

import os
import shutil
sourcePath = r'H://'
destPath = r'O://test_o/'
ls=os.listdir('.')#list current dir
#print('listing current dir\n')
#print(ls)
for root, dirs, files in os.walk(sourcePath):

    #figure out where we're going
    dest = destPath + root.replace(sourcePath, '')

    #if we're in a directory that doesn't exist in the destination folder
    #then create a new folder
    if not os.path.isdir(dest):
        os.mkdir(dest)
        print 'Directory created at: ' + dest

    #loop through all files in the directory
    for f in files:

        #compute current (old) & new file locations
        oldLoc = root + '\\' + f
        newLoc = dest + '\\' + f

        if not os.path.isfile(newLoc):
            try:
                shutil.copy2(oldLoc, newLoc)
                print 'File ' + f + ' copied.'
            except IOError:
                print 'file "' + f + '" already exists'