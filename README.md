# scripts

A small collection of scripts I wrote over the course of my PhD work that made analyzing MD trajectories easier. 

split_traj.py\n
In VMD, save the entire trajectory as a PDB (at least all frames of interest), and use that as an argument for the script. It will split the file into constituent PDBs, and save each one in its own directory


dynamic_regions.py\n
This script will write out all residues and constituent atoms of any residue within a given radius of any atoms within selected residues. The script differentiates between QM and active regions for later 
calculations. Given that each frame needs to be checked once, this can be time consuming.


chemshell_energy.py\n
Greps absolute energy and energy changes from a chemshell log file in kcal/mol


find_centermost_atom.py\n
Finds the centermost atom in a PDB. Useful for determining boundary conditions in subsequent calculations


transpose.sh\n
Transposes an array, ie either a line of text into multiple lines, or vice versa. Output is saved as $INPUT_transpose
