
from datas import *
import pandas as pd


df_2015 = pd.DataFrame(report_2015).iloc[:,lambda x:[0,1,2,3,5,6,7,8,9,10,11]]
df_2015 = df_2015.rename(columns={"Economy (GDP per Capita)":"Economy","Health (Life Expectancy)":"Health","Trust (Government Corruption)":"Trust"})

df_2016 = pd.DataFrame(report_2016).iloc[:,lambda x:[0,1,2,3,6,7,8,9,10,11,12]]
df_2016 = df_2016.rename(columns={"Economy (GDP per Capita)":"Economy","Health (Life Expectancy)":"Health","Trust (Government Corruption)":"Trust"})

regions = pd.DataFrame(report_2015).iloc[:,lambda x:[0,1]]
df_2017 = pd.DataFrame(report_2017).iloc[:,lambda x:[0,1,2,5,6,7,8,10,9,11]]
df_2017 = pd.merge(df_2017,regions,on="Country")
df_2017 = df_2017.rename(columns={"Happiness.Rank":"Happiness Rank","Happiness.Score":"Happiness Score","Economy..GDP.per.Capita.":"Economy","Health..Life.Expectancy.":" Health","Trust..Government.Corruption.":"Trust","Dystopia.Residual":"Dystopia Residual"})
df_2017 = df_2017.iloc[:,lambda x:[0,10,1,2,3,4,5,6,7,8,9]]

df_2018 = pd.DataFrame(report_2018).iloc[:,lambda x:[1,0,2,3,4,5,6,7,8]]
df_2018 = df_2018.rename(columns={"Country or region":"Country","Overall rank":"Happiness Rank","Score":"Happiness Score","GDP per capita":"Economy","Healthy life expectancy":"Health","Freedom to make life choices":"Freedom","Perceptions of corruption":"Corruption"})
df_2018 = pd.merge(df_2018,regions,on="Country")
df_2018 = df_2018.iloc[:,lambda x:[0,9,1,2,3,4,5,6,7,8]]

df_2019 = pd.DataFrame(report_2019).iloc[:,lambda x:[1,0,2,3,4,5,6,7,8]]
df_2019 = df_2019.rename(columns={"Country or region":"Country","Overall rank":"Happiness Rank","Score":"Happiness Score","GDP per capita":"Economy","Healthy life expectancy":"Health","Freedom to make life choices":"Freedom","Perceptions of corruption":"Corruption"})
df_2019 = pd.merge(df_2019,regions,on="Country")
df_2019 = df_2019.iloc[:,lambda x:[0,9,1,2,3,4,5,6,7,8]]
