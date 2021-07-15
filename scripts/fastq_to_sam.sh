#!/bin/bash

bwa mem /home/victoire/IGenotyper/referenceGenome/hg19.fa "$1" "$2" | samtools view -bS | samtools sort > "$3"

samtools index -b "$3"


#samtools view -bS output.sam | samtools sort -o output.bam

#samtools index -b output.bam
