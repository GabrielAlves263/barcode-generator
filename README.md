# Barcode Generator with Flask

## Introduction
This project is a barcode generator built using Python and Flask framework. It allows users to generate Code 128 barcodes. The generated barcodes can be saved as png images.

## Features
- Generate Code128 barcodes.
- Save generated barcodes as png images.
- Easy integration with other applications.

## Prerequisites
- Python 3.x
- virtualenv

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/GabrielAlves263/barcode-generator.git
   cd barcode-generator

2. Create and activate a virtual environment:
    ```bash
    venv .venv
    source venv/bin/activate  # For Linux/macOS
    # Or
    .\venv\Scripts\activate   # For Windows

   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
1. Run the Flask Application:
   ```bash
   python run.py
2. To get barcodes, make a POST request to:
   ```
   http://localhost:3000/create-tag

## Testing
- Run test using pytest:
  ```bash
  pytest

You can use tools like cURL or Postman for making HTTP requests.

## Code Quality

- This project utilizes Pylint Pre-commit hooks for code linting. Ensure you have Pylint installed in your environment.

- To manually lint the code:
   ```bash
   pylint run.py

## Built With

- Flask - Web framework
- Cerberus - Data validation
- Pillow - Imaging library
- pytest - Testing framework
- python-barcode - Barcode generation library
- virtualenv - Virtual environment manager