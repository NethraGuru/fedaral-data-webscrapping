import pandas as pd
import re
import argparse
import os

def clean_data(input_files):
    for input_file in input_files:
        # Extract rate type from filename
        filename = os.path.basename(input_file)
        rate_type = filename.replace('table_data_', '').replace('.csv', '')
        output_prefix = f"cleaned_{rate_type}"

        # Load the CSV file
        df = pd.read_csv(input_file)

        # Identify the column containing the date and value
        df = df.dropna()  # Remove empty rows
        df = df.astype(str)  # Convert all data to string for processing

        # Extract year and rate values using regex
        cleaned_rows = []
        for index, row in df.iterrows():
            for col in df.columns:
                match = re.search(r'(\b\d{4}\b)', row[col])  # Corrected regex pattern
                if match:
                    original_value = row[col]  # Keep the original column value
                    year = int(match.group(1))  # Convert year to integer
                    rate = None

                    # Find the value in the next column
                    col_index = df.columns.get_loc(col)
                    if col_index + 1 < len(df.columns):  # Ensure next column exists
                        rate_value = row[df.columns[col_index + 1]]
                        if re.match(r'^\d+(\.\d+)?$', rate_value):  # Check if it's a valid number
                            rate = float(rate_value)

                    if rate is not None:
                        cleaned_rows.append({"Original_Value": original_value, "Year": year, "Rate": rate})

        # Convert cleaned data into DataFrame
        cleaned_df = pd.DataFrame(cleaned_rows)

        if not cleaned_df.empty:
            cleaned_df["Year"] = cleaned_df["Year"].astype(int)  # Ensure Year column is integer
            latest_year = cleaned_df["Year"].max()
            last_10_years_df = cleaned_df[cleaned_df["Year"] >= latest_year - 10]

            # Save to CSV with rate type in filename
            output_file = os.path.join('data', f"{output_prefix}.csv")
            last_10_years_df.to_csv(output_file, index=False)

            print(f"Cleaned data saved to {output_file}")
        else:
            print(f"No valid data found in {input_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean multiple CSV files containing year and rate data.")
    parser.add_argument("input_files", nargs="+", help="List of CSV files to clean")
    args = parser.parse_args()
    
    clean_data(args.input_files)