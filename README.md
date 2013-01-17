<?xml version="1.0"?>

<tool name="naive variant consensus caller" id="awesome_consensus_0.1"  > 
    <description>
        Naive consensus caller for ATLAS SNP2, GATK UG, freebayes output files.
    </description>

    <command interpreter="python">
        consensus.py --atlas-vcf $ATLAS_VCF \
            --gatk-vcf $GATK_VCF \
            --freebayes-vcf $FREEBAYES_VCF \
            --out $OUT
    </command>

    <inputs>
        <param name="ATLAS_VCF" type="data" format="vcf"
            label="ATLAS VCF">
        </param>
        <param name="FREEBAYES_VCF" type="data" format="vcf"
            label="freebayes VCF">
        </param>
        <param name="GATK_VCF" type="data" format="vcf"
            label="GATK VCF">
        </param>
        <param name="OUT" format="vcf" type="data" label="Consensus VCF">
        </param>
    </inputs>
    
    <outputs>
        <data format="vcf" name="output_vcf" label="Consensus VCF" />
    </outputs>

    <help>
        This tool is designed to accept output VCF files from freebayes, GATK
        Unified Genotyper, and ATLAS SNP2 and merge variation called within
        those.
    </help>

</tool>
