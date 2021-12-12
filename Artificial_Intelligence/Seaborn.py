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

#3 Matrix Plots

#Correlation table
tc = tips.corr()

#Heat map
sns.heatmap(tc,annot=True,cmap='coolwarm')

fp = flights.pivot_table(index='month', columns='year', values='passengers')

sns.heatmap(fp,cmap='magma',linecolor='white',linewidths=1)


#Cluster Map
sns.clustermap(fp,cmap='coolwarm',standard_scale=1)


iris = sns.load_dataset('iris')


#4 Grid plots
#Pairplot shows all the plots

sns.pairplot(iris)

#Shos all the pairplots empty

g = sns.PairGrid(iris)

g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.scatter)


g = sns.FacetGrid(data=tips,col='time',row='smoker')
g.map(sns.distplot,'total_bill')
g.map(sns.distplot,'total_bill','tip')


#5 Regreggion Plots
sns.lmplot(x='total_bill',y='tips',data=tips,hue='sex',markers=['o','v'],scatter_kws={'s':100})
sns.lmplot(x='total_bill',y='tips',data=tips,col='sex',row='time')

#6 Style and color
sns.set_style('whitegrid')
sns.countplot(x='sex',data=tips)
sns.despine()
plt.figure(figsize=(12,3))
sns.countplot(x='sex',data=tips)



