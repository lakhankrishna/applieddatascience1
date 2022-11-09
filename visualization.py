import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
wine = pd.read_csv('Californa_Wine_Production_1980_2020.csv')

#line graph

amador = wine[wine['County']=='Amador']
kings = wine[wine['County']=='Kings']
lake = wine[wine['County']=='Lake']
alameda = wine[wine['County']== 'Alameda']

plt.plot(amador['Year'],amador['HarvestedAcres'],label='Amador')
plt.plot(kings['Year'],kings['HarvestedAcres'],label='Kings')
plt.plot(lake['Year'],lake['HarvestedAcres'],label='Lake')
plt.plot(alameda['Year'],alameda['HarvestedAcres'],label='Alameda')
plt.legend()
plt.title('Harvested Acres in various county from 1980 to 2020')
plt.xlabel('Years')
plt.ylabel('Acres Harvested')
plt.show()


#bar graph
year = 2010
amador = amador[amador['Year'] >= year]
kings = kings[kings['Year'] >= year]
lake = lake[lake['Year'] >= year]
alameda = alameda[alameda['Year'] >= year]

la=lake['Yield(Unit/Acre)'].groupby(lake.Year).mean()
kg=kings['Yield(Unit/Acre)'].groupby(kings.Year).mean()
am=amador['Yield(Unit/Acre)'].groupby(amador.Year).mean()
al=alameda['Yield(Unit/Acre)'].groupby(alameda.Year).mean()

X = np.arange(len(la.index))
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X + 0.00, la, color = 'b', width = 0.25,label='Lake')
ax.bar(X + 0.25, kg, color = 'g', width = 0.25,label='Kings')
ax.bar(X + 0.50, am, color = 'r', width = 0.25,label='Amador')
plt.xticks(X + 0.25/2,la.index,rotation=90)
plt.legend()
plt.xlabel('Years')
plt.ylabel('Yield(Unit/Acre)')
plt.title('Yield(Unit/Acre) in different county from year '+str(year))
plt.show()


# pie chart
def plot_production(year,data,num_county):
    ''' The plot_production function produces a pie chart of top selected producing counties in the selected year, the function takes year, data and num_county to be selected as the parameters.'''
    y= wine[wine['Year']==year]
    y=y.dropna()
    county = y['County'].values
    prod = y['Production'].values
    var=[]
    for i in range(len(county)):
        var.append([prod[i],county[i]])
    var = sorted(var,reverse=True)
    sums=0
    num_county=num_county
    for i in range(len(var)):
        if i>num_county:
            sums=sums+var[i][0]
        i=i+1
        if i == len(var):
            var=var[:num_county]
            break
    
    var.append([sums,'others'])
    prod = [i[0] for i in var]
    county = [i[1] for i in var]
    plt.figure(figsize=(8,8))
    plt.pie(prod,labels=county,autopct='%1.1f%%',startangle=90,wedgeprops = {"edgecolor" : "black",'linewidth': 2,'antialiased': True})
    plt.axis('equal')
    plt.title('Production of wine in '+str(year)+' (Top '+str(num_county)+') county')
    plt.legend()
    plt.show()

plot_production(2020, wine, 10)
    
