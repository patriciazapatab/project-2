import matplotlib.pyplot as plt
import seaborn as sns

def variables_correlation_visualization(df):
    subset = df[['Rank','% Draw Controls', 'Turnovers x game','Ground balls x game','% Saves', '% Clears']]
    correlation_matrix = subset.corr()
    plt.figure(figsize=(14, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.savefig("./figures/correlation_heatmap.png")


def deffense_correlation(df):
    subset_deffense = df[['Rank', 'Turnovers x game','% Clears', '% Saves','Goals allowed x game']]
    correlation_matrix = subset_deffense.corr()
    plt.figure(figsize=(14, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title("Deffense Correlation Heatmap")
    plt.savefig("./figures/deffence_correlation.png")

def attack_correlation(df):
    subset_attack = df[['Rank','% Free positions','Goals x game','% Shots','Shots x game','Shots on goal x game']]
    correlation_matrix = subset_attack.corr()
    plt.figure(figsize=(14, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title("Attack Correlation Heatmap")
    plt.savefig("./figures/attack_correlation.png")

def conference_rank_bar_plot(df):
    conference_rank = df.groupby("Conference")["Rank"].mean()
    conference_rank = conference_rank.sort_values()
    plt.figure(figsize=(14, 6))
    conference_rank.plot(kind="bar", rot=45)
    plt.title("Rank by Conference")
    plt.ylabel("Mean Rank")
    plt.savefig("./figures/rank_by_conference.png")


def conference_fouls_bar_plot(df):
    conference_mean_rank = df.groupby("Conference")["Rank"].mean().reset_index()
    conference_mean_rank = conference_mean_rank.sort_values(by="Rank")
    
    color = (0.2, # redness
     0.4, # greenness
     0.2, # blueness
     0.6 # transparency
     )
    
    plt.figure(figsize=(14, 6))
    sns.barplot(x="Conference", y="Fouls x game", data=df, order=conference_mean_rank["Conference"], color = color)
    plt.title("Fouls by conference")
    plt.xlabel("Conference")
    plt.ylabel("Fouls")
    plt.xticks(rotation=45)
    plt.savefig("./figures/fouls_by_rank.png")
   

def conference_shots_bar_plot(df):
    conference_mean_rank = df.groupby("Conference")["Rank"].mean().reset_index()
    conference_mean_rank = conference_mean_rank.sort_values(by="Rank")
    color = (0.2, # redness
         0.4, # greenness
         0.2, # blueness
         0.6 # transparency
         )
    plt.figure(figsize=(14, 6))
    sns.barplot(x="Conference", y="Shots on goal x game", data=df, order=conference_mean_rank["Conference"], color=color)
    plt.title("Shots on goal by conference")
    plt.xlabel("Conference")
    plt.ylabel("Shots on goal")
    plt.xticks(rotation=45)
    plt.savefig("./figures/shots_by_rank.png")



def conference_saves_bar_plot(df):
    conference_mean_rank = df.groupby("Conference")["Rank"].mean().reset_index()
    conference_mean_rank = conference_mean_rank.sort_values(by="Rank")
    color = (0.2, # redness
         0.4, # greenness
         0.2, # blueness
         0.6 # transparency
         )
    plt.figure(figsize=(14, 6))
    sns.barplot(x="Conference", y="% Saves", data=df, order=conference_mean_rank["Conference"], color=color)
    plt.title("Saves by Conference")
    plt.xlabel("Conference")
    plt.ylabel("Saves")
    plt.xticks(rotation=45)
    plt.savefig("./figures/saves_by_rank.png")