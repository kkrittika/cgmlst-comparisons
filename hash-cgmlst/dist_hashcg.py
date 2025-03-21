import csv
import sys
'''
Description: This script reads the matrix generated from the hash-cgmlst tool and calculates the distances between two samples
date: 07/25/2023
Orignial Author: Anusha Ginni; Modified by Krittika Krishnan
usage:  python dist_hashcg_v1.py infile.tsv outfile.tsv
'''

def read_tsvfile(file_path):
    data = {}
    with open(file_path, 'r') as tsvfile:
        matrixreader = csv.reader(tsvfile, delimiter='\t')
        next(matrixreader)
        for row in matrixreader:
            sample_id = row[0] # assembly Ids
            alleles = [(allele) for allele in row[1:]] #hashvalues of allele numbers
            # print(alleles)
            data[sample_id] = alleles
            # print(data)
            alleles = [] #emptying the list for next iteration
    return data

def calculate_distance(sample1, sample2):
    #total_loci = len(sample1)
    
    common_alleles = sum(1 for allele1, allele2 in zip(sample1, sample2) if allele1 == allele2 != "-1") #get common alleles between two samples
    missingLoci = sum(1 for allele1 in sample1 if allele1 == "-1")
    numLoci = int(len(sample1) - missingLoci) 
    #KK: accounting for -1 loci so that it is not compared
    alleleComp = sum(1 for allele1, allele2 in zip(sample1, sample2) if allele1 != "-1" or allele2 != "-1")
    percent_identity = (common_alleles / alleleComp) * 100
    
    return percent_identity, common_alleles, alleleComp, numLoci

    


def write_csv_output(output_file, data):
    with open(output_file, 'w') as outfile:
        colnames = ['hash_sample1', 'hash_sample2', 'hash_identity', 'hash_numAllelesSame', 'hash_numLociCompared', 'hash_totalLoci']
        writer = csv.DictWriter(outfile, fieldnames=colnames,delimiter='\t',lineterminator='\n')
        writer.writeheader()
        samples = list(data.keys())
        for i in range(len(samples)):
            if samples[i] == samples[-1]: #Calculating the metrics for the last sample- Jan 23,2024
                sample1 = samples[i]
                percent_identity, num_alleles_same, num_loci_compared, total_loci = calculate_distance(data[sample1], data[sample1])
                writer.writerow({'hash_sample1': sample1, 'hash_sample2': sample2, 'hash_identity': percent_identity,
                                    'hash_numAllelesSame': num_alleles_same, 'hash_numLociCompared': num_loci_compared, 'hash_totalLoci': total_loci})
            else:
                for j in range(i + 1, len(samples)):
                    sample1 = samples[i]
                    sample2 = samples[j]
                    
                    percent_identity, num_alleles_same, num_loci_compared, total_loci = calculate_distance(data[sample1], data[sample2])
                    writer.writerow({'hash_sample1': sample1, 'hash_sample2': sample2, 'hash_identity': percent_identity,
                                    'hash_numAllelesSame': num_alleles_same, 'hash_numLociCompared': num_loci_compared, 'hash_totalLoci': total_loci})

def main():
    input_tsv_file = sys.argv[1]
    output_csv_file = sys.argv[2]
    data = read_tsvfile(input_tsv_file)
    write_csv_output(output_csv_file, data)


if __name__ == '__main__':
    main()