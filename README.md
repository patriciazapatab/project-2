# Project-2
# Introduction

This project aims to analyze the NCAA women's lacrosse statistics and understand the variables that have the most significant impact on a team's ranking at the end of the season. The project encompasses web scraping, data extraction, data transformation, and data visualization.
<br>

# Requirements/Libraries Used:
This code was written in Python/Jupyter Notebook, using the following libraries:
<br>
- Pandas
- matplotlib
- Seaborn
- re
- import requests
- from bs4 import BeautifulSoup
<br>
 

# Data Source and variables definitions
<br>

**Data Source**: The dataset used in this project is obtained through web scraping from the official NCAA Women's Lacrosse webpage. The initial data set contained the final ranking of 2022-2023 season. 

**Data Content**: The enriched dataset includes various statistics related to women's lacrosse, such as:
<br>
- Turnovers: represent the number of times a team loses possession of the ball to the opposing team.

- Draw controls: count of how many times a player successfully gains control of the ball at the start of a play or after a goal.

- Clears: defensive-to-offensive transitions

- Saves: goalkeeper's successful stops

- Free positions: similar to football penalties, opportunities where a player has a chance to take an uncontested shot at the goal.

- Fouls: number of rule violations committed by a team

- Ground balls: how many times a player or team gains control of the ball after it has been on the ground

- Scoring defense: goals allowed per game

- Scoring offense: goals scored per game

- Shot percentage: number of goals / number of shots taken

- Shots per game: offensive shot frequency

- Shots on goal per game: shots that aim inside the goal / shots taken. It is used to measure shot accuracy. 

<br>

# Workflow & methodology

**Extraction**: The src/extraction.py module is responsible for extracting data from the NCAA Women's Lacrosse website. It mainly reads tables from various pages using web scraping techniques.

**Transformation**: In the src/transforming.py module the data set is cleaned, formatted, and merged into a single, unified dataframe for analysis.

**Visualization**: The src/visualization.py component focuses on creating visualizations to gain insights into the data. Bar plots and correlation visualizations are used to identify the relationships between various statistics and a team's end-of-season ranking.

<br>

# Initial questions

The analysis aims to answer the following questions: 
<br>
1. What is the correlation across variables and the ranking position?

2. Should teams focus more on attack or on deffense?

3. Are there differences across conferences? 

<br>

# Analysis and results

After enriching, cleaning, and transforming the dataset, the project conducts visualizations to address research questions.

### Correlation visualizations

The following heatmap is utilized to examine correlations between variables.
<br>

![correlation](https://github.com/patriciazapatab/project-2/blob/main/figures/correlation_heatmap.png?raw=true)

The first row ( or column) shows the correlation of variables with the rank. "Draw controls" is the variable with higher correlation which shows the importance of having control over the ball since the first moment of the game. 

It is followed by "Clears percentage", where players succesfully transition the ball out of their deffensive area. 

Also it is interesesting to note the low correlation of ground balls, a variable previously perceived as highly influential and decisive to win games.

To gain further insights it is possible to compare correlation of variables considered deffensive and variables related to the attack. 

![deffense_correlation](https://github.com/patriciazapatab/project-2/blob/main/figures/deffence_correlation.png?raw=true)

As expected, "goals allowed per game" is positively correlated with rank, meaning that there are more goals allowed further on the ranking is the team. However, an interesting point is that this correlation is the same one as "goals per game" on the attack correlation heatmap. This shows that it is equally important to score than to not get scored. 

![attack_correlation](https://github.com/patriciazapatab/project-2/blob/main/figures/attack_correlation.png?raw=true)


On the attack correlation heatmap is worth mentioning that there is a higher correlation between "shots per game" and "shots on goal per name" meaning that it is more important to shot even if it does not go between the three goal poles.

### Conferences characteristics

After the correlation analyisis more data is plotted to visualize differences across conferences. 

To give some context, on the NCAA lacrosse teams are divided between conferences. In some cases this division is made because of geographical position or historical reasons, in other cases it is random.

The following picture shows the conferences distributions: 

![NCAA conferences](https://github.com/patriciazapatab/project-2/blob/main/images/NCAA_Division_I_womens_lacrosse_map.png?raw=true)

When plotting the rank mean grouping by conference the results show Big Ten and the Atlantic Coast Conference as the ones with better result. However, results might be affected by the uneven number of teams between conferences.

![Rank_mean_conferences](https://github.com/patriciazapatab/project-2/blob/main/figures/rank_by_conference.png?raw=true)

The following graphs illustrate differences across conferences on three variables: 

![Fouls_mean_conferences](https://github.com/patriciazapatab/project-2/blob/main/figures/fouls_by_rank.png?raw=true)

It is curious to observe how conferences that rank higher are in the middle of fouls committed. This could mean that even though fouls won't make you win a game in some occasions they might be useful. Teams with lower number of fouls are towards the end of the ranking. 

![Saves_mean_conferences](https://github.com/patriciazapatab/project-2/blob/main/figures/saves_by_rank.png?raw=true)

Saves percentages are similar across conferences. However it is visible that does not determin the result since Mountain Pacific Sports Federation Conference and Northeast Conference are positioned towards the end of the ranking with better save numbers. 

![goalsongoal_mean_conferences](https://github.com/patriciazapatab/project-2/blob/main/figures/shots_by_rank.png?raw=true)

Finally, the data presented on the last graph shows conferences with better accuracy. Again, it is possible to observe that conferences with high shot accuracy are not necessarily ranked better. 

# Conclusions

After finalizing the analysis and visualization of the data the following conclusions are extracted:

 - Having a player as a draw control specialist is a good strategy and will have a positive impact on team results.

- Teams strategy should take into account both attack and deffense tactics to ensure success. 

 - Shooting is more important than shooting accurate... If you don't shoot you have a 100% chance of not scoring. 

 - There are some differences in the game across conferences but none of the observed make one whole conference better than another one. 

 - As in most sports, success in woman's lacrosse is a combination of parcticing and mastering many variables. 



# Links of interest

- Presentation: https://www.canva.com/design/DAFyv848aXQ/1oICXROx4PYCOfGHgYA9nw/edit 