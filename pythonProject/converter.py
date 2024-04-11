import csv
import json

def csv_to_json(csv_file, json_file, encoding='utf-8'):
    # Open the CSV file for reading with the specified encoding
    with open(csv_file, 'r', encoding=encoding) as csv_input:
        # Create a CSV reader
        csv_reader = csv.DictReader(csv_input, delimiter='\t')

        # Create a dictionary to store the data
        data = {}

        # Iterate over each row in the CSV
        for row in csv_reader:
            # Use the "concept_id" as the primary key
            primary_key = row.pop('concept_id')  # Remove and get the concept_id

            # Store the row data in the dictionary using the primary key
            data[primary_key] = row

    # Wrap the data in another dictionary with "concept_id" as the key
    wrapped_data = {'concept_id': data}

    # Open the JSON file for writing
    with open(json_file, 'w') as json_output:
        # Write the JSON data to the file
        json.dump(wrapped_data, json_output, indent=4)

# INSERT FILEPATHS HERE
csv_file_path = r'C:\'
json_file_path = r'C:\'

csv_to_json(csv_file_path, json_file_path)
