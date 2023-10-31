import pandas as pd

def transform_turnovers (df):
    df = df.drop(['Caused TOs'], axis = 1)
    df = df.rename(columns={'Per Game': 'Turnovers x game'})
    return df

def transform_draw_controls(df):
    df = df.drop(['Draw Controls','Opp DC'], axis = 1)
    df = df.rename(columns={'Pct.': '% Draw Controls'})
    return df

def transform_clears(df):
    df = df.drop(['Clears','Clr Att'], axis = 1)
    df = df.rename(columns={'Pct.': '% Clears'})
    return df

def transform_saves(df):
    df = df.drop(['Team Min','Goals Allowed', 'Saves'], axis = 1)
    df = df.rename(columns={'Pct.': '% Saves'})
    return df

def tranform_free_positions(df):
    df = df.drop(['Freepos Goals','Freepos Shots'], axis = 1)
    df = df.rename(columns={'Pct.': '% Free positions'})
    return df

def transform_fouls(df):
    df = df.drop(['Fouls'], axis = 1)
    df = df.rename(columns={'Per Game': 'Fouls x game'})
    return df

def transform_ground_balls(df):
    df = df.drop(['Ground Balls'], axis = 1)
    df = df.rename(columns={'Per Game': 'Ground balls x game'})
    return df

def transform_scoring_deffense(df):
    df = df.drop(['Goals Allowed'], axis = 1)
    df = df.rename(columns={'Per Game': 'Goals allowed x game'})
    return df

def transform_scoring_offense(df):
    df = df.drop(['Goals'], axis = 1)
    df = df.rename(columns={'Per Game': 'Goals x game'})
    return df

def transform_shot_pct(df):
    df = df.drop(['Goals', 'Shots'], axis = 1)
    df = df.rename(columns={'Pct.': '% Shots'})
    return df

def transform_shots_per_game(df):
    df = df.drop(['Shots'], axis = 1)
    df = df.rename(columns={'Per Game': 'Shots x game'})
    return df

def transform_shots_on_goal_per_game(df):
    df = df.drop(['SOG'], axis = 1)
    df = df.rename(columns={'Per Game': 'Shots on goal x game'})
    return df


def merge_and_transform(dataframes_list, initial_df):
    merged_df = dataframes_list[0]  # Initialize with the first dataframe
    for dataframe in dataframes_list[1:]:
        merged_df = merged_df.merge(dataframe, on=['Team', 'Games'], how = 'outer')
    
    merged_df = pd.merge(initial_df, merged_df, on='Team', how="left")
    merged_df.drop(['Games','Record', 'Road', 'Neutral', 'Home', 'Non DIV - I'], axis = 1, inplace = True)
    merged_df = merged_df.dropna()

    return merged_df