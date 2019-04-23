import numpy as np 
import pandas as pd 

ages = pd.Series(
    {
        'Aidan':2,
        'Anitah':23,
        'Amina':25
    }
)
heights = pd.Series(
    {
        'Aidan':3,
        'Anitah':14,
        'Amina':5
    }
)

summary = pd.DataFrame({'Ages(yrs)':ages,'Heights(ft)':heights})
print(summary)
print(summary.sort_values('Heights(ft)', ascending=True))
print(summary.describe())