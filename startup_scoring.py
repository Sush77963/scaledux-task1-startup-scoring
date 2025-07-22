# Import required tools
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
import os

# STEP 1: Load your CSV file
df = pd.read_csv('data/Startup_Scoring_Dataset.csv')

# STEP 2: Invert burn rate (high burn is bad)
df['burn_rate_inverse'] = df['monthly_burn_rate_inr'].max() - df['monthly_burn_rate_inr']

# STEP 3: Normalize the important numbers
columns_to_normalize = [
    'team_experience',
    'market_size_million_usd',
    'monthly_active_users',
    'funds_raised_inr',
    'valuation_inr',
    'burn_rate_inverse'
]

scaler = MinMaxScaler()
df_scaled = df.copy()
df_scaled[columns_to_normalize] = scaler.fit_transform(df_scaled[columns_to_normalize])

# STEP 4: Give weights to each thing (like importance)
weights = {
    'team_experience': 0.15,
    'market_size_million_usd': 0.20,
    'monthly_active_users': 0.25,
    'funds_raised_inr': 0.15,
    'valuation_inr': 0.15,
    'burn_rate_inverse': 0.10
}

# STEP 5: Calculate final score
df_scaled['score'] = (
    df_scaled['team_experience'] * weights['team_experience'] +
    df_scaled['market_size_million_usd'] * weights['market_size_million_usd'] +
    df_scaled['monthly_active_users'] * weights['monthly_active_users'] +
    df_scaled['funds_raised_inr'] * weights['funds_raised_inr'] +
    df_scaled['valuation_inr'] * weights['valuation_inr'] +
    df_scaled['burn_rate_inverse'] * weights['burn_rate_inverse']
) * 100

# STEP 6: Show Top 10 and Bottom 10
print("Top 10 Startups:")
print(df_scaled.sort_values('score', ascending=False).head(10)[['startup_id', 'score']])

print("\nBottom 10 Startups:")
print(df_scaled.sort_values('score').head(10)[['startup_id', 'score']])

# STEP 7: Make a folder for charts
os.makedirs('outputs', exist_ok=True)

# STEP 8: Draw a bar chart of scores
df_sorted = df_scaled.sort_values('score', ascending=False).reset_index(drop=True)
plt.figure(figsize=(10, 4))
df_sorted['score'].plot(kind='bar')
plt.title("Startup Scores")
plt.ylabel("Score")
plt.xlabel("Startup Index")
plt.tight_layout()
plt.savefig('outputs/bar_chart.png')
plt.close()

# STEP 9: Draw a heatmap to show how features are related
plt.figure(figsize=(8, 6))
sns.heatmap(df_scaled[columns_to_normalize + ['score']].corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig('outputs/heatmap.png')
plt.close()

# STEP 10: Score distribution histogram
df_scaled['score'].plot(kind='hist', bins=15, title='Score Distribution')
plt.xlabel("Score")
plt.tight_layout()
plt.savefig('outputs/histogram.png')
plt.close()

# Save Top 10 and Bottom 10 to CSV files
top_10 = df_scaled.sort_values('score', ascending=False).head(10)
bottom_10 = df_scaled.sort_values('score').head(10)

top_10.to_csv('outputs/top_10_startups.csv', index=False)
bottom_10.to_csv('outputs/bottom_10_startups.csv', index=False)
