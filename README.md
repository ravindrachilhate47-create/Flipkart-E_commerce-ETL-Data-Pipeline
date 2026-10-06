# Flipkart-E_commerce-ETL-Data-Pipeline

Flipkart Sales Data Cleaning Pipeline (Basic)

A simple, beginner-friendly ETL (Extract, Transform, Load) pipeline built in Python. It reads a raw sales CSV file, inspects it, cleans it, and saves the cleaned version to a new CSV file.


This is a basic version built as part of my Data Engineering learning journey — the goal was to practice core concepts (OOP, file handling, data cleaning with Pandas, logging, error handling), not to build a production-ready pipeline. It's kept simple on purpose.


What It Does
Raw CSV  →  Extract  →  File Info (inspect)  →  Transform (clean)  →  Load  →  Clean CSV
Extract — Reads the raw CSV file using Pandas.
File Info — Looks at the data before cleaning it: shape, column types, missing values, and duplicate rows.
Transform — Cleans the data:
Strips extra whitespace from text columns (Product Name, Category)
Fills missing values in Price (INR) with 0
Load — Saves the cleaned data to a new CSV file, automatically creating the output folder if needed.
Tech Used
Tool	Purpose
Python	Core language
Pandas	Reading, inspecting, and cleaning data
logging	Tracking pipeline progress and errors
pathlib	Safe file path handling
How to Run
Update the input_files and output_files paths at the top of the script to point to your own CSV file and desired output location.
Run:
bash
python pipeline.py


If successful, you'll see logs like:


INFO:root:Reading CSV files

INFO:root:Basic info in Files

INFO:root:Transforming data

INFO:root:Loading a files on PC

INFO:root:pipeline completed successfully


What I Learned Building This
Structuring code using OOP — a class with extract, file_info, transform, load, and run methods
Using Pandas to inspect real-world data before deciding how to clean it
Handling file paths safely using pathlib, including auto-creating output folders
Using logging instead of print() to track pipeline progress
Handling errors with try-except so the pipeline fails with a clear message instead of crashing
Debugging real issues step by step — typos, missing return statements, indentation mistakes
Note

This is a basic/learning-stage pipeline, not a finished production tool. Planned next steps (not yet done):

Load the cleaned data into a database/data warehouse
Add more thorough data validation
Automate it to run on a schedule
Author

Built by Ravindra Chilhate as part of my Data Engineering learning journey.
