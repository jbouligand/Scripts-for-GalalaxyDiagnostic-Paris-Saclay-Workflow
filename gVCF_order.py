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


def def_order(ligne):
	order = ["#CHROM","POS","REF","ALT","QUAL","MQ","FORMAT","__pd____oc__fastq_input1Xbasename__cc__","AF","Func.refGene","Gene.refGene","GeneDetail.refGene","ExonicFunc.refGene","AAChange.refGene","EFF","PopFreqMax","clinvar_20150629","ljb23_pp2hdiv","ljb23_pp2hvar","ExAC_ALL","ExAC_AFR","ExAC_AMR","ExAC_EAS","ExAC_FIN","ExAC_NFE","ExAC_OTH","ExAC_SAS","snp138","ID","BaseQRankSum","ClippingRankSum","FS","MLEAC","MLEAF","QD","ReadPosRankSum","SOR","MQRankSum","AC","AN","DP","FILTER"]
	indices = []
	cols = ligne.strip().split("\t")
	for i in order :
		if i in cols: 
			indices.append(cols.index(i))

	return indices


def reformat_vcf(filin,filout):
	fichier = open(filin)
	lignes = fichier.readlines()
	fichier.close()
	
	fichier = open(filout,"w")
	
	for ligne in lignes : 
		cols= ligne.strip().split("\t")
		if ligne.startswith("##"):
			fichier.write(ligne)
		elif ligne.startswith("#CHROM"):
			order = def_order(ligne)
			fichier.write("\t".join([cols[i] for i in order])+"\n")
		else:
			fichier.write("\t".join([cols[i] for i in order])+"\n")
	
	fichier.close()	
	

if __name__ == '__main__':
	parser=argparse.ArgumentParser(usage="prog -i filin -o filout")
	parser.add_argument("-i","--infile",dest="infilename",help="gVCF output from GATK",default=None)
	parser.add_argument("-o","--outfile",dest="outfilename",help="Parsed VCF",default=None)

	args=parser.parse_args()

	if args.infilename is None :
		parser.error("Input file (-i) is missing.")
	if args.outfilename is None :
		parser.error("Output filename (-o) is missing.")



	reformat_vcf(args.infilename,args.outfilename)



	
