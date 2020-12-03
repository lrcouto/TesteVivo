# TesteVivo

This is a technical test for a jr. developer position at Telefônica VIVO. It was also my first contact with Python and with Flask APIs. I chose to work with python for its powerful libraries and tools to work with data, as well as easily accessible documentation.

# First Exercise

I interpreted the exercise to have a constant array with numbers from 0 to 15, and variable matrixes. To achieve that, I generate a different matrix every time the program is called, iterate the array through each element of the matrix, and record the number of matches on another array, which will be returned as JSON. The user can input the size of the matrix as a query, allowing for repeated testing.

# Second Exercise

I mainly used Pandas' DataFrames to work on this challenge. For the log, since it was part of the original PDF, I assumed it would be input in a plain text format. Each column of the DataFrame is converted to the appropriate data type, and it is then sliced and selected for useful information, which is then processed and stored in dictionaries. The dictionaries were chosen for their key: value structure, which would make the conversion to a JSON output easier.

# Setting up a Python Virtual Environment

Create environment:

```python3 -m venv ./venv```

Activate environment:

```source ./venv/bin/activate```

# Installing depencencies

```pip install Flask```

```pip install numpy```

```pip install pandas```

# Running the API

```export FLASK_APP=file_name.py```

```flask run```

# Resources used for studying

Flask - https://flask.palletsprojects.com/en/1.1.x/

REST API - https://restfulapi.net/

Python Virtual Environment - https://docs.python.org/3/library/venv.html

PIP(Linux) - https://www.tecmint.com/install-pip-in-linux/

Basic Python guide - https://www.w3schools.com/python/default.asp

NumPy guide - https://www.geeksforgeeks.org/python-numpy/

Pandas DataFrame documentation - https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
