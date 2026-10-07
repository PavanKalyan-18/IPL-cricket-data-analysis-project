# ==========================================================
# IPL / CRICKET DATA ANALYTICS PROJECT
# Using:
# Python + Pandas + NumPy + Matplotlib
# ==========================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# STEP 1 : CREATE SAMPLE DATASET
# ==========================================================
data = {
 "Player": [
 "Virat", "Rohit", "Dhoni", "Gill", "Surya",
 "Virat", "Rohit", "Dhoni", "Gill", "Surya"
 ],
 "Team": [
 "RCB", "MI", "CSK", "GT", "MI",
 "RCB", "MI", "CSK", "GT", "MI"
 ],
 "Runs": [
 82, 45, 30, 95, 60,
 70, 100, 40, 88, 72
 ],
"Balls": [
 50, 30, 25, 55, 35,
 45, 60, 20, 50, 40
 ],
 "Wickets": [
 0, 0, 1, 0, 0,
 0, 0, 2, 0, 0
 ],
 "Season": [
 2024, 2024, 2024, 2024, 2024,
 2025, 2025, 2025, 2025, 2025
 ],
 "Result": [
 "Win", "Lose", "Win", "Win", "Lose",
 "Win", "Win", "Lose", "Win", "Win"
 ]
}

# CREATE DATAFRAME
df = pd.DataFrame(data)

# ==========================================================
# STEP 2 : DISPLAY DATA
# ==========================================================

print("\n========== IPL DATA ==========\n")
print(df)

# ==========================================================
# STEP 3 : STRIKE RATE CALCULATION
# ==========================================================

df["Strike_Rate"] = (df["Runs"] / df["Balls"]) * 100
print("\n========== STRIKE RATE ==========\n")
print(df[["Player", "Runs", "Balls", "Strike_Rate"]])

# ==========================================================
# STEP 4 : HIGHEST RUN SCORERS
# ==========================================================

print("\n========== TOP RUN SCORERS ==========\n")
top_runs = df.groupby("Player")["Runs"].sum().sort_values(ascending=False)
print(top_runs)

# ==========================================================
# STEP 5 : BEST STRIKE RATE
# ==========================================================

print("\n========== BEST STRIKE RATE ==========\n")
best_sr = df.groupby("Player")["Strike_Rate"].mean().sort_values(ascending=False)
print(best_sr)

# ==========================================================
# STEP 6 : TEAM PERFORMANCE
# ==========================================================

print("\n========== TEAM PERFORMANCE ==========\n")
team_runs = df.groupby("Team")["Runs"].sum()
print(team_runs)

# ==========================================================
# STEP 7 : MATCH WIN ANALYSIS
# ==========================================================

print("\n========== MATCH RESULTS ==========\n")
wins = df[df["Result"] == "Win"]["Team"].value_counts()
print(wins)

# ==========================================================
# STEP 8 : PLAYER RANKING
# ==========================================================
print("\n========== PLAYER RANKING ==========\n")
ranking = df.groupby("Player")["Runs"].sum().sort_values(ascending=False)
print(ranking)

# ==========================================================
# STEP 9 : PLAYER PERFORMANCE GRAPH
# ==========================================================
plt.figure(figsize=(8,5))
top_runs.plot(kind='bar')
plt.title("Player Total Runs")
plt.xlabel("Player")
plt.ylabel("Runs")
plt.savefig("player_runs_chart.png")
plt.show()

# ==========================================================
# STEP 10 : TEAM WIN ANALYSIS
# ==========================================================
plt.figure(figsize=(8,5))
wins.plot(kind='bar')
plt.title("Team Wins")
plt.xlabel("Team")
plt.ylabel("Wins")
plt.savefig("team_wins_chart.png")
plt.show()

# ==========================================================
# STEP 11 : STRIKE RATE GRAPH
# ==========================================================
plt.figure(figsize=(8,5))
best_sr.plot(kind='line', marker='o')
plt.title("Player Strike Rate")
plt.xlabel("Player")
plt.ylabel("Strike Rate")
plt.savefig("strike_rate_chart.png")
plt.show()

# ==========================================================
# STEP 12 : SEASON COMPARISON
# ==========================================================
print("\n========== SEASON COMPARISON ==========\n")
season_runs = df.groupby("Season")["Runs"].sum()
print(season_runs)
plt.figure(figsize=(8,5))
season_runs.plot(kind='pie', autopct='%1.1f%%')
plt.title("Season Runs Comparison")
plt.ylabel("")
plt.savefig("season_comparison_chart.png")
plt.show()

# ==========================================================
# STEP 13 : SAVE REPORT
# ==========================================================
df.to_csv("ipl_analysis_report.csv", index=False)
print("\nIPL report saved as ipl_analysis_report.csv")

# ==========================================================
# STEP 14 : FINAL SUMMARY
# ==========================================================
print("\n========== FINAL SUMMARY ==========\n")
print("Project Name : IPL Cricket Data Analytics")
print("Technology : Python + Pandas + NumPy + Matplotlib")
print("Total Players :", df["Player"].nunique())
print("Total Teams :", df["Team"].nunique())
print("\nProject Completed Successfully")