import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import json

# create a Flask app
app = Flask(__name__)

# set of allowed file extensions
ALLOWED_EXTENSIONS = {'json'}

# check if uploaded file is an allowed file type
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def get_upload_folder(file_path):
    upload_folder = os.path.dirname(file_path)
    return upload_folder

def format_title(title):
    title = title.replace('_', ' ')
    title = title.title()
    return title

#JSON_data_reader reads JSON files and iterativly goes through the key values and flattens the data (currently in the depth 4)
#grouping each of the group key values (depth 1), the block key values (depth 2), the item key values (depth 3) and subkey values (depth 4)
# later a column will be made for each of the keys of the flattened data that are the same
def JSON_data_reader(uploaded_data):
    grouped_data = []
    temp_ID_index = 0
    #within each flattened entry of my create array, create a key : value_entry
    for group_key, group_value in uploaded_data.items():
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

#Loinc data reader
def Loinc_JSON_data_reader(uploaded_data):
    grouped_data = []
    temp_ID_index = 0
    # within each flattened entry of my create array, create a key : value_entry
    for concept_id, concept_data in uploaded_data["concept_id"].items():
        # creating an ID for each entry
        entry = {"id": temp_ID_index, "concept_id": concept_id}
        temp_ID_index += 1
        # Iterate within the concept data
        for key, value in concept_data.items():
            entry[f"{key}"] = value
        grouped_data.append(entry)

    return grouped_data


#app.route for home.html and upload_file function
@app.route('/', methods=['GET', 'POST'])

#upload_file function will be called when the user submits the form on the home page
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file and error handling
        if 'file' not in request.files:
            flash('No file part has been uploaded', 'No_File')
            return redirect(request.url)
        # assign the file to the variable file
        file = request.files['file']
        # if user does not select file return an error message
        if file.filename == '':
            flash('No file has been selected yet', 'No_Selection')
            return redirect(request.url)
        # if the file is valid and allowed to be uploaded, save the file
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(get_upload_folder(file.filename), file.filename)
            app.config['UPLOAD_FOLDER'] = get_upload_folder(file_path)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('filter', name=filename))
    # render the home.html page
    return render_template('home.html', title='Upload new File')


#app.route for uploadedtable.html and file reader
@app.route('/filter/<name>')
def filter(name):
    # Get the input file path
    input_file_path = os.path.join(app.config['UPLOAD_FOLDER'], name)

    # Read the content of the file
    with open(input_file_path, 'r') as input_file:
        uploaded_data = json.load(input_file)
        #DEBUGGING
        for key, value in uploaded_data.items():
            print("uploaded_data:")
            print(key, value)
    #store in grouped_data
    input_data_grouped = JSON_data_reader(uploaded_data)
    #DEBUGGING
    #display the grouped_data
    print("input_data_grouped:")
    print(input_data_grouped)

    #read loinc file
    with open(r'C:\Users\konst\Downloads\latest\JSONMapper\pythonProject\templates\blank.json', 'r') as loinc_file:
        loinc_data = json.load(loinc_file)
        #DEBUGGING
        for key, value in loinc_data.items():
            print("loinc_data:")
            print(key, value)
    #store in grouped_loinc_data
    grouped_loinc_data = Loinc_JSON_data_reader(loinc_data)
    #DEBUGGING
    #display the grouped_loinc_data
    print("grouped_loinc_data:")
    print(grouped_loinc_data)

    #render the uploadedtable.html page json.dumps is used to convert the grouped_data to a string
    return render_template('uploadedtable.html', title='Filter Result', input_data=json.dumps(input_data_grouped), loinc_data=json.dumps(grouped_loinc_data))

if __name__ == "__main__":
    app.run(debug=True)
