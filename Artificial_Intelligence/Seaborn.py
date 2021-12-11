import seaborn as sns
import numpy as np


#1 Distribution plots

#Load dataset.
tips = sns.load_dataset('tips')

#Plot a histogram in a dataset.
sns.distplot(tips['total_bill'], kde = False,bins = 30 )


#Combined multiple distibutions.
sns.jointplot(x='total_bill',y='tip', data=tips)


#Combined multiple distibutions hexagon distribution.
sns.jointplot(x='total_bill',y='tip', data=tips, kind = 'hex')


#Combined multiple distibutions shows a linear fit.
sns.jointplot(x='total_bill',y='tip', data=tips, kind = 'reg')



#Displayes all the data, the second parameter sets what to compare against if wanted. Use a binomial value.
sns.pairplot(tips, hue='sex', palette = 'blue')

sns.rugplot(tips['total_bill'])

#Bar plots.
sns.barplot(x='sex',y='total_bill',data=tips, estimator=np.std)

#Count plot.
sns.countplot(x='sex', data=tips)

#2 Catogorical plots

#Box plots, dots are outliers, hue separates data based on a categorical data point.
sns.boxplot(x='day', y='total_bill',data=tips, hue='smoker')

#Violin Plot.
sns.violinplot(x='day', y='total_bill',data=tips, hue='sex')

#Strip plot.
sns.stripplot(x='day',y='total_bill',data=tips, jitter=True)

#Swarmplot.
sns.swarmplot(x='day',y='total_bill',data=tips)

#Factor plot, can call in any plot based on the kind parameter.
sns.factorplot(x='day',y='total_bill',data=tips, kind='bar')
