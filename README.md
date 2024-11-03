# stickertranslate

## Description
stickertranslate is a Python script that allows users to fetch and display information about stickers from a remote API. Users can input non-human-readable SKU to get the human-readable name, stock, and a preview of the sticker. Useful for when sticker SKUs is shown but not the name. For example, Older version of shipment viewer.

## Features
- Fetch sticker data from a remote API
- Input SKU to get sticker details
- Display sticker name, stock, and preview image
- Indicate stock status (in stock, low stock, out of stock)

## Requirements
- Python 3.x
- `requests` library
- `colorama` library
- `venv` Installed

## Installation

All commands below assume that your shell is bash or zsh.

1. Clone the repository:
    ```sh
    git clone https://github.com/noigamegun/stickertranslate.git
    cd stickertranslate
    ```

2. Make a virtual enviroment:
    ```sh
    python3 -m venv ./venv/
    ```

3. Install the required libraries:
    ```sh
    source ./venv/bin/activate
    pip3 install requests colorama
    ```

## Usage
1. Run the script:
    ```sh
    python3 main.py
    ```

2. Follow the prompts to input a SKU and get sticker details.

## License
This project is licensed under the GPLv3 License.