## Overview

Side project to visualize how time is allocated to different activities throughout the day, i.e. daily routine. Pie chart represents a 24-hour day, which is divided into various sections representing how much of the day each activity consumed.

Time for the day must be tracked and saved to a CSV file; see `sample.csv` as an example. Different readers are implemented to read CSV files from various sources, so tracked time can either be recorded manually or using time tracking tools that can export CSV files. Currently supported tools are:
- Toggl Track

## Documentation

### Pre-requisites
1. python 3
1. pip (for python 3)
1. modules from requirements.txt

### Installation

```console
python main.py
```

## Roadmap
1. Automatically calculate untracked time throughout the day
1. Cleaner visualization 
1. Support CSV formats from more time tracking tools
1. Visualization of weeks, months, years
1. Heat map of when activities are usually done
