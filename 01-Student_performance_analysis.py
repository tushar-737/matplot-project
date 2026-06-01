import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('student_performance_150.csv')
df['Total']=df['Maths']+df['Science']+df['English']
df['average']=df['Total']/3
#Bar chart for subject wise avg marks
subject_average=df[['Maths','Science','English']].mean()
print(subject_average)
subject_average.plot(kind='bar')
plt.ylabel("marks")
plt.title("Subject average")
plt.show()

#Histogram for marks distribution
plt.hist(df["Total"], bins=10)
plt.title("Distribution of Total Marks")
plt.xlabel("Total Marks")
plt.ylabel("Students")
plt.show()

#scatterplot for study hrs vs marks
plt.scatter(df["Study_Hours"],df["Total"],color='red')
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study_hrs vs Marks")
plt.show()