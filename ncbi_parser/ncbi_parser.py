from Bio import Entrez, SeqIO

def download_genbank_file():
    Entrez.email = "wpatt2@pdx.edu"
    handle = Entrez.efetch(db="nuccore", id="KF874616.1", rettype="gb", retmode='text')

    genome = SeqIO.read(handle, 'genbank')
    #print(genome.features)
    for feature in genome.features:
        seq = feature.extract(genome.seq)
        print(feature)
        print(seq)
        print("")


if __name__ == "__main__":
    download_genbank_file()

