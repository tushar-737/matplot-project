import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("02-ipl_data.csv")

# ----------------------------
# 1. Team Wins Analysis
# ----------------------------
team_wins = df["Winner"].value_counts()

plt.figure(figsize=(10, 5))
team_wins.plot(kind="bar")
plt.title("IPL Team Wins")
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------
# 2. Average Runs by Team
# ----------------------------
team1_avg = df.groupby("Team1")["Team1_Runs"].mean()
team2_avg = df.groupby("Team2")["Team2_Runs"].mean()

avg_runs = pd.concat([team1_avg, team2_avg], axis=1).mean(axis=1)

plt.figure(figsize=(10, 5))
avg_runs.sort_values(ascending=False).plot(kind="bar")
plt.title("Average Runs by Team")
plt.xlabel("Teams")
plt.ylabel("Average Runs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------
# 3. Venue Analysis
# ----------------------------
venue_matches = df["Venue"].value_counts()

plt.figure(figsize=(10, 5))
venue_matches.plot(kind="bar")
plt.title("Matches Played at Each Venue")
plt.xlabel("Venue")
plt.ylabel("Number of Matches")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------
# 4. Player of Match Awards
# ----------------------------
pom = df["Player_of_Match"].value_counts().head(10)

plt.figure(figsize=(10, 5))
pom.plot(kind="bar")
plt.title("Top Player of the Match Winners")
plt.xlabel("Players")
plt.ylabel("Awards")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------
# 5. Match Runs Distribution
# ----------------------------
total_runs = df["Team1_Runs"] + df["Team2_Runs"]

plt.figure(figsize=(8, 5))
plt.hist(total_runs, bins=10)
plt.title("Total Runs Distribution")
plt.xlabel("Total Runs")
plt.ylabel("Number of Matches")
plt.tight_layout()
plt.show()

# ----------------------------
# 6. Team1 Runs vs Team2 Runs
# ----------------------------
plt.figure(figsize=(8, 5))
plt.scatter(df["Team1_Runs"], df["Team2_Runs"])
plt.title("Team1 Runs vs Team2 Runs")
plt.xlabel("Team1 Runs")
plt.ylabel("Team2 Runs")
plt.tight_layout()
plt.show()

# ----------------------------
# 7. Dashboard
# ----------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

team_wins.plot(kind="bar", ax=axes[0, 0])
axes[0, 0].set_title("Team Wins")

avg_runs.sort_values(ascending=False).plot(kind="bar", ax=axes[0, 1])
axes[0, 1].set_title("Average Runs")

venue_matches.plot(kind="bar", ax=axes[1, 0])
axes[1, 0].set_title("Venue Analysis")

pom.plot(kind="bar", ax=axes[1, 1])
axes[1, 1].set_title("Top Players")

plt.tight_layout()
plt.show()

# ----------------------------
# Top 5 Teams
# ----------------------------
print("\nTop Teams by Wins")
print(team_wins.head())

# ----------------------------
# Top Players
# ----------------------------
print("\nTop Player of the Match Winners")
print(pom)