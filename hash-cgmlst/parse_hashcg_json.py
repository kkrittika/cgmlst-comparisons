#!/usr/bin/env python3
'''
Script to parse the allele calls by hash-cgmlst tool 
Date: 2nd May, 2024
Author: Krittika Krishnan
Usage: python parse_hashcg_json_v1.py path/to/jsons outfile.tsv
'''

import sys
import json
import os
# from itertools import islice

def getFiles(directory,outfile):

    asmname="" 
    allele_calls={} #store the allele presence/absence info
    alleleStatus = [] #allele profile for each sample 
    alleleOutput = [] #holding the complete info for each sample before printing
    jsonfiles = [file for file in os.listdir(directory) if file.endswith('.json')]
    
    for jfile in jsonfiles:
        with open(os.path.join(directory, jfile)) as infile:
            # try:
            jsontmp = json.load(infile)
            asmname = jsontmp["name"]
            allele_calls = jsontmp["alleles"]
            # except (json.JSONDecodeError,KeyError) as e:
            #     print(f"Error in decoding JSON file: {jfile}")
            #     print(e)

            for k,v in allele_calls.items():
                if v == "":
                    allele_calls[k] = "-1"

        alleleheader = list(allele_calls.keys())
        for v1 in allele_calls.values():
            alleleStatus.append(v1)
        
        alleleOutput.append((asmname+"\t"+"\t".join(alleleStatus)))
        alleleStatus = []

    with open(outfile,"a") as fh1:
        fh1.write("Sample"+"\t"+("\t").join(alleleheader)+"\n")
        for alleles in alleleOutput:
            fh1.write(alleles+"\n")
   
    
    return
    
def main():
    directory = sys.argv[1]
    outfile = sys.argv[2]
    getFiles(directory,outfile)
    

if __name__=="__main__":
    main()
