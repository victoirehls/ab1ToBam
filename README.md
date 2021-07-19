# ab1ToBam #

## Introduction ##

ab1ToSam was designed to convert .ab1 files into .bam files.

## Requirements ##
Linux operating system <br>
Python <br>
bwa <br>
samtools <br>

## Installations ##

### Install bwa ###
`git clone https://github.com/lh3/bwa.git` <br>
`sudo apt install bwa`


### Install samtools ###
`git clone https://github.com/samtools/samtools.git ` <br>
`sudo apt install samtools`


### Running ab1ToBam ###
`cd placeOfScript`

#### With two ab1 files (reverse + forward reads)####
`python ab1_to_bam -p nameOfFile1.ab1 nameOfFile2.ab1`

### With the name of the folder where the ab1 files are#
Naming system : nameOfRead_1.ab1, nameOfRead_2.ab1 (reverse + forward reads)
`python ab1_to_sam -f nameOfFolder
