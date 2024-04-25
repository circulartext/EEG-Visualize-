import pandas as pd

# Load data from CSV
df = pd.read_csv("11.csv")

# Calculate features for every 5 rows
window_size = 10
num_windows = len(df) // window_size

results = []
for i in range(num_windows):
    start_idx = i * window_size
    end_idx = (i + 1) * window_size
    window_df = df.iloc[start_idx:end_idx]

    # Calculate features for this window
    average_c4 = window_df['C4'].mean()
    std_c4 = window_df['C4'].std()
    diff_c4 = window_df['C4'].diff()

    # Append results to list
    results.append({
        "Window": i + 1,
        "Average_C4": average_c4,
        "Std_C4": std_c4,
        "Rate_of_Change_C4": diff_c4.mean()
    })

# Convert results to DataFrame
results_df = pd.DataFrame(results)

# Save results to CSV
results_df.to_csv("alldata11.csv", index=False)
