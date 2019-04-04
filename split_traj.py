#!/usr/bin/env python

import sys
import os

"""takes the massive pdb from a trajectory (in vmd save all as pdb) as input.
splits the batch pdb up into constituent pdbs for analysis, each in individual directories"""
with open(sys.argv[1]) as f:
	i=0
	directory = "frame_"+str(i)
        if not os.path.exists(directory):
                os.makedirs(directory)
        filepath=directory+"/f_"+str(i)+".pdb"
	out = open(filepath,"w")
	print "Parsing frame %d" % i
	for line in f:
                words = line.split()
		if words[0].lower() == "atom":	
			out.write(line)
		elif words[0].lower() == "end":
			out.write(line)
			out.close()	
			i+=1
			directory = "frame_"+str(i)
			if not os.path.exists(directory):
       				os.makedirs(directory)
       			filepath=directory+"/f_"+str(i)+".pdb"
       			out = open(filepath,"w")


			print "Parsing frame %d" % i


print "done now. "

print("Delete \""+sys.argv[1]+"\"? \nSize: %0.2f MB.") % (float(os.stat(sys.argv[1]).st_size/1000000.0))

ans=str(raw_input("[y/n]"))

if ans.lower() == "y":
	os.remove(sys.argv[1])

			
