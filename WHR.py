import csv
import matplotlib.pyplot as plot
import pandas as pd
import numpy as np

# WHR Project Data Sci
# Jack Donahue

# Questions
# 1) What impact does GDP have on the general happiness level?
# 2) Does the country's main industries meaningfully impact happiness?
# 3) What is the impact of government style on Happiness?
# 4) What (if any) is the impact of air quality on happiness?

filepath = "WHR.csv"
for airport in destinations:
    delaylist = []
    average = 0
    with open(filepath) as data:
        csv_reader = csv.reader(data)
        iteration = 0
        for row in csv_reader:
            if row[8] == airport:
                if row[11] == '':
                    delaylist.append(0)
                else:
                    delaylist.append(int(row[11]))
        if len(delaylist) == 0:
            delaylist.append(0)
        average = sum(delaylist) / len(delaylist)
        averagedelay.append(average)
    iteration += 1
        
df = pd.DataFrame({"Destinations":destinations,"Averagedelay":averagedelay})
df = df.sort_values('Averagedelay',ascending=False)
df = df.iloc[0:10]

plot.bar("Destinations", "Averagedelay",data=df, width=0.8, edgecolor='black')
plot.title('Question A')
plot.xticks(rotation='vertical')
plot.xlabel('Destinations')
plot.ylabel('Average Delay')
plot.show()
