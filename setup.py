from setuptools import setup, find_packages

setup(name="gb-to-fasta",
      version="1.0.0",
      description="Downloads genbank file and converts it to fasta",
      license="MIT",
      author="William Patterson",
      packages=find_packages(),
      package_data={}
      install_requires=["biopython"],
      long_description="",
      entry_points={"console_scripts": ["gbtofasta=gb-to-fasta.gb-to-fasta:main"],})
