"""
Project		: Kuma-DoTech Automation Tools
Author		: Kuma-DoTech.Dev
Description	: High-performance utility to convert raw JSON data into clean CSV reports.
             	  Optimized for data mining and web scraping workflows.
"""

import json
import csv
import os

def convert_json_to_csv(input_file, output_file):
    """
    Kuma-DoTech.Dev Utility: JSON to CSV Converter
    Function: Converts scraping results (JSON) into a business-ready format (CSV).
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: File {input_file} not found.")
            return

        # Load JSON data
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Validate JSON format (must be a list of dictionaries)
        if not isinstance(data, list):
            print("Error: JSON format must be a list of items.")
            return

        # Extract headers from the first dictionary keys
        headers = data[0].keys()

        # Write to CSV file
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

        print(f"Success! Data successfully converted to: {output_file}")

    except Exception as e:
        print(f"Technical error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage for demonstration
    input_json = 'raw_data.json' 
    output_csv = 'clean_report.csv'
    
    print("--- Kuma-DoTech Data Processor ---")
    convert_json_to_csv(input_json, output_csv)
