import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

def plot_chart():
    sns.set()
    
    np.random.seed(33)
    normal_data_a = np.random.normal(size = 500, loc = 100, scale = 10)
    
    df_normal_a = pd.DataFrame(data = normal_data_a, columns=['Score']).assign(group = 'Group A')
    
    sns.histplot(data=df_normal_a
                 , x='Score'
                 , bins=50
                 )
    
    plt.show()
