
# EEG Visualizer

This Python EEG visualizer consists of three scripts:

1. **Dataextract.py:** This script extracts data from .edf files and calculates features using the provided code.

2. **Features.py:** This script calculates features using the provided code and saves the results to a CSV file named `alldata11.csv`.

3. **Visual.py:** This script visualizes the data extracted and features calculated by `Dataextract.py` and `Features.py`. It loads data from `alldata11.csv`, plots the average Rate of Change of channel C4 over windows, and displays it using Matplotlib.

## Requirements

- Python 3.x
- pandas
- matplotlib

## Usage

1. Run `Dataextract.py` to extract data from .edf files and calculate features.
   ```bash
   python Dataextract.py

2. Run Features.py to calculate features using the extracted data and save the results to alldata11.csv.

3. Run Visual.py to visualize the data.
   
   This will generate a visualization of the average Rate of Change of channel C4 over windows.
