from os import name
import pandas as pd
from flask import Flask, jsonify
from pandas.core.tools.datetimes import to_datetime
from pandas.core.tools.timedeltas import to_timedelta

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Read the log file into a dataframe, using a regex expression to define the separators.

data = pd.read_csv('log.txt', sep=';|–|[|]', skiprows=1, engine='python', header=None,
names=["Time", "Number", "Name", "Lap", "LTime", "Speed"])

# Replace commas with periods on the speed column, so I can convert it to float.

data['Speed'] = data['Speed'].str.replace(',','.')
data['Speed'] = data['Speed'].astype(float)

# Convert time-based information into datetime type.

data['LTime'] = pd.to_datetime(data['LTime'], format='%M:%S.%f')
data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S.%f')

# Filtering dataframe from the point the first character finished lap 4 to extract ranking information.

df_ranking = data[(data['Lap'] == 4).cummax()]

# Remove last row, since the character is duplicated and I only need one instance to rank it.

df_ranking.drop(df_ranking.tail(1).index,inplace=True)

# Creating ranking column basead on the order characters appear on the previous operation.

ranking = [1, 2, 3, 4, 5, 6]
df_ranking['Ranking'] = ranking

# Removing columns with data that's irrelevant, leaving only numbers as a key to merge plus the ranking info.

del df_ranking["Time"], df_ranking["Lap"], df_ranking["LTime"], df_ranking["Name"], df_ranking["Speed"]

# Merge ranking info to the original dataframe.

data = pd.merge(data, df_ranking, how="left", on="Number")

# Filtering my dataframe to access information pertinent to each character easily.

df_super = data[data['Number'] == 38]
df_flash = data[data['Number'] == 33]
df_merc = data[data['Number'] == 2]
df_sonic = data[data['Number'] == 23]
df_papaleg = data[data['Number'] == 15]
df_gatoajato = data[data['Number'] == 11]

# Convert datetime column to string, then to timedelta, so I can use the .sum()
# method to get the total race time.

def race_time(data):
	original_time = pd.DataFrame(data['LTime'].astype(str))
	split_time = pd.DataFrame(original_time.LTime.str.split(' ',1).tolist(), columns = ['first','Last'])
	time_sum = to_timedelta(split_time['Last']).sum()
	return time_sum

# Populate a dictionary with the info from the dataframe.

def get_runner(data):
	runner = {
		"Name": str(data.iloc[0]['Name']),
		"Number": str(data.iloc[0]['Number']),
		"Ranking": str(data.iloc[0]['Ranking']),
		"Average Speed": str(data['Speed'].mean()),
		"Laps Completed": str(data['Lap'].max()),
		"Total Race Time": str(race_time(data))
	}
	return runner

# Convert each individual character info to a dictionary.

superman = get_runner(df_super)
flash = get_runner(df_flash)
sonic = get_runner(df_sonic) 
merc = get_runner(df_merc)
papaleg = get_runner(df_papaleg)
gatoajato = get_runner(df_gatoajato)

# Export as JSON.

@app.route('/', methods=['GET'])
def get_all():
	return jsonify(superman, flash, merc, sonic, papaleg, gatoajato)

if __name__ == '__main__':
	app.run(debug=True)
