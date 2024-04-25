import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import itertools

# Load data from CSV
df = pd.read_csv("alldata111.csv")

# Extract columns
windows = df["Window"]
average_c4 = df["Rate_of_Change_C4"]

# Define a list of colors and marker styles
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'orange', 'purple', 'brown']
markers = ['o', 's', 'D', '^', 'v', '>', '<', 'p', '*', 'x']

# Create an iterator that cycles through colors and markers
marker_color_iterator = itertools.cycle(zip(markers, colors))

# Define update function for animation
def update(frame, data, plots, marker_color_iterator):
    marker, color = next(marker_color_iterator)  # Get next color and marker style
    plots[frame], = ax.plot(frame, data[frame], marker=marker, markersize=5, linestyle='', color=color)  # Plot data for current frame
    ax.set_xlabel("Window")
    ax.set_ylabel("Average C4")
    ax.set_title("Average C4 Over Windows")
    ax.grid(True)

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Initialize list to store plot objects
plots = [None] * len(windows)

# Initialize animation
ani = FuncAnimation(fig, update, frames=range(len(windows)), fargs=(average_c4, plots, marker_color_iterator), interval=.01, repeat=False)

# Show plot
plt.show()
