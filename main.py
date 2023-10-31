import pandas as pd
import src.extraction as extract
import src.transforming as transform
import src.visualization as visualize

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")


url_list_to = ["https://www.ncaa.com/stats/lacrosse-women/d1/current/team/264" , 
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/264/p2",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/264/p3"]

url_list_dc = ["https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1209", 
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1209/p2",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1209/p3"]

url_list_clears = ["https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1210", 
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1210/p2",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1210/p3"]


url_list_saves = ["https://www.ncaa.com/stats/lacrosse-women/d1/current/team/959", 
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/959/p2",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/959/p3"]

url_list_fp = ["https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1082",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1082/p2",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1082/p3"]

url_list_fouls = ["https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1186",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1186/p2",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1186/p3"]

url_list_gb = ["https://www.ncaa.com/stats/lacrosse-women/d1/current/team/245",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/245/p2",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/245/p3"]


url_list_sd = ["https://www.ncaa.com/stats/lacrosse-women/d1/current/team/247",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/247/p2",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/247/p3"]

url_list_so = ["https://www.ncaa.com/stats/lacrosse-women/d1/current/team/246",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/246/p2",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/246/p3"]


url_list_sp = ["https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1158",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1158/p2",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1158/p3"]


url_list_sg = ["https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1160",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1160/p2",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1160/p3"]

url_list_sog = ["https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1162",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1162/p2",
            "https://www.ncaa.com/stats/lacrosse-women/d1/current/team/1162/p3"]



# extraction
turnovers = extract.combined_dataframe(url_list_to)
draw_controls = extract.combined_dataframe(url_list_dc)
clears = extract.combined_dataframe(url_list_clears)
saves = extract.combined_dataframe(url_list_saves)
free_positions = extract.combined_dataframe(url_list_fp)
fouls = extract.combined_dataframe(url_list_fouls)
ground_balls = extract.combined_dataframe(url_list_gb)
scoring_deffense = extract.combined_dataframe(url_list_sd)
scoring_offense = extract.combined_dataframe(url_list_so)
shot_pct = extract.combined_dataframe(url_list_sp)
shots_per_game = extract.combined_dataframe(url_list_sg)
shots_on_goal_per_game = extract.combined_dataframe(url_list_sog)


# transforming - getting transformed dataframes
turnovers = transform.transform_turnovers (turnovers)
draw_controls = transform.transform_draw_controls(draw_controls)
clears = transform.transform_clears(clears)
saves = transform.transform_saves(saves)
free_positions = transform.tranform_free_positions(free_positions)
fouls = transform.transform_fouls(fouls)
ground_balls = transform.transform_ground_balls(ground_balls)
scoring_deffense = transform.transform_scoring_deffense(scoring_deffense)
scoring_offense = transform.transform_scoring_offense(scoring_offense)
shot_pct = transform.transform_shot_pct(shot_pct)
shots_per_game = transform.transform_shots_per_game(shots_per_game)
shots_on_goal_per_game = transform.transform_shots_on_goal_per_game(shots_on_goal_per_game)


#transforming - merging the transformed dataframes
dataframes_list = [turnovers,draw_controls, clears, saves, free_positions, fouls, ground_balls,
                     scoring_deffense, scoring_offense, shot_pct, shots_per_game, shots_on_goal_per_game]

lacrosse = pd.read_excel("./data/lacrosse.xlsx") #reading the original df

final_df = transform.merge_and_transform(dataframes_list,lacrosse)

#visualization - bar plots
deffense_correlation = visualize.deffense_correlation(final_df)
attack_correlation = visualize.attack_correlation(final_df)
correlation_plot = visualize.variables_correlation_visualization(final_df)

rank_bar_plot = visualize.conference_rank_bar_plot(final_df)
fouls_bar_plot = visualize.conference_fouls_bar_plot(final_df)
shots_on_goal_plot = visualize.conference_shots_bar_plot(final_df)
saves_plot = visualize.conference_saves_bar_plot(final_df)

