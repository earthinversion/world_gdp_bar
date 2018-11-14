import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib import animation

# function for setting the format of values in billions of dollars
def trillions(x,pos):
    'The two args are the value and tick position'
    return '${:.1f}T'.format(x * 1e-12)
formatter = FuncFormatter(trillions)



df=pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_10203569.csv',skiprows=3)
df = df.set_index("Country Name")
with open('neglect_regions.txt',mode='r') as file:
    alist = [line.rstrip() for line in file]
# print(alist)
df=df.drop(alist)

years=np.arange(1960,2018)
xx=45
for year in years:
    num=10
    print(year)
    top_10=df.nlargest(num, str(year))
    # print(top_10[str(year)])
    fig, ax = plt.subplots(figsize=(10,6))
    ax.yaxis.set_major_formatter(formatter)
    plt.bar(np.arange(num),top_10[str(year)].values)
    plt.xticks(np.arange(num), top_10.index.values,fontsize=6)
    plt.title(str(year))
    plt.savefig('figures/gdprank_{}.png'.format(year),dpi=200,bbox_inches='tight')
    plt.close(fig) #to clear the memory
    plt.cla()

#source:https://data.worldbank.org

