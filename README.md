# Data Visualizer & Analysis Tool
Video Demo:  https://youtu.be/wPiLEgFqZLk
## Overview
This is a Python-based Data Visualizer & Analysis Tool that allows users to load CSV files, analyze their data, and generate visualizations interactively. The program offers a menu-driven interface to perform various data operations such as filtering, exporting, and statistical analysis. This project follows a modular approach, ensuring that each function is testable and reusable. The program uses Pandas for data manipulation and Matplotlib for generating visualizations. Unit tests are implemented using pytest to ensure reliability.

## Features
- Load CSV files and display data
- Show basic statistics about the dataset
- Filter data based on column values
- Export filtered data as a new CSV file
- Generate charts such as histograms, bar charts, and scatter plots
- Modular design with unit tests using pytest

## Project Structure
📁 project-folder/
│-- 📄 project.py # Main script containing core functions
│-- 📄 test_project.py # Unit tests for core functions
│-- 📄 requirements.txt # List of dependencies
│-- 📄 README.md # Project documentation
│-- 📂 Data/ # Folder for sample CSV files
|-- 📁 Output/ # folder for exported output


## Installation
To run this project, ensure you have Python installed. The required dependencies can be installed using the following command:

```bash
pip install -r requirements.txt
If pytest is not installed, install it separately:

bash
Copy
Edit
pip install pytest
Usage
Run the main script to start the program:

bash
Copy
Edit
python project.py
The program provides a menu where users can choose different options:

Load a CSV file

Display basic statistical information

Filter data based on column values

Export filtered data

Generate a chart
Users will be prompted to enter the file path and other required details.

Functions
load_csv(filename)
Loads a CSV file and returns a Pandas DataFrame. If the file does not exist, it returns None.

show_basic_info(df)
Displays basic statistical information about the dataset. If the dataset is empty, it returns a message instead of throwing an error.

filter_data(df, column, value)
Filters the DataFrame based on a specific column and value. Returns the filtered DataFrame. If the column does not exist, an error is raised.

export_data(df, filename)
Exports a given DataFrame to a new CSV file with the specified filename.

generate_chart(df, column, chart_type)
Generates a chart for a specified column using Matplotlib. The user can choose from histograms, bar charts, or scatter plots.

Running Tests
To ensure that all functions work correctly, run the following command:

bash
Copy
Edit
pytest
This will execute the test cases defined in test_project.py and provide a summary of passed and failed tests.

Example CSV File Format
The program works with CSV files that have structured data. Below is an example format:

csv
Copy
Edit
ID,Name,Age,Department,Salary
1,Ali,25,IT,60000
2,Sara,30,HR,65000
3,Ahmed,35,Finance,70000
Users can load their own CSV files as long as they follow a similar structure.

Error Handling
The program includes error handling for the following cases:

Invalid file paths

Empty datasets

Non-existent columns for filtering

Incorrect input types

These cases are managed through exception handling and user-friendly messages.
