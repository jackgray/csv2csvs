# When your machine can't handle a really big csv file, split it up with this script

Run it with 
`python splitCSV.py /path/to/your/spreadsheet.py <lines to split by>`

Where the line count could be 1000, 5000, or more depending on your machine's capabilities. 

Requires pandas library.
Does not currently work on xlsx files.