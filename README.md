# JSONMapper
A simple library to map JSON to a class and vice versa.

## Installation

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
Checkboxes at the start of each row can be used to select the rows to be mapped. Only one terminology code can be mapped to many source codes. To map click the button "Map Data". The value "Target Val" of the source table on the left will be updated after. The button "Undo" can remove any mapped input in "Target Val" of the source table. To exit and save hit "Export". A dialog will open to save the source file with the updated Target Val.

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

