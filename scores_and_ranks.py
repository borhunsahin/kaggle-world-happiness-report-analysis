
from datas import *
import pandas as pd


df_2015_score = pd.DataFrame(data = read_csv("2015.csv")).iloc[:,lambda x:[0,1,2,3]]
df_2016_score = pd.DataFrame(data = read_csv("2016.csv")).iloc[:,lambda x:[0,2,3]]
df_2017_score = pd.DataFrame(data = read_csv("2017.csv")).iloc[:,lambda x:[0,1,2]]
df_2018_score = pd.DataFrame(data = read_csv("2018.csv")).iloc[:,lambda x:[0,1,2]]
df_2019_score = pd.DataFrame(data = read_csv("2019.csv")).iloc[:,lambda x:[0,1,2]]

df_2018_score = df_2018_score.rename(columns={"Country or region":"Country"})
df_2019_score = df_2019_score.rename(columns={"Country or region":"Country"})

scores_ranks_df = pd.merge(df_2015_score,df_2016_score,on="Country")
scores_ranks_df = pd.merge(scores_ranks_df,df_2017_score,on="Country")
scores_ranks_df = pd.merge(scores_ranks_df,df_2018_score,on="Country")
scores_ranks_df = pd.merge(scores_ranks_df,df_2019_score,on="Country")

scores_ranks_df = scores_ranks_df.rename(columns={"Happiness Score_x":"2015 Score","Happiness Score_y":"2016 Score","Happiness.Score":"2017 Score","Score_x":"2018 Score","Score_y":"2019 Score"})
scores_ranks_df = scores_ranks_df.rename(columns={"Happiness Rank_x":"2015 Rank","Happiness Rank_y":"2016 Rank","Happiness.Rank":"2017 Rank","Overall rank_x":"2018 Rank","Overall rank_y":"2019 Rank"})


scores_df = scores_ranks_df.iloc[:,lambda x:[0,3,5,7,9,11]]
scores_df = scores_df.rename(columns={"2015 Score":"2015","2016 Score":"2016","2017 Score":"2017","2018 Score":"2018","2019 Score":"2019"})

ranks_df = scores_ranks_df.iloc[:,lambda x:[0,2,4,6,8,10]]
ranks_df = ranks_df.rename(columns={"2015 Rank":"2015","2016 Rank":"2016","2017 Rank":"2017","2018 Rank":"2018","2019 Rank":"2019"})
