import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv("dataset.csv")

colors = ["red", "yellow","lime", "darkorange"]

ax = df.iloc[:, 2:6].plot.barh(align='center', stacked=True, figsize=(10, 6), color=colors)
plt.tight_layout()

title = plt.title("Quarterly Sales Analysis", pad=60, fontsize=18)
title.set_position([.5, 1.02])
plt.subplots_adjust(top=0.8, left=0.26)

plt.yticks(np.arange(12) , ('Q1 Notepad', 'Q1 Pencil', 'Q1 Whitener','Q2 Notepad', 'Q2 Pencil', 'Q2 Whitener','Q3 Notepad', 'Q3 Pencil', 'Q3 Whitener','Q4 Notepad', 'Q4 Pencil', 'Q4 Whitener' ),fontsize=15)

legend = plt.legend(loc='center',frameon=False,bbox_to_anchor=(0., 1.02, 1., .102), mode='expand', ncol=4, borderaxespad=-.46,prop={'size': 15})

for text in legend.get_texts():
    plt.setp(text,color='#525252')

        
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy() 
    ax.text(x+width/2, y+height/2, '{:.0f}'.format(width), horizontalalignment='center', verticalalignment='center',color='black',fontsize=10)
