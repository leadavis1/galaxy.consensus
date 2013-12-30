from ensemble_walker import concordant_walker
from variant_ensemble import variant_ensemble
from consensus_writer import consensus_vcf
import argparse as arg
import pysam

def __main__():

  ## parse command line
  parser = arg.ArgumentParser(description='Find sites and genotypes which aggree among an arbitrary number of VCF files.')
  parser.add_argument('vcfFiles', nargs='+', metavar='VCFS', help='List of VCF files for input.')
  parser.add_argument('--contig', help='Contig ID to operate on.', required = False)
  args = parser.parse_args()

  walker = concordant_walker(vcfList = args.vcfFiles)
  ## set up the consensus VCF you want to write out
  ## TODO:: there should be a standard and transparent way to propagate information for individual VCF files to the consensus stage.
  outVcf = consensus_vcf()
  outVcf.add_format(id="CN", number="1", type="Character", description="Consensus status")
  outVcf.add_format(id="GT", number="1", type="String", description="Genotype")
  outVcf.add_info(id="X1", number="1", type="String", description="Placeholder for INFO parsing")
  outVcf.add_info(id="X2", number="1", type="String", description="Placeholder 2 for INFO parsing")
  outVcf.samples = walker.samples
  outVcf.write_header()

  walker = concordant_walker(vcfList = args.vcfFiles)

  ## iterate over sites which match among all VCFs in concordant_walker
  for concordantSites in walker.walk_concordant_sites():
    consensus = variant_ensemble(recordSet=concordantSites, samples=walker.samples)
    concordantGenotypes = consensus.set_consensus()
    outVcf.write_record(concordantSites, concordantGenotypes)


if __name__ == '__main__':
  __main__()



