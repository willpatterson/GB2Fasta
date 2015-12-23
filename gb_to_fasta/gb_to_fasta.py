from Bio import Entrez, SeqIO
import argparse

def gb_to_fasta(db_name, id_name, out_fasta):
    Entrez.email = "rclaire@pdx.edu"
    handle = Entrez.efetch(db=db_name, id=id_name, rettype="gb", retmode='text')

    genome = SeqIO.read(handle, 'genbank')
    #print(genome.features)
    with open(out_fasta, "w") as ofasta:
        for feature in genome.features:
            gene_name = ">{}_{}\n".format(feature.type, feature.location)
            seq = feature.extract(genome.seq)
            seq = "{}\n".format(str(seq))
            if feature.type != "source":
                ofasta.write(gene_name)
                ofasta.write(seq)

def main():
    parser = argparse.ArgumentParser(description="Downloads a gb file from NCBI and converts it to fasta format")

    parser.add_argument("db_name", help="NCBI Database to download from")
    parser.add_argument("id_name", help="Species ID to download from")
    parser.add_argument("out_fasta", help="Name of the output fasta file")

    args = parser.parse_args()

    gb_to_fasta(args.db_name, args.id_name, args.out_fasta)

if __name__ == "__main__":
    main()
