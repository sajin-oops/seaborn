import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot([0,1,2,3,4,5])
plt.show()


import seaborn as sns
import numpy as np
tips=sns.load_dataset("tips")
sns.lineplot(x="tip",y="total_bill",data=tips,color="green")


import seaborn as sns
import matplotlib.pyplot as plt
tips =sns.load_dataset("tips")
sns.scatterplot(x="total_bill",y="tip",data=tips)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
tips =sns.load_dataset("tips")
sns.scatterplot(x="total_bill",y="tip",data=tips,color="yellow")
plt.show()