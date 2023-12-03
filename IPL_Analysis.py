# Importing Essential Libraries or Modules
import numpy as np  # --> linear algebra
import pandas as pd  # --> data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px

# Reading our CSV files
Matches = pd.read_csv("IPL_Dataset.csv", index_col='id')
Records = pd.read_csv("Stats.csv")

# Data Preprocessing
Matches.columns

# Deleting Method which is not useful
Matches.loc[Matches.method.notnull()]
Matches.drop(['method'], axis=1, inplace=True)
Matches.info()

# #Pie Graph on Winner Team
df1 = Matches.groupby(['winner'])[
    'winner'].count().reset_index(name='count')

# Pie chart using the Plotly
fig = px.pie(df1, values='count', names='winner', title='Most IPL wins')
fig.show()
print('Mumbai Indians is Most Succesful Team with 120+ Wins')

# Select two columns with conditional values

Matches[['eliminator', 'winner']][Matches['eliminator'] == 'Y'].value_counts()

# Bar Plot - Most Wins in Eliminator

df2 = Matches.groupby('winner')['eliminator'].apply(
    lambda x: (x == 'Y').sum()).reset_index(name='count')

# Bar chart using the Plotly
fig = px.bar(df2, x='winner', y='count', color="winner",
             title='Most IPL wins in Eliminator')
fig.show()
print('Kings XI Punjab (3) has the Most IPL wins in Eliminator')

# Most Runs in IPL

fig = px.scatter(Records.head(15), x='Player', y='Runs', color='Player',
                 size='Runs', title='15 Top Most Players Having Maximum Runs in IPL')
fig.show()
print('Virat Kohli has the Highest Runs in IPL Runs(6980+)')

# Most No of Centuries in IPL

Records1 = Records.sort_values(by='100s', ascending=False)
fig = px.bar(Records1.head(15), x='Player', y='100s', color='Player',
             orientation='h', title="Top '15' Players with Most Hundered (100s).")
fig.show()
print('Chris Gayle Has most No of Hundereds in IPL (6)')

# Player Stats

Records2 = Records.sort_values(by=['Strike Rate'], ascending=False).head(5)
fig = px.sunburst(Records2, path=['4s', '6s', 'Strike Rate', 'Player'],
                  values='Runs', title='Stats of 5 Players having Highest Strike Rate')
fig.show()
print('AD Russell has the Highest Strike Rate in IPL (175.42)')

# Most Sixes
Records3 = Records.sort_values(by=['6s'], ascending=False).head(5)
fig = px.scatter(Records.head(15), x='Player', y='6s', color='Player',
                 size='6s', title="Top '15' Players with Most Sixes (6s)")
fig.show()
print('Chris Gayle has the Most no of Sixes in IPL (357)')

# Top Famous Venues
# Count the number of matches played at each venue/stadium
venue_counts = Matches['venue'].value_counts()

# Create a DataFrame with the count of matches played at each venue/stadium
df3 = pd.DataFrame({'venue': venue_counts.index,
                   'Matches played': venue_counts.values})

# Sort the DataFrame
df3 = df3.sort_values(by='Matches played', ascending=False).head(10)

# Bar chart using the Plotly
fig = px.bar(df3, x='venue', y='Matches played', color='venue',
             title='10 Most Popular Venue or Stadium')
fig.show()
print('Eden Gardens is the Most Popular Venue')

# Most Player of the Match Awards
# Count the number of awards
award_counts = Matches['Man of the Match'].value_counts()

# # Create a DataFrame with the count of award
df4 = pd.DataFrame({'Man of the Match': award_counts.index,
                   'No of Awards': award_counts.values})

# # Sort the DataFrame
df4 = df4.sort_values(by='No of Awards', ascending=False).head(10)

# # Bar chart using the Plotly
fig = px.scatter(df4, x='Man of the Match', y='No of Awards', color='Man of the Match',
                 size='No of Awards', title='10 Most "Man of the Match" Awarded Player')
fig.show()
print('AB de Villiers has Most no of Man of the Match Awards (23)')

# Most no of Toss Wins!
# Count the number of Toss won by a particular Franchise
toss_counts = Matches['Toss Winner'].value_counts()

# # Create a DataFrame with the count of award
df5 = pd.DataFrame({'Toss Winner': toss_counts.index,
                   'No of Toss Won': toss_counts.values})

# # Sort the DataFrame
df5 = df5.sort_values(by='No of Toss Won', ascending=False).head(10)

# Pie chart using the Plotly
fig = px.pie(df5, values='No of Toss Won', names='Toss Winner',
             color='Toss Winner', title='10 Teams with Most Toss Wins')
fig.show()
print('Mumbai Indians has Most Toss Wins Record (106)')

# Elected To Bat or Field after Winning Toss.

BatField_counts = Matches['Toss Decision'].value_counts()

df6 = pd.DataFrame({'Toss Decision': BatField_counts.index,
                   'Elected to Bat or Field': BatField_counts.values})

df6 = df6.sort_values(by='Toss Decision', ascending=False).head(10)

fig = px.bar(df6, x="Toss Decision", y="Elected to Bat or Field",
             color='Toss Decision', title='Most Elected option after winning Toss')
fig.show()
print('It is more likely that the teams elect to field first. (496)')

# Top Umpires
# Count the number of times Umpire is Umpiring
umpire_count = Matches['umpire1'].value_counts()

# # Create a DataFrame with the count of umpire
df5 = pd.DataFrame({'umpire1': umpire_count.index,
                   'Umpired Matches': umpire_count.values})

# # Sort the DataFrame
df5 = df5.sort_values(by='Umpired Matches', ascending=False).head(10)

# Pie chart using the Plotly
fig = px.histogram(df5, y='Umpired Matches', x='umpire1',
                   color='umpire1', title='Top Umpires')
fig.show()
print('HDPK Dharmasena is the top most Umpire')

# Rivalry Between Strongest Teams.

# MI VS CSK
num_mi_wins = len(Matches[(Matches["team1"] == 'Chennai Super Kings') & (
    Matches["team2"] == 'Mumbai Indians') & (Matches["winner"] == "Mumbai Indians")])

num_csk_wins = len(Matches[(Matches["team1"] == 'Mumbai Indians') & (
    Matches["team2"] == 'Chennai Super Kings') & (Matches["winner"] == "Chennai Super Kings")])

# Create a DataFrame with the team names and number of wins
data = {'Team': ['Mumbai Indians', 'Chennai Super Kings'],
        'Wins': [num_mi_wins, num_csk_wins]}

df = pd.DataFrame(data)

# Create the bar chart using Plotly Express
fig = px.scatter(df, x='Team', y='Wins', color='Team',
                 size='Wins', title='MI vs CSK')
fig.show()
print('Mumbia Indians have More Wins Against Chennai Super Kings')

# MI VS RCB
num_rcb_wins = len(Matches[(Matches["team1"] == 'Mumbai Indians') & (
    Matches["team2"] == 'Royal Challengers Bangalore') & (Matches["winner"] == "Royal Challengers Bangalore")])

num_mi1_wins = len(Matches[(Matches["team1"] == 'Royal Challengers Bangalore') & (
    Matches["team2"] == 'Mumbai Indians') & (Matches["winner"] == "Mumbai Indians")])

data = {'Team': ['Royal Challengers Bangalore',
                 'Mumbai Indians'], 'Wins': [num_rcb_wins, num_mi1_wins]}
df = pd.DataFrame(data)

fig = px.histogram(df, x='Team', y='Wins', color='Team', title='MI vs RCB')
fig.show()
print('Mumbia Indians have More Wins Against Royal Challenger Banglore')
