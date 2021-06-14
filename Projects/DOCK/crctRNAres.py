# import modules
import os,sys
import Bio
from Bio.PDB import *
#automating path defination
cwd = os.getcwd()
input = os.path.join (cwd, "prerec.pdb")# sets condition- i/p file to be named as "prerec.pdb"
# parse pdb
parser = PDBParser()
RNAstrctr = parser.get_structure("prerec", r"prerec.pdb")
#amends the residue format
for model in RNAstrctr:
    for chain in model:
        for res in chain:
            if res.resname[1].isspace() == True:
                res.resname = res.resname.replace(res.resname, res.resname[::-1])
            else:
                res.resname = res.resname
#writes new file
io= PDBIO ()
io.set_structure(RNAstrctr)
io.save("rec.pdb")