import os
from flask import Flask, render_template
import json

# create a Flask app
app = Flask(__name__)

def format_title(title):
    title = title.replace('_', ' ')
    title = title.title()
    return title

#JSON_data_reader reads JSON files and iterativly goes through the key values and flattens the data (currently in the depth 4)
#grouping each of the group key values (depth 1), the block key values (depth 2), the item key values (depth 3) and subkey values (depth 4)
# later a column will be made for each of the keys of the flattened data that are the same
def source_JSON_data_reader(source_data):

    grouped_data = []
    temp_ID_index = 0
    #within each flattened entry of my create array, create a key : value_entry
    for group_key, group_value in source_data.items():
        for block_key, block_value in group_value.items():
            if not isinstance(block_value, dict):#if our block key is a dict then we continue, otherwise it ends here
                continue
            for item_key, item_value in block_value.items():
                entry = {"id": temp_ID_index} #creating an ID for each entry
                temp_ID_index += 1
                for sub_key, sub_value in item_value.items():
                    if isinstance(sub_value, dict):
                        for sub_sub_key, sub_sub_value in sub_value.items():
                            entry[f"{sub_sub_key}"] = sub_sub_value
                    else:
                        entry[f"{sub_key}"] = sub_value
                grouped_data.append(entry)

    return grouped_data

#terminology data reader
def terminology_JSON_data_reader(terminology_data):
    grouped_data = []
    temp_ID_index = 0
    # within each flattened entry of my create array, create a key : value_entry
    for concept_id, concept_data in terminology_data["concept_id"].items():
        # creating an ID for each entry
        entry = {"id": temp_ID_index, "concept_id": concept_id}
        temp_ID_index += 1
        # Iterate within the concept data
        for key, value in concept_data.items():
            entry[f"{key}"] = value
        grouped_data.append(entry)

    return grouped_data

#app.route for uploadedtable.html and file reader
@app.route('/')
def filter():

    #file reading
    source_dir = 'source'
    terminology_dir = 'terminology'

    # file input error handling. returns template without tables if there are no files in the directories
    if len(os.listdir(source_dir)) != 1 :
        return render_template('uploadedtable.html', title='Filter Result')

    elif len(os.listdir(terminology_dir)) != 1 :
        return render_template('uploadedtable.html', title='Filter Result')

    source_filename = os.listdir(source_dir)[0]
    terminology_filename = os.listdir(terminology_dir)[0]

    # Construct file paths using the filenames
    source_path = os.path.join(source_dir, source_filename)
    terminology_path = os.path.join(terminology_dir, terminology_filename)

    # Read terminology file

    with open(source_path, 'r') as source_file:
        source_data = json.load(source_file)
        #DEBUGGING
        for key, value in source_data.items():
            print("uploaded_data:")
            print(key, value)
    #store in grouped_data
    grouped_source_data = source_JSON_data_reader(source_data)

    #DEBUGGING
    #display the grouped_data
    print("input_data_grouped:")
    print(grouped_source_data)

    # read source file
    with open(terminology_path, 'r') as terminology_file:
        terminology_data = json.load(terminology_file)
        #DEBUGGING
        for key, value in terminology_data.items():
            print("terminology_data:")
            print(key, value)
    #store in grouped_loinc_data
    grouped_terminology_data = terminology_JSON_data_reader(terminology_data)

    #DEBUGGING
    #display the grouped_loinc_data
    print("grouped_terminology_data:")
    print(grouped_terminology_data)

    #render the uploadedtable.html page
    return render_template('uploadedtable.html', title='Filter Result', source_data=json.dumps(grouped_source_data), terminology_data=json.dumps(grouped_terminology_data))

if __name__ == "__main__":
    app.run(debug=True)
