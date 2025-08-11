
import ruptures as rpt
import matplotlib.pyplot as plt

# --- Step 1: Preprocessing and Aggregation ---
querytrendr['created'] = pd.to_datetime(querytrendr['created'])
querytrendr['year'] = querytrendr['created'].dt.year

querytrendy['created'] = pd.to_datetime(querytrendy['created'])
querytrendy['year'] = querytrendy['created'].dt.year
querytrendy = querytrendy[querytrendy['year']>=2018]

# Group by year and calculate mean sentiment
yearly_avg = querytrendy.groupby('year')['sentiment_compound'].mean().reset_index()
yearsr = yearly_avg['year'].values
signalr = yearly_avg['sentiment_compound'].values

yearly_avg = querytrendr.groupby('year')['sentiment_compound'].mean().reset_index()
yearsy = yearly_avg['year'].values
signaly = yearly_avg['sentiment_compound'].values

# Group by year and calculate mean sentiment
yearly_avg = querytrendr.groupby('year')['sentiment_compound'].mean().reset_index()
yearsr = yearly_avg['year'].values
signalr = yearly_avg['sentiment_compound'].values

yearly_avg = querytrendy.groupby('year')['sentiment_compound'].mean().reset_index()
yearsy = yearly_avg['year'].values
signaly = yearly_avg['sentiment_compound'].values

# --- Step 2: Drift Detection using Ruptures ---
algo = rpt.Binseg(model="rbf").fit(signalr)
algo = rpt.Binseg(model="rbf").fit(signaly)
# change_points = algo.predict(n_bkps=2)  # You can change n_bkps

# --- Step 3: Plotting with Matplotlib ---
plt.figure(figsize=(12, 6))
plt.plot(yearsr, signalr, marker='o', linestyle='-', color='orange', label='Reddit')

plt.plot(yearsy, signaly, marker='o', linestyle='-', color='red', label='YouTube')

# --- Optional: Enhancements ---
plt.title("Sentiment Drift Over Time (Health & Mental Well-being)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Average Compound Sentiment Score", fontsize=12)
plt.xticks(yearsr)  # Show all years on x-axis
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
