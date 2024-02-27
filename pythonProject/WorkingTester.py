import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import json

app = Flask(__name__) #this is just referencing this file, __name__ represent name of current module

ALLOWED_EXTENSIONS = {'json'} #Setting which files are allowed


def allowed_file(filename): # checks if uploaded file is an allowed file
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
    initial_group_key = None
    temp_ID_index = 0
    #within each flattened entry of my create array, create a key : value_entry
    for group_key, group_value in uploaded_data.items():
        for block_key, block_value in group_value.items():
            if not isinstance(block_value, dict):
                continue
            for item_key, item_value in block_value.items():
                entry = {"id": temp_ID_index, "initial_group_key": initial_group_key} #creating an ID for each entry
                temp_ID_index += 1
                for sub_key, sub_value in item_value.items():
                    if isinstance(sub_value, dict):
                        for sub_sub_key, sub_sub_value in sub_value.items():
                            entry[f"{sub_sub_key}"] = sub_sub_value
                    else:
                        entry[f"{sub_key}"] = sub_value
                grouped_data.append(entry)

    return grouped_data

#app.route defines mapping between a URL route and a function, when root URL / (my endpoit /) called,
@app.route('/', methods=['GET', 'POST']) #method GET requests an upload and POST processes the file to perform the necessary actions
def upload_file(): # upload_file function is called
    if request.method == 'POST': # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part has been uploaded', 'No_File')
            return redirect(request.url) #We have checked if a file is uploaded, now that we can confirm it has,
        file = request.files['file'] #we assign the file variable the file object from the request.files dictionary
        if file.filename == '': # If the user does not select a file, the browser submits an
            flash('No file has been selected yet', 'No_Selection') # empty file without a filename. i.e. nothing uploaded yet
            return redirect(request.url)
        if file and allowed_file(file.filename): #allowed_file designed to accept a filename as its argument, not a file object
            filename = secure_filename(file.filename)
            file_path = os.path.join(get_upload_folder(file.filename), file.filename)
            app.config['UPLOAD_FOLDER'] = get_upload_folder(file_path)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('filter', name=filename))
    return render_template('home.html', title='Upload new File')


@app.route('/filter/<name>')
def filter(name):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], name) #app.config dictionary-like object to store configuration options
    # (used to set various options of the app, like security settings, database connections etc) for my flask app, globally accesible

    # Read the content of the file
    with open(file_path, 'r') as file:
        uploaded_data = json.load(file)

    grouped_data = JSON_data_reader(uploaded_data)

    print(grouped_data)

    return render_template('uploadedtable.html', title='Filter Result', data=json.dumps(grouped_data))


if __name__ == "__main__":
    app.run(debug=True)
