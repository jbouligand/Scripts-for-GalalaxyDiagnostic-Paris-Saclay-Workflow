# Scripts-for-GalalaxyDiagnostic-Paris-Saclay
The generic galaxy workflow that we used for diagnosis “Galaxy-Workflow-2016-11-14_SNV_generic_GATK3.4.ga” can be uploaded in a local galaxy instance. To be operational, the workflow requires the installation of various galaxy tools: 
1) from the galaxytoolshed:
- FastQC Read Quality reports (Galaxy Version 0.63)
- Sickle Windowed Adaptive Trimming of FastQ data (Galaxy Version 1.0.0)
- Map with BWA-MEM - map medium and long reads (> 100 bp) against reference genome (Galaxy Version 0.4.1)
- MarkDuplicates examine aligned records in BAM datasets to locate duplicate molecules (Galaxy Version 1.136.0)
- GATK tool collection Version 3.4-0 (Galaxy Version 3.4-0.d9)
- ANNOVAR Annotate VCF with functional information using ANNOVAR (Galaxy Version 0.2)
- SnpEff Variant effect and annotation (Galaxy Version 4.0.0)
- VCF-BEDintersect: Intersect VCF and BED datasets (Galaxy Version 0.0.3)
- SlopBed (Galaxy Version 2.22.0)
- SAM/BAM Hybrid Selection Metrics for targeted resequencing data (Galaxy Version 1.56.0)
- Compute both the depth and breadth of coverage of features in file A across the features in file B (coverageBed) (Galaxy Version 2.22.1)
2) 3 additional scripts provided as supplemental material.
They need to be installed in the “tools” directory of your local galaxy instance. 
- gVCF_parser
- gVCF_order
- gVCF_filt_freqmax

Note : Python scripts are for python 2.7

Author : Christophe Habib
