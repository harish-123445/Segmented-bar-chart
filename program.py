import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv("dataset.csv")

plt.figure(figsize=(10, 8))
bar1=plt.bar(df.index,df['Los Angeles'],color="red",height="acc(thres=0.5)",width=0.4)
bar2=plt.bar(df.index, df['Houston'], bottom=df['Los Angeles'],color="yellow",height="acc(thres=0.5)",width=0.4)
bar3=plt.bar(df.index, df['Chicago'], bottom=df['Houston'],color="lime",height="acc(thres=0.5)",width=0.4)
bar4=plt.bar(df.index, df['New York'], bottom=df['Chicago'],color="darkorange",height="acc(thres=0.5)",width=0.4)
plt.legend(["Los Angeles", "Houston","Chicago","New York"], loc ="upper right",fontsize=15)
plt.xticks(np.arange(12) , ('Q1 Notepad', 'Q1 Pencil', 'Q1 Whitener','Q2 Notepad', 'Q2 Pencil', 'Q2 Whitener','Q3 Notepad', 'Q3 Pencil', 'Q3 Whitener','Q4 Notepad', 'Q4 Pencil', 'Q4 Whitener' ),rotation='vertical',fontsize=15)
plt.ylabel("Sales",fontsize=20)

for bars in [bar1,bar2,bar3,bar4]:
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, yval + 0.005, yval, ha="center")
    
plt.title("Quarterly Sales Analysis",fontsize=20)


plt.show()
