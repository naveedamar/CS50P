# 👽 UFO Sightings Analyzer 👽
A final project for Harvard's CS50's Introduction to Programming with Python, leveraging concepts from both CS50 and the University of Pennsylvania's Java and Python Specialization on Coursera.

## Video Demo:

## Description:

### 📁 About the Project

**UFO Sightings Analyzer** is a user-friendly Python command-line interface (CLI) designed to explore and analyze a rich dataset of over **80,000** reported UFO sightings primarily from the **National UFO Reporting Center (NUFORC)** from around the globe. Users can explore top UFO shapes, durations, and sighting locations (city, state, country), as well as search and count sightings based on these criteria. The project handles real-world CSV data, offering a user-friendly interface to investigate the mysteries of reported UFO encounters.

**CSV Source Citing**
Name of the dataset : ufo-reports
Dataset creator's name : Sigmond Axel
Year & Month of dataset creation : 2014, July 9th
URL of the dataset : [https://github.com/planetsig/ufo-reports]

**Dive into decades of mysterious encounters and uncover patterns in the unknown.**

With **UFO Sightings Analyzer**, you can interactively:

- Discover the **top reported UFO shapes**.
- Investigate sightings based on the **shape** of the observed object.
- Explore sighting locations by **city, state, or country**.
- Examine detailed reports, including timestamps, geographical coordinates, and reported shapes.

### 🗂️ Dataset

The core of this project is the comprehensive dataset stored in: `data/ufo_sightings.csv`.

This fascinating dataset contains over 80,000 records of UFO sightings spanning the last century. Each entry provides valuable information, including:

| Column                 | Description                                       |
|------------------------|---------------------------------------------------|
| `datetime`             | Date and time when the sighting occurred          |
| `city`                 | The city where the UFO was sighted                |
| `state`                | The US state of the sighting (if in the US)       |
| `country`              | The country where the sighting was reported       |
| `shape`                | The reported shape of the observed UFO            |
| `duration (seconds)`   | The duration of the sighting in seconds           |
| `duration (hours/min)` | The duration of the sighting in hours and minutes |
| `comments`             | Free-text notes or descriptions from the reporter |
| `date posted`          | The date when the sighting was posted online      |
| `latitude`             | The geographic latitude of the sighting location  |
| `longitude`            | The geographic longitude of the sighting location |

### 💻 How to Use
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/ufo-analyzer.git](https://github.com/yourusername/ufo-analyzer.git)
   cd ufo-analyzer

2. Ensure your dataset is located at data/ufo_sightings.csv.

3. Run the application:
    ```bash
    python main.py

4. Explore the Menu: Follow the interactive on-screen menu to begin your analysis of the UFO sightings data!

### 🔍 Example Usage

When you run main.py, you'll be presented with a menu similar to this:

   --- UFO Sightings Analyzer ---
    1. View Top N Durations
    2. Count Sightings by Duration
    3. View Top N Shapes
    4. Count Sightings by Shape
    5. View Top N Regions
    6. Count Sightings by Region
    7. Exit

    Enter your choice (1-7):

### 📌 Features:
    Intuitive CLI: A simple and user-friendly command-line interface for easy interaction.
    Real-world Data Handling: Efficiently processes a large CSV dataset.
    Flexible Searches: Conduct case-insensitive searches for shapes and regions.
    Organized Code: Implemented with modular and reusable Python functions for clarity and maintainability.
    Comprehensive Analysis: Offers functionalities to explore top trends and specific occurrences in the data.

## Functions Explanation:

1. load_data(): Reads and parses the UFO sightings CSV file into a list of dictionaries.
2. count_by_duration(): Counts sightings with a duration greater than or equal to a given value.
3. get_top_durations(): Returns the N most frequent sighting durations.
4. get_all_shapes(): Extracts all unique UFO shapes from the data.
5. count_by_shape(): Counts sightings of a specific UFO shape.
6. get_top_shapes(): Returns the N most frequently reported UFO shapes.
7. get_region_values(): Extracts all unique values for a specified region (city, state, country).
8. count_by_region(): Counts sightings in a specific region with a given value.
9. get_top_regions(): Returns the N most frequently sighted regions for a given type.
10. search_by_duration(), search_by_shape(), search_by_region(): Return lists of sightings matching specific criteria.
11. display_sightings(): Prints a list of sighting dictionaries in a readable JSON format.

### 📁 File Structure:
    .
    ├── data/
    │   └── ufo_sightings.csv
    ├── main.py
    ├── test_project.py
    ├── README.md
    ├── requirenments.txt
