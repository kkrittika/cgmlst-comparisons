import csv
import sys
'''
Date: 1st Sept, 2023
Author: Krittika Krishnan
Usage: python kma-cgmlst_dist.py <inputfile> <outfile>
'''

def read_tsvfile(file_path):
    data = {}
    with open(file_path, 'r') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t') #change the delimiter depending on csv/tsv
        header = next(reader)
        for row in reader:
            sample_id = row[0] # assembly Ids
            alleles = [(allele) for allele in row[1:]] 
            # print(alleles)
            data[sample_id] = alleles
            # print(data)
    return data

def calculate_distance(sample1, sample2):
    #total_loci = len(sample1)
    common_alleles = sum(1 for allele1, allele2 in zip(sample1, sample2) if allele1 == allele2 != "-") #get common alleles between two samples
    missingLoci = sum(1 for allele1 in sample1 if allele1 == "-")
    numLoci = int(len(sample1) - missingLoci)
    # same_loci = sum(1 for allele1, allele2 in zip(sample1, sample2) if allele1 == allele2 != 0)
    #KK: accounting for -1 loci so that it is not compared
    alleleComp = sum(1 for allele1, allele2 in zip(sample1, sample2) if allele1 != "-" or allele2 != "-")
    percent_identity = (common_alleles / alleleComp) * 100
    return percent_identity, common_alleles, alleleComp, numLoci

def write_csv_output(output_file, data):
    with open(output_file, 'w', newline='') as csvfile:
        colnames = ['kma_sample1', 'kma_sample2', 'kma_identity', 'kma_num_alleles_same', 'kma_num_loci_compared','total_loci']
        writer = csv.DictWriter(csvfile, fieldnames=colnames)
        writer.writeheader()
        samples = list(data.keys())
        for i in range(len(samples)):
            for j in range(i + 1, len(samples)):
                if samples[i]==samples[-1]:
                    sample1=samples[i]
                    percent_identity, num_alleles_same, num_loci_compared, total_loci = calculate_distance(data[sample1], data[sample1])
                    writer.writerow({'kma_sample1': sample1, 'kma_sample2': sample2, 'kma_identity': percent_identity,
                                 'kma_num_alleles_same': num_alleles_same, 'kma_num_loci_compared': num_loci_compared, 'total_loci': total_loci})
                
                else:
                    sample1 = samples[i]
                    sample2 = samples[j]
                
                    percent_identity, num_alleles_same, num_loci_compared, total_loci = calculate_distance(data[sample1], data[sample2])
                    writer.writerow({'kma_sample1': sample1, 'kma_sample2': sample2, 'kma_identity': percent_identity,
                                 'kma_num_alleles_same': num_alleles_same, 'kma_num_loci_compared': num_loci_compared, 'total_loci': total_loci})

if __name__ == '__main__':
    input_tsv_file = sys.argv[1]
    output_csv_file = sys.argv[2]
    data = read_tsvfile(input_tsv_file)
    write_csv_output(output_csv_file, data)