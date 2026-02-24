[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/YlfKWlZ5)
# Fire Perimeter Analysis

This project processes and visualizes historical fire perimeter data and Canadian CPI data.

## Setup

```bash
conda env create -f environment.yml
conda activate fire_analysis
```

## Project Structure

```
data/
  raw-data/           # Raw data files
    fire.csv          # Historical fire perimeter data
    canadian_cpi.csv  # Canadian Consumer Price Index data
  derived-data/       # Filtered data and output plots
    fire_filtered.gpkg  # Fire data filtered to post-2015
    cpi_filtered.csv    # CPI data filtered to 2020 onwards
code/
  preprocessing.py    # Filters fire and CPI data
  plot_fires.py       # Plots fire perimeters
```

## Usage

1. Run preprocessing to filter data:
   ```bash
   python code/preprocessing.py
   ```

2. Generate the fire perimeter plot:
   ```bash
   python code/plot_fires.py
   ```

## Large Raw Dataset
`building_violations_raw.csv` is >100MB and is not stored in this GitHub repository.

Download (Google Drive):
- https://drive.google.com/file/d/1pgeuZq6TKBKSqyTAro4o173iqnzVodFW/view?usp=sharing
'Link access: anyone with the link can view/download.'

After downloading, save it to this exact path (do not rename):
- `data/raw-data/building_violations_raw.csv`
