# heycar-techtest

## Getting started
Requirements are in api/requirements.txt, run the following to install:
    
    pip install -r requirements.txt

## Running application locally
Run the following to bring up the API locally (from root directory that contains `manage.py`)

    python manage.py runserver

- To view the API endpoint on DRF's default UI go to http://127.0.0.1:8000/progimage
- To view the admin panel go to http://127.0.0.1:8000/admin

## Running tests
To run the tests run:

    pytest
