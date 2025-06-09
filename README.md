# Pagination application

The purpose of this application is to read a one-line document and paginate it into lines and pages accordingly to configuration.

## Objective

The application:
- Breaks the text into lines of **at most 80 characters**, ensuring words are not split across lines.
- Groups lines into **pages of 25 lines each**.
- Adds a **centered page separator** at the end of each page in the format:  
  `--- Page X ---`


## Project Structure
pagination_app/ <br>
│<br>
├── document.txt # Input file (one line of text)<br>
├── paginated_document.txt # Output file with pagination<br>
├── pagination.py # Main application code<br>
└── README.md # This file<br>


## Requirements

- Python 3.6 or newer


## How to run

1. Clone the repository or download the files to your machine.

2. Run the script:
```bash
python3 pagination.py
```
or depending of your python version
```bash
py pagination.py
```
3. The output, `paginated_document.txt` will be generated in the same directory.

## Author

Arnau Pons Oliván

Contact: arnau18pons@gmail.com