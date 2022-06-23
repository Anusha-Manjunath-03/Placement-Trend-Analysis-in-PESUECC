import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


while(True):
    year = int(input('Enter the placement year to visualize as graph(Format = YYYY)\n\t\t i)2016 ii)2017 :\n'))
    
    if year != 2016 and year != 2017:
        print('Information about the provided year is not available\n')
    else:
        break
while(True):
    n = int(input('Enter the Tier Companies(Input = 1 or 2 or 3): '))
    if(n != 1 and n != 2 and n != 3):
        print('Invalid Tier\n')
    else:
        break


if year == 2016:
    if n == 1:
        tier = pd.read_excel("Tier1_2016.xlsx")
    elif n == 2:
        tier = pd.read_excel("Tier2_2016.xlsx")
    else:
        tier = pd.read_excel("Tier3_2016.xlsx")
        
else:
    if n == 1:
        tier = pd.read_excel("Tier1_2017.xlsx")
    elif n == 2:
        tier = pd.read_excel("Tier2_2017.xlsx")
    else:
        tier = pd.read_excel("Tier3_2017.xlsx")
	
print(tier)

	
companies = list(tier['Company'])
	
CS_placed = list(tier['CS'])

EC_placed = list(tier['EC'])

IS_placed = list(tier['IS'])

Total_placed = list(tier['Total'])

plotdata = pd.DataFrame({"Total Placed":Total_placed,"CS Placed":CS_placed,"IS Placed":IS_placed,"EC Placed":EC_placed},index = companies)

sns.set_style('darkgrid')
plotdata.plot(kind='bar',color = {'green','red','blue','yellow'},figsize = (20,10)).set(xlabel = 'Companies',ylabel = 'No. of Students',title = 'Placement Statistics')

plt.show()