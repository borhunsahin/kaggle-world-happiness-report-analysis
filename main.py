
from pandas.core.reshape.concat import concat

from restoring import *
from scores_and_ranks import *

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


print("********** 2015 Report **********")
print(report_2015)
print(report_2015.info())

# 158 Country 6 Feature
# Features : Economy,Family,Health,Freedom,Generosity,Dystopia Residual

print("********** 2016 Report **********")
print(report_2016)
print(report_2016.info())
# 157 Country 8 Feature
# Features : Economy,Family,Health,Freedom,Generosity,Dystopia Residual
# New Features : Lower Confidence Interval,Upper Confidence Interval

print("********** 2017 Report **********")
print(report_2017)
print(report_2017.info())
# 155 Country 8 Feature
# Features : Economy,Family,Health,Freedom,Generosity,Dystopia Residual
# New Features : hisker.high,Whisker.low

print("********** 2018 Report **********")
print(report_2018)
print(report_2018.info())
# 156 Country 9 Feature
# Features : Economy,Family,Health,Freedom,Generosity,Dystopia Residual
# New Features : Social support,Perceptions of corruption
# Old Features : Family

print("********** 2019 Report **********")
print(report_2019)
print(report_2019.info())
# 156 Country 9 Feature
# Features : Economy,Family,Health,Freedom,Generosity,Dystopia Residual
# New Features : Social support,Perceptions of corruption
# Old Features : Family

print(scores_ranks_df)


# What countries or regions rank the highest in overall happiness and each of the six factors contributing to happiness?

df_2019_economy=(df_2019.iloc[:,lambda x:[0,4]]).sort_values(by="Economy",ascending=False).head(20)
df_2019_social_support=(df_2019.iloc[:,lambda x:[0,5]]).sort_values(by="Social support",ascending=False).head(20)
df_2019_health=(df_2019.iloc[:,lambda x:[0,6]]).sort_values(by="Health",ascending=False).head(20)
df_2019_freedom=(df_2019.iloc[:,lambda x:[0,7]]).sort_values(by="Freedom",ascending=False).head(20)
df_2019_generosity=(df_2019.iloc[:,lambda x:[0,8]]).sort_values(by="Generosity",ascending=False).head(20)
df_2019_corruption=(df_2019.iloc[:,lambda x:[0,9]]).sort_values(by="Corruption",ascending=False).head(20)

df_2019_top = pd.concat([df_2019_economy,df_2019_social_support,df_2019_health,df_2019_freedom,df_2019_generosity,df_2019_corruption], axis=1, join="inner").iloc[:,lambda x:[1,3,5,7,9,11]].T
df_2019_top = df_2019_top.rename(columns={10:"Australia",8:"Canada"})


# How did country ranks or scores change between the 2015 and 2016 as well as the 2016 and 2017 reports?

scores_df_2015_2016 = scores_ranks_df.iloc[:,lambda x:[0,3,5]]
scores_df_2016_2017 = scores_ranks_df.iloc[:,lambda x:[0,5,7]]

rank_df_2015_2016 = scores_ranks_df.iloc[:,lambda x:[0,2,4]]
rank_df_2016_2017 = scores_ranks_df.iloc[:,lambda x:[0,4,6]]


# Did any country experience a significant increase or decrease in happiness?

scores_df_difference = pd.DataFrame(scores_df["2019"]-scores_df["2015"],columns=["Difference"])
scores_df = concat([scores_df,scores_df_difference],axis=1)
print(scores_df)

rank_df_difference = pd.DataFrame(ranks_df["2015"]-ranks_df["2019"],columns=["Difference"])
ranks_df = concat([ranks_df,rank_df_difference],axis=1)
print(ranks_df)


venezuela_df_score = scores_df[(scores_df["Difference"]>2) | (scores_df["Difference"]<-2)]
venezuela_df_score = pd.DataFrame(data=venezuela_df_score.iloc[:,lambda x :[1,2,3,4,5]].T)
venezuela_df_score = venezuela_df_score.rename(columns={21:"Venezuela"})

venezuela_df_rank = ranks_df[(ranks_df["Difference"]>80) | (ranks_df["Difference"]<-80)]
venezuela_df_rank = pd.DataFrame(data=venezuela_df_rank.iloc[:,lambda x :[1,2,3,4,5]].T)
venezuela_df_rank = venezuela_df_rank.rename(columns={21:"Venezuela"})
