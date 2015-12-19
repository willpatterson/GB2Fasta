import urllib.request
import argparse

import os, sys, re

def open_web_page(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    print(str(response_data))

    gene_lines = re.findall(r'<span class="feat_h">(.*?)</span>', str(response_data))
    print (gene_lines)

if __name__ == "__main__":
    open_web_page("http://www.ncbi.nlm.nih.gov/nuccore/KF874616.1")

