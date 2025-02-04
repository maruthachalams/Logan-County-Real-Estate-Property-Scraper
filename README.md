# Logan County Real Estate Property Scraper

This Python script scrapes property details from the Logan County Real Estate website using Selenium and saves the extracted information in a text file. The information includes location, acres, owner, land use, particular, appraised, and assessed values.

## Features
- Scrapes property details from the Logan County Real Estate website.
- Extracts information such as location, acres, owner, land use, particular, appraised, and assessed values.
- Saves the extracted information into a text file (`Output.txt`).

## Requirements
- Python 3.x
- `selenium` library
- `re` library

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/maruthachalams/Logan-County-Real-Estate-Property-Scraper.git
    cd logan-county-property-scraper
    ```
2. Install the required libraries:
    ```sh
    pip install selenium
    ```
3. Download the Chrome WebDriver and ensure it is in your PATH or in the same directory as your script.

## Usage
1. Ensure the input data file `input_property_number.txt` contains the property numbers you want to scrape, with one property number per line.
2. Run the script:
    ```sh
    python scraper.py
    ```
3. The output will be saved in a file named `Output.txt`.

## Code Explanation
### `data_clean(data)`
This function cleans the input data by replacing or removing unwanted characters.

### `single_regex(pattern, target_string)`
This function uses regular expressions to find matches in a target string and returns the first match found.

### Main Script
1. Initializes an output string with headers and writes it to `Output.txt`.
2. Reads property numbers from the `input_property_number.txt` file and stores them in a list.
3. For each property number in the list:
    - Sets up a Chrome WebDriver to automate browser actions.
    - Opens the Logan County Real Estate search page and enters the property number.
    - Retrieves the content of the search results page and writes it to `Result_Page.html`.
    - Cleans the page content and extracts information such as location, acres, owner, land use, and values (particular, appraised, assessed).
    - Formats the extracted information and appends it to `Output.txt`.
    - Prints "completed ID" for each property number.
    - Closes the Chrome WebDriver.

