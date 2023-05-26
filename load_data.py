
import opendatasets as od
import pandas as pd

url2 = "https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/383116/rawdata_new.csv"
od.download(url2)

print("data installed successfully")
