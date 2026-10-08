# cgMLST comparison project
The scripts housed here are for calculating the cgMLST allele differences at each locus.

### Usage
#### parse_hashcg_json.py
A script to collate all the individual sample JSON output files from Hash-cgmlst software. The output is a profile tab-separated value (TSV) file.

Run: 
`parse_hash_json.py <results_dir_path> <profile_output.tsv>`

#### dist_hashcg.py
Calculate the pairwise distances between Hash-cgmlst results (comparison of hashes). Missing loci are ignored. It returns the percent identity **(percent_identity)** for the called loci between two samples, the number of loci compared **(hash_numLociCompared)**, the number of alleles found to be same **(hash_numAllelesSame)** and the total loci called **(hash_totalLoci)** for the first sample **(sample1)** in the comparison.

Run:
`dist_hashcg.py <profile_output.tsv> <dist_output.tsv>`

#### kma-cgmlst_dist.py
Calculate the pairwise distances between two kma-cgmlst results. Missing loci are ignored. It returns the percent identity **(kma_identity)** for the called loci between two samples, the number of loci compared **(kma_num_loci_compared)**, the number of alleles found to be same **(kma_num_alleles_same)** and the total loci called **(total_loci)** for the first sample **(kma_sample1)** in the comparison. The input is the collated "sample_cgmlst.csv" output files (converted to .tsv).

Run:
`kma-cgmlst_dist.py <kmacgmlst-profiles.tsv> <dist_output.tsv>`

#### matrix.etoki.pl
Generates a matrix/profiles file of EToKi results from the FASTA output. It requires the output (database) from the "MLSTdb" module of EToKi.

Run:
`matrix.etoki.pl --database <etokidb.csv> <path to output FASTA>`

#### distance.etoki.pl
Calculate the pairwise distances between two cgMLST results from EToKi. It returns the percent identity **(dist)**, number of alleles found to be the same **(numAllelesSame)** and number of loci compared **(numLociSame)**. 

Run:
`distance.etoki.pl <etoki-profiles.tsv>`

#### distance.chewbbaca.pl
Calculate the pairwise distances between two cgMLST results from chewBBACA. It returns the percent identity **(identity)**, number of alleles found to be the same **(numSame)**, number of loci compared **(numCompared)**, total loci in sample 1 **(sample1loci)** and total loci in sample 2 **(sample2loci)**.

Run:
`distance.chewbbaca.pl <chewbbaca-profiles.tsv>`

#### colorid.dist.py
Calculate the pairwise distances between two colorID results. Missing loci are ignored. It returns the percent identity **(colorid_identity)** for the called loci between two samples, the number of loci compared **(colorid_num_loci_compared)**, the number of alleles found to be same **(colorid_num_alleles_same)** and the total loci called **(colorid_total_loci)** for the first sample **(colorid_sample1)** in the comparison. The input is the collated "*.profiles.tsv" colorID output files.

Run:
`colorid.dist.py <colorid-profiles.tsv> <dist_output.tsv>`

#### distance.bn.pl
Calculate the pairwise distance between two cgMLST results from BioNumerics/PulseNet 2.0. It returns the percent identity **(identity)**, number of alleles found to be the same **(numSame)**, number of loci compared **(numCompared)**.

Run:
`distance.bn.pl <pn2.0_core_calls.tsv>`

