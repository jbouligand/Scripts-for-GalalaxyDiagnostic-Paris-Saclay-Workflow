#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Christophe Habib'
__copyright__ = 'Copyright (C) 2017 GMPH'
__license__ = 'GNU General Public License'
__version__ = '1.0.0'
__email__ = 'christophe.habib@gmail.com'
__status__ = 'prod'

"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

import sys,os,argparse


def initINFOS(infosHeader):
	dico ={}
	for i in infosHeader:
		dico[i]="."
	return dico

def parseINFOcol(lignes,infosHeader,oldHeader):

	col = oldHeader.split("\t")

	#to_write = "\t".join(col[0:7])+"\t"+"\t".join(infosHeader)+"\t"+"\t".join(col[8:])
	to_write = "\t".join(col[0:7])+"\t"+"\t".join(col[8:]).strip()+"\t"+"\t".join(infosHeader)+"\n"

	for ligne in lignes :
		col = ligne.split("\t")
		variants = col[4].split(",")[:-1]
		print variants
		annotations = getINFOcol(col[7],infosHeader)
		if variants == [] :
			for annotation in annotations :
				to_write+="\t".join(col[0:7])+"\t"+"\t".join(col[8:]).strip()+"\t"+annotation+"\n"	
		else:
			for var,annotation in zip(variants,annotations):
				col[4]=var
				to_write+="\t".join(col[0:7])+"\t"+"\t".join(col[8:]).strip()+"\t"+annotation+"\n"			
			#	to_write+="\t".join(col[0:7])+"\t"+getINFOcol(col[7],infosHeader)+"\t"+"\t".join(col[8:])
			#	to_write+="\t".join(col[0:7])+"\t"+"\t".join(col[8:]).strip()+"\t"+getINFOcol(col[7],infosHeader)+"\n"

	return to_write

		 
def getINFOcol(allInfos,infosHeader):
	infos = initINFOS(infosHeader)
	cols = allInfos.split(";")
	annotations = []
	for indice in range(len(cols)) :
		elts = cols[indice].split("=")
		if infos.has_key(elts[0]):
			if infos[elts[0]]=='.' :
				infos[elts[0]]=str(elts[1])
	 	#elif elts==['ALLELE_END'] or indice == (len(cols)-1)  :
		#elif indice == (len(cols)-1)  :
	annotations.append("\t".join([infos[i] for i in infosHeader]))
	infos = initINFOS(infosHeader)

	return annotations
	
		
def getINFOheader(infos,infosHeader):
	fields = []
	cols = infos.split(";")
#	for col in cols[:-1]:
	for col in cols:
		if col.split("=")[0] not in fields :
			fields.append(col.split("=")[0])
	if len(fields)>len(infosHeader):
		return fields
	else:
		return infosHeader
		

def keepRelevant(filin,filout):
	output=filout
	sortie = open(output,"w")
	
	to_keep = ["##fileformat","##ALT=","##GATKCommandLine","##INFO","##reference","##FORMAT","##SnpEff"]

	entree = open(filin)
	lignes = entree.readlines()
	
	chromosom = []
	infosHeader = []

	for ligne in lignes :
		if ligne.startswith("chr"):
			if ligne.count("\t<NON_REF>\t") == 0 :
				chromosom.append(ligne)
				infosHeader = getINFOheader(ligne.split("\t")[7], infosHeader)
		elif ligne.startswith("#CHROM"):
			oldHeader=ligne
		else:			
			col=ligne.split("=")
			if col[0] in to_keep:
				sortie.write(ligne)
	if 'ALLELE_END' in infosHeader:
		infosHeader.remove('ALLELE_END')
	if 'ANNOVAR_DATE' in infosHeader:
		infosHeader.remove('ANNOVAR_DATE')

	sortie.write(parseINFOcol(chromosom,infosHeader,oldHeader))
							
	entree.close()
	sortie.close()



if __name__ == '__main__':
	parser=argparse.ArgumentParser(usage="prog -i filin -o filout")
	parser.add_argument("-i","--infile",dest="infilename",help="gVCF output from GATK",default=None)
	parser.add_argument("-o","--outfile",dest="outfilename",help="Parsed VCF",default=None)

	args=parser.parse_args()

	if args.infilename is None :
		parser.error("Input file (-i) is missing.")
	if args.outfilename is None :
		parser.error("Output filename (-o) is missing.")


	keepRelevant(args.infilename,args.outfilename)



	
