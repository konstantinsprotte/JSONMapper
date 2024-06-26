# JSONMapper
A simple library to easily and visually map JSON data from a Terminology file to a Source File.

Place the file on which data will be mapped in the Source Folder and the file to be mapped from in the Terminology Folder.

## Installation
Execute the setup file for either Mac/Linux or Windows to make sure the required libraries are downloaded and to gain access to the Terminology and Source Folders.

Executing the setup.sh file for Mac/Linux:
1. Navigate to your Command Prompt Terminal
2. Make sure you are in the project directory JSONMapper [cd /path/to/the/project/directory]
3. Make sure the setup file has executable permissions, you can make it executable by running [ chmod +x setup.sh ] within the directory
4. Execute the setup.sh script by running [ ./setup.sh ]

Executing the setup.bat file for Windows
1. Navigate to your Command Prompt Terminal
2. Make sure you are in the project directory JSONMapper [cd /path/to/the/project/directory]
3. Execute the setup.bat script by running [ ./setup.bat ]

Required libraries:
- flask
- os
- json

## Usage
### Data preparation
Provided in the project directory is a script (converter.py) to convert terminology data from .csv to JSON. This is optimized for Athena Format. Insert filepaths at the bottom of the code (line 30 & 31) and run converter.py.

### Running the code
Put the dictionary file in the project folder "terminology" and the file to edit in the project folder "source". Run JSONMapper.py and open the WebApp in your browser (http://127.0.0.1:5000/).

### Mapping
Checkboxes at the start of each row can be used to select the rows to be mapped. Only one terminology code can be mapped to many source codes. To map click the button "Map Data". The value "Target Val" of the source table on the left will be updated after. To remove a current input in "Target Val", select the desired row and hit the "Undo" button which will remove any selected "Target Val" inputs. To exit and save hit "Export". A dialog will open to save the source file with the updated Target Val.

### Table filtering
Columns: You can select which columns to display by using the dropdown menu above each table.

Search: The searchbar above each table can be used to filter the table by the entered string.

Shown entries: The dropdown menu below each table can be used to select how many entries are shown per page.

Show only selected: This button can be used to filter the table to only display the selected rows.

Show already mapped/Show all: This button is helpful to filter your source table to only display mapped or to display all entries.

## Troubleshooting

On startup print statements display the read data on the console. Check if the data is read correctly.

## License

JSONMapper © 2024 by Anton Burckhardt and Konstantin Sprotte is licensed under CC BY-NC-SA 4.0. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/

