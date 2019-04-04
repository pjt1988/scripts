from math import sqrt
import time

"""takes a range of frames (0..X) and finds active and QM regions based on a set of geometric considerations. Defined below for ease of manipulation

Defined by residues, ie we write down all constituent atoms of any residue having at least one atom within the provided radius around the target
residues

the directories are frame_X, with the relevant pdbs being f_X.pdb.

Constituent atoms are written into respective files for use in later input generation

The script contains a timer to let the user know when it's time to go home and leave everything else running overnight

"""

t0 = time.time()

def dis(x,y,z,xref,yref,zref):
	return sqrt((xref-x) ** 2 + (yref-y) ** 2 + (zref - z) ** 2)

class resinfo():

	def __init__(self):
		self.resn=""
		self.x=[]
		self.y=[]
		self.z=[]

start = int(input("Start (inclusive): "))
stop = int(input("Stop (inclusive): "))
stride = int(input("Step size: "))

#radii set here ... modify them as needed
r_qm_sys = 3.5
r_qm_wat = 3.5

r_ac_sys = 7.00
r_ac_wat = 7.00

#r_qm_ghost = 8.0

ref_ids = [1,2,3,4];  #the resid around which to look..

print "Reference resid: "+str(ref_ids[0:])

f_dyn = open("dyn_data", "a")

for i in range(start,stop+1,stride):
	direct="frame_"+str(i)+"/"
	pdbfile=direct+"f_"+str(i)+".pdb"
	qm_out=direct+"f_"+str(i)+"_qmres"
	ac_out=direct+"f_"+str(i)+"_acres_all"
	ac_out_s=direct+"f_"+str(i)+"_acres_sys"
	ac_out_w=direct+"f_"+str(i)+"_acres_wat"
	gh_out=direct+"f_"+str(i)+"_ghres"

	pdb = {}

	with open(pdbfile, "r") as f:
		for line in f:
			line=line.replace(" X", " ") #gets rid of that X next to the resname
                	words = line.split()
			if words[0].lower() == "atom":

				id = int(words[4])
				if id not in pdb:
					pdb[id] = resinfo()
				pdb[id].resn = str(words[3])
				pdb[id].x.append(float(words[5]))
				pdb[id].y.append(float(words[6]))
				pdb[id].z.append(float(words[7]))

	qm = []
	ac = []
	qm_wat = []
	ac_wat = []
	ac_sys = []
	#gh = []

	for j in pdb:
		if j not in qm:
			for k in range(len(pdb[j].x)):
				for resid_cen in ref_ids:
					for l in range(len(pdb[resid_cen].x)):
					#	if pdb[j].resn != "WAT":
						if dis(pdb[j].x[k],pdb[j].y[k],pdb[j].z[k],pdb[resid_cen].x[l],pdb[resid_cen].y[l],pdb[resid_cen].z[l]) <= r_qm_sys:
							qm.append(j)
							if(j not in ref_ids):
								ac_wat.append(j)
							else:
								ac_sys.append(j)
							ac.append(j)
							break
						elif dis(pdb[j].x[k],pdb[j].y[k],pdb[j].z[k],pdb[resid_cen].x[l],pdb[resid_cen].y[l],pdb[resid_cen].z[l]) <= r_ac_sys:
							ac.append(j)
							if(j not in ref_ids):
								ac_wat.append(j)
							else:
								ac_sys.append(j)
							ac.append(j)
							break
		

	qm = list(set(qm))
	ac = list(set(ac))
	#gh = list(set(gh))
	qm_wat = list(set(qm_wat))
	ac_wat = list(set(ac_wat))
	ac_sys = list(set(ac_sys))

	qmat_count = 0
	acat_count = 0	
	#gh_count = 0
	for j in qm:
		qmat_count += len(pdb[j].x)

	for j in ac:
		acat_count += len(pdb[j].x)
	
	#for j in gh:
	#	gh_count += len(pdb[j].x)
	#
	f_qm = open(qm_out,"w")
	for j in qm:
		f_qm.write(str(j)+" ",)
	f_qm.close()

	f_ac = open(ac_out,"w")
	for j in ac:
		f_ac.write(str(j)+" ",)
	f_ac.close()

	f_gh = open(gh_out,"w")
	for j in ac:
		f_gh.write(str(j)+" ",)
	f_gh.close()

	f_acw = open(ac_out_w, "w")
	for j in ac_wat:
		f_acw.write(str(j)+" ",)
	f_acw.close()

	f_acs = open(ac_out_s,"w")
	for j in ac_sys:
		f_acs.write(str(j)+" ",)
	f_acs.close()
	

	f_dyn.write("Frame %d qm_at: %d qm_res: %d ac_at: %d ac_res %d qm_wat: %d ac_wat: %d ... elapsed: %0.2f s \n" % (i, qmat_count, len(qm), acat_count, len(ac), len(qm_wat), len(ac_wat), time.time() - t0) )
	print "Frame %d qm_at: %d qm_res: %d ac_at: %d ac_res %d qm_wat: %d ac_wat: %d gh_res: %d gh_at: %d ... elapsed: %0.2f s" % (i, qmat_count, len(qm), acat_count, len(ac), len(qm_wat), len(ac_wat), len(ac), acat_count, time.time() - t0)


f_dyn.close()
