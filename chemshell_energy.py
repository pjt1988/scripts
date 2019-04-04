#!/usr/bin/env python

import sys

f=open(sys.argv[1])
lines=f.readlines()

en = []

for i in lines:
	if len(i.strip()) > 0:
		words = (i.strip()).split()
		if words[0].lower() == "energy":
			if words[1].lower() == "calculation" and words[2].lower() == "finished,":
				en.append(float(words[4]))

print "ITER 	\t E \t dE_0 (kcal/mol)    dE_prev. (kcal/mol) "
print " 0   \t %f \t  0.0000 \t  0.0000 " % en[0]
for i in range(1,len(en)):
	print " %d \t %.6f \t %.4f \t %.4f " % (i, en[i], (float(en[i]-en[0]))*627.509469, (float(en[i] - en[i-1]))*627.509469)	
	
