#!/usr/bin/env python

import sys
from math import sqrt

def distance(cx,cy,cz,x,y,z):
	r=sqrt(((cx-x) ** 2) + ((cy-y) ** 2) + ((cz-z) ** 2))
	return r

ATOMSYM,RESNAME,RESNUM,X,Y,Z = [], [], [], [], [], []
with open(sys.argv[1]) as f:
	for line in f:
		words = line.split()
		if words[0].lower() != "end" and words[0].lower() != "ter" and words[0].lower() != "remark":
			ATOMSYM.append(str(words[2]))
			RESNAME.append(str(words[3]))
			RESNUM.append(int(words[4]))
			X.append(float(words[5]))
	        	Y.append(float(words[6]))
                	Z.append(float(words[7]))

print "System read and processed. %d entries found \n" % len(X)

cx,cy,cz=0,0,0
for i in range(len(X)):
	cx+=X[i]
	cy+=Y[i]
	cz+=Z[i]

cx/=len(X)
cy/=len(Y)
cz/=len(Z)

print "The center of the system is found at (%.4f,%.4f,%.4f) \n" % (cx,cy,cz)

min_index,min_radius=0,100
max_index,max_radius=0,0

for i in range(len(X)):
	dis = distance(cx,cy,cz,X[i],Y[i],Z[i])
	if dis < min_radius:
		min_radius=dis
		min_index=i
	if dis > max_radius:
		max_radius=dis
		max_index=i

print "The closest atom to the center is at resid %d (%s), with type \"%s\". It's %.4f A from the center \n" % (RESNUM[min_index],RESNAME[min_index],ATOMSYM[min_index],min_radius)

print "The farthest atom is at resid %d (%s), with type  \"%s\". It's %.4f A from the center \n" % (RESNUM[max_index],RESNAME[max_index],ATOMSYM[max_index],max_radius)


