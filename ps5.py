# Ziyang Zhang, Siegler Troy

import pandas as pd
import math
import numpy as np
import scipy.stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit
import datetime as dt
from utils import *
from covid import *

# Problem 1
# Pulled dataset off the internet at https://github.com/CSSEGISandData/COVID-19

# Problem 2

## International Organization: The WHO (World Health Organization)
# The WHO by its name is responsible for world health matters and handles issues such as COVID 19. 
# I would imagine the data from the WHO to be very accurate as it is of very high importance that they
# provide accurate data. The WHO has perhaps been one of the leading credible sources for information on the virus 
# since the outbreak started. 

# Government Organization: China CDC
# In short, the China CDC is the equivalent of the CDC here in the United States. 
# I would imagine this data to be fairly accurate. However, I would verify data from the China CDC with another 
# source, as there were allegations of China intentionally under-reporting cases during the outbreak. 

# News Organization: BNO News
# BNO News is a Dutch news corporation. I would imagine that the data from this news outlet to be accurate, 
# however in considering good data analytics practices it would not hurt to double check the information they provide
# against another source.

# Problem 3
df = loadAndCleanData(file):
	pandaFile = pd.read_csv(file)
	pandaFile.fillna(value = 0, inplace=True)
	return pandaFile
cleanedData = loadAndCleanData("time_series_covid9_confirmed_global.csv")
cleanedData

# Problem 4
def correctDateFormate(data):
	df = data.melt(id_vars=df.columns[0:4],var_name="Date",value_name="Confirmed")
	data["Date"] = pd.to_datetime(data["Date"])
	return data

# Problem 5
globalCase = correctDataFormat(cleaneddata)
print(globalCase)

x = "Date"
y = "Confirmed"

# Problem 6
globalCase['Data'] = pd.to_datetime(data["Date"])
return globalCase

# Problem 7
globalRecovered = pd.read_csv("time_series_covid9_recovered_global.csv")
globalRecovered

globalDeathCleaned = loadAndCleanData("time_series_covid9_deaths_global.csv")
globalDeathCleaned

def correctDataFormatDeaths(data):
	data=data.melt(id_vars=data.columns[0:4],var_name="Date",value_name="Deaths")
	data["Date"] = pd.to_datetime(data["Date"])
	return data
globalDeathCompleted = correctDataFormatDeaths(globalDeathsCleaned)
globalDeathCompleted

globalRecoveredCleaned = loadAndCleanData("time_series_covid9_recovered_global.csv")
globalRecoveredCleaned

def correctDateFormatRecovered(data):
	data=data.melt(id_vars=data.columns[0:4],var_name="Date",value_name="Recovered")
	data["Date"] = pd.to_datetime(data["Date"])
	return data

globalRecoveredComplete = correctDateFormatRecovered(globalRecoveredCleaned)
globalRecoveredComplete

# Problem 8
mergeData(globalCase,globalDeathsCompleted,"Deaths")
firstMerge = mergeData(globalCase,globalDeathsCompleted,"Deaths")
firstMerge

globalData = mergeData(firstMerge, globalRecoveredCleaned, "Recovered")
globalData

# Problem 9
print(mergeData(df,df1,"Deaths"))
x = mergeData(x,df2,"Recovered")
print(mergeData(x,df2,"Recovered"))


# Problem 10
def plotTimeLine(data,time_col,vc):
	sns.lineplot(data=data,x=time_col,y=vc)
	plt.show()

# Problem 11
plotTime(globalData,"Date","Confirmed")
plotTime(globalData,"Date","Deaths")
plotTime(globalData,"Date","Recovered")

# In this problem, we are plotted the “Death”, “Confirmed”, and “Recovered” values from the data sets. 
# All of these data columns are matched up with their respective “Date” and then plotted on the graph.
# As time as gone on the growth rate for deaths and confirmed cases are beginning to slow down.
# And the recovered values continue to grow as time moves on. 

# Problem 12
def plotMultipleTimeLines(data,time_col,vc,cat_col):
	sns.lineplot(data=data,x=time_col,y=vc,hue=cat_col)
	plt.show()


# Problem 13
plotMulitipleTimeLines(globalData,"Date","Recovered","Deaths")
plotMulitipleTimeLines(globalData,"Date","Confirmed","Deaths")
plotMulitipleTimeLines(globalData,"Date","Confirmed","Recovered")

# Problem 14
def aggregateCountry(df,country):
	data = df.loc[df["Country/Region"] == country]
	return data.groupby("Date",as_index=False).sum()

# Problem 15
def topCorrelation(data,country):
	corrs = []
	countries = pd.unique(data["Country/Region"])
	repeat = []
	for c1 in countries:
		for c2 in countries:
			if c1 != c2:
				if [c1,c2] not in repeat and [c2,c1] not in repeat:
					c1Data = df.loc[data["Country/Region"] == c1]
					c1Data = df.groupby("Date",as_index=False).sum()

					x = c1Data["Confirmed"].sum()
					c2Data = df.loc[data["Country/Region"] == c2]
					c2Data = df.groupby("Date",as_index=False).sum()

					y = c2Data["Confirmed"].sum()
					if c1Data["Confirmed"].sum() >= 500 and c2Data["Confirmed"].sum() >= 500:
						return c1Data[topColumn].corr(c1Data[topColumn])

# Problem 16
topCorrelation(firstMerge,"Confirmed")



# Problem 19
# I compare the growth rates between South Korea and China and two later ones: Italy and the United States.
# The US and Italy’s growth rates absolutely blow China and South Korea’s out the water. 
# We can tell the data from the early outbreak countries did not help the regions that experienced the virus later. 


# Problem 20
# Most of these rates are strongly correlated one way or another. 

# Hypotheses:

# As the Confirmed Cases go up, so does the Death Rate
# As Death Rates go up, so do the recovery rate
# As recovery rate goes up, so does confirmed cases 

# I believe that all of these are positively correlated. 
# The fact that confirmed cases and death goes up as recovery rates go up are contradictory. 
# This happens because so many mire individuals are getting tested now, 
# so the cases and deaths are bound to increase dramatically. 
# And people recovering from the virus will have constant growth at the epidemic progresses. 




