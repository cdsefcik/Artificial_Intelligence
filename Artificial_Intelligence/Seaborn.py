import seaborn as sns



#1 Distribution plots

#Load dataset
tips = sns.load_dataset('tips')

#Plot a histogram in a dataset
sns.distplot(tips['total_bill'], kde = False,bins = 30 )


#Combined multiple distibutions
sns.jointplot(x='total_bill',y='tip', data=tips)


#Combined multiple distibutions hexagon distribution
sns.jointplot(x='total_bill',y='tip', data=tips, kind = 'hex')


#Combined multiple distibutions shows a linear fit
sns.jointplot(x='total_bill',y='tip', data=tips, kind = 'reg')



#Displayes all the data, the second parameter sets what to compare against if wanted. Use a binomial value.
sns.pairplot(tips, hue='sex', palette = 'blue')

sns.rugplot(tips['total_bill'])





