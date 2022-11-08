import numpy as np
import pandas as pd

def preprocess(df):
    df = __delete_nan_data(df)
    #df =__remove_outlier(df)
    #new_col_name = "match_types"
    #df[new_col_name] = __convert_match_type_column(df,"matchType")
    #df = __change_nan_points(df)
    #df = __one_hot_encode_data_frame(df, new_col_name)
    df = __select_features(df)
    return df

  
def __delete_nan_data(df):
    return df.dropna()

  
def __convert_match_type_column(prepro_df,encoding_feature):
    encoded = prepro_df[encoding_feature].agg(preprocessing_match_type)
    return encoded

  
def preprocessing_match_type(match_type):
    standard_matches = ["solo", "duo", "squad", "solo-fpp", "duo-fpp", "squad-fpp"]
    if match_type in standard_matches:
        return match_type
    else:
        return "others" 

      
def __change_nan_points(df):
    kill_rank_win_points = ["killPoints", "rankPoints", "winPoints"]
    match_types_list = list(df.match_types.unique())
    for col in kill_rank_win_points:
        if col != "rankPoints":
            cond0 = df[col] == 0
            cond1 = df[col] != 0
        else:
            cond0 = df[col] == -1
            cond1 = df[col] != -1
        for m_type in match_types_list:
            cond2 = df.match_types == m_type
            mean = df[cond1 & cond2][col].mean()
            std = df[cond1 & cond2][col].std()
            size = df[cond0 & cond2][col].count()
            if m_type != 'others' or col == "rankPoints":
                rand_points = np.random.randint(mean-std, mean+std, size=size)
            else:
                rand_points = np.array([mean]*size)
            df[col].loc[cond0 & cond2] = rand_points
    return df

  
def __one_hot_encode_data_frame(df, encoding_feature):
    df = pd.get_dummies(df, columns=[encoding_feature])
    return df


def __select_features(df):
    main_columns = ["winPlacePerc", "walkDistance", "killPlace", "boosts", "heals", "kills", "killStreaks", "longestKill", "rideDistance"]
    #main_columns = ["winPlacePerc", "walkDistance", "boosts", "heals", "kills", "killStreaks", "longestKill", "rideDistance"]
    sub_columns = ["weaponsAcquired", "damageDealt", "headshotKills", "assists", "DBNOs"]
    #main_columns = ["winPlacePerc", "walkDistance", "boosts", "weaponsAcquired"]
    #kill_columns = ["kills", "damageDealt"]
    match_type_columns = df.columns[df.columns.str.contains("match_types")]
    #deleted_columns = df[["Id","groupId","matchId","matchType"]]
    #deleted_columns = df[["Id","groupId","matchId"]]
    #deleted_columns = df[["Id","groupId","matchId","killPlace"]]
    #deleted_columns = df[["Id","groupId","matchId","matchType","killPlace"]]
    #deleted_columns = df[["Id","groupId","matchId","matchType","killPoints","matchType","maxPlace","numGroups","rankPoints","revives","roadKills","swimDistance","teamKills","vehicleDestroys","winPoints","revives","weaponsAcquired"]]
    #deleted_columns = list(set(df.columns)-set(main_columns))
    #deleted_columns = list(set(df.columns)-set(main_columns)-set(sub_columns))
    #deleted_columns = list(set(df.columns)-set(main_columns)-set(match_type_columns))
    deleted_columns = list(set(df.columns)-set(main_columns)-set(sub_columns)-set(match_type_columns))
    return df.drop(columns=deleted_columns)


def __remove_outlier(df):
    df = df[(((df['winPlacePerc']+0.5) / (df['walkDistance'])) > 1/13000) & (df['walkDistance']>1) ]
    df = df[((df['winPlacePerc'] / (df['killPlace']-103)) > -1/42)]
    df = df[((df['winPlacePerc']+ 0.51 ) / (df['boosts'])) > 1/17 ]
    df = df[((df['winPlacePerc']+0.5 ) / (df['heals'])) > 1/50 ]
    df = df[((df['winPlacePerc']+0.8 ) / (df['kills'])) > 1/30]
    df = df[((df['winPlacePerc']+1.7 ) / (df['killStreaks'])) > 1/6]
    df = df[((df['winPlacePerc']+ 0.75) / (df['longestKill'])) > 1/600]
    df = df[((df['winPlacePerc']+0.73 ) / (df['rideDistance'])) > 1/24000]
    df = df[((df['winPlacePerc']+ 3.8 ) / (df['weaponsAcquired'])) > 1/20 ]
    df = df[((df['winPlacePerc']+ 0.25 ) / (df['headshotKills'])) > 1/40 ]
    df = df[((df['winPlacePerc']+ 2.8 ) / (df['assists'])) > 1/5 ]
    df = df[((df['winPlacePerc']+ 1.25 ) / (df['DBNOs'])) > 1/16 ]
    return df
