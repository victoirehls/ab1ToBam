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

### Install ab1ToBam ###
`git clone https://github.com/victoirehls/ab1ToBam.git`

## Input ##
Two ab1 files (reverse and forward reads) OR the name of a file that contains ab1 files to convert (reverse and forward reads). <br>

## Running ab1ToBam ##
`cd placeOfScript`

--> With two ab1 files (reverse + forward reads) <br>
`python ab1_to_bam -p nameOfFile1.ab1 nameOfFile2.ab1`<br>
nameOfFile.ab1 : whole path if the files are not in the same folder as ab1ToBam

--> With the name of the folder where the ab1 files are <br>
Naming system : nameOfRead1.ab1, nameOfRead2.ab1 (reverse + forward reads) <br>
`python ab1_to_sam -f nameOfFolder`

## Outputs ##
Two fastq files : nameOfRead1.fasq, nameOfRead2.fastq <br>
Sam file : nameOfRead1_nameOfRead2.sam <br>
Bam file : nameOfRead1_nameOfRead2.bam <br>
Bai file (index file) : nameOfRead1_nameOfRead2.bam.bai <br>

