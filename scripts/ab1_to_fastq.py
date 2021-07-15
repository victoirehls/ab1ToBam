#!/bin/env python

from Bio import SeqIO
import os
import argparse
from os import listdir
from os.path import isfile, join
import subprocess

parser = argparse.ArgumentParser(description = "Convert two .ab1 files (reverse and forward reads) into .sam")
parser.add_argument("-p", "--pair", help = "the paths of the pairs to convert", nargs = 2)
parser.add_argument("-f", "--folder", help = "folder with the files to convert", nargs = "+")
args = parser.parse_args()


if args.pair :
	for path in args.pair:
		base = os.path.basename(path)
		filename, ext = os.path.splitext(base)
		if ext != ".ab1" :
			raise argparse.ArgumentTypeError('File must have a .ab1 extension')
		records = SeqIO.parse(path, "abi")
		count = SeqIO.write(records, "%s.fastq" %(filename), "fastq")
		print("Converted %s" %(path))
		
		
	base1 = os.path.basename(args.pair[0])
	base2 = os.path.basename(args.pair[1])
	f1 = str(os.path.splitext(base)[0])
	f2 = str(os.path.splitext(base)[0])
	filename1 = str(os.path.splitext(base)[0]) + ".fastq"
	filename2 = str(os.path.splitext(base)[0]) + ".fastq"

	subprocess.call("bwa mem /home/victoire/IGenotyper/referenceGenome/hg19.fa " + filename1 + " " + filename2 + " " + ">" + " " + f1 + "_" + f2 + ".sam", shell = True)
	print("création d'un fichier sam avec " + args.pair[0] + " et " + args.pair[1])
	
	
	subprocess.call("samtools view -bS " + f1 + "_" + f2 + ".sam " + "| samtools sort -o "+ f1 + "_" + f2 + ".bam ", shell = True) 
	subprocess.call("samtools index -b " + f1 + "_" + f2 + ".bam ", shell = True)
	print("Transformation du fichier .bam en .sam avec indexation")
	

	
	
	
	
'''


if args.folder :
	os.chdir(args.folder[0])
	for path in listdir(args.folder[0]) :
		base = os.path.basename(path)
		filename, ext = os.path.splitext(base)
		if ext == ".ab1":
			print("processing $path file...")
			records = SeqIO.parse(path, "abi")
			count = SeqIO.write(records, "%s.fastq" %(filename), "fastq")
			print("Converted %s" %(path))
		for path2 in listdir(args.folder[0]):
			base2 = os.path.basename(path)
			filename2, ext2 = os.path.splitext(base)
			if filename[:-1] == filename2[:-1]:
				subprocess.call("bwa mem /home/victoire/IGenotyper/referenceGenome/hg19.fa" +  path + path2 + ">" + path + "_" + path2 + ".bam", shell = True)
				print("création d'un fichier bam avec " + str(filename) + " et " + str(filename2))
 
'''
