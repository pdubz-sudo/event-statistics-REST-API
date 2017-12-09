import pandas as pd
from collections import defaultdict
from flask import Flask, jsonify, make_response


df = pd.read_csv('rating_small.csv')

### memory usage and some quick stat info
# df.info(memory_usage="deep")
# df.memory_usage()
# df.describe()

# parse the timestamp because it's currently an object
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Double check it's been parse correctly
# df.timestamp.dtype


# Calculate load per year and reset index. "A" is annual
load_per_year = df.groupby(pd.Grouper(key="timestamp", freq="A")).count()
load_per_year.reset_index(inplace=True)

### check type of timestamp
# print(load_per_year.dtypes)
# print(load_per_year)  ########## the print shows that 1995 only has 4 entries


### double check that 1995 really has only 4 entries in originial df with code below
# df[(df['timestamp'] > '1995-01-01 00:00:00') & (df['timestamp'] < '1996-01-01 00:00:00')]

### Confirmed to contain only 4 entries so remove 1995 from load_per_year dataframe.
### Additionally remove 2016 because that data was only collected until March 31,2015
load_per_year = load_per_year.iloc[1:20,:] # you used same variable to avoid slice on copy warning


# convert timestamp back to string and only had the year label
load_per_year["timestamp"] = load_per_year["timestamp"].dt.strftime("%Y")


# keep timestamp and one other columns for keeping track of the entries count
load_per_year.drop(['movieId', 'rating'], axis=1, inplace=True)


# rename time grouping and the other column to a count label
load_per_year.rename(columns = {"timestamp": "year collected", "userId": "number of entries"}, inplace=True)


# final step is convert to list of dictionaries for the API. Call the list loads because your endpoint it /loads
loads = load_per_year.to_dict("records")
# type(loads)    # to double check that you created a list of dictionaries


# calculate min,max,standard dev, and average and make sure they're all integers for the API
year_max = int(load_per_year.max()[1])
year_min = int(load_per_year.min()[1])
standard_dev_loads = int(load_per_year.std()[0])
average_load = int(load_per_year.mean()[1])


# make a dictionary of all the stats together
# use defaultdict to make an empty dict
statistics = defaultdict(dict)  # makes an empty dictionary
statistics["loads per year"] = loads
statistics["max load per year"] = year_max
statistics["min load per year"] = year_min
statistics["standard deviation of loads per year"] = standard_dev_loads
statistics["average loads per year"] = average_load

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

int_load = load_per_year.iloc[:, :2]

plt.bar(range(len(int_load['number of entries'])), int_load['number of entries'])
plt.xticks(range(len(int_load['year collected'])),["'97","'98",",99","'00","'01","'02","'03","'04","'05","'06","'07",
                                              "'08","'09","'10","'11","'12","'13","'14","'15"], size='small')
plt.xlabel("Year")
plt.ylabel("Events Load")
plt.title("Year vs Events Load --CLOSE WINDOW TO CONTINUE CODE--")
plt.show()

##########################################################
##########################################################
### Make Flask API

# create app from Flask class which gives each file a unique name
app = Flask(__name__) 

# Make request decorator that fires after the request is made so all requests get the the custom header
@app.after_request
def after_request(response):
    response.headers["X-Service_Version"] = "v0.1.0"
    return response

# GET /statistics
@app.route("/statistics") 
def get_statistics():
    return jsonify({"statistics": statistics})

# GET /statistics/loads
@app.route("/statistics/loads") 
def get_statistics_loads():
    return jsonify({"loads per year": loads})

# GET /statistics/loads/avg
@app.route("/statistics/loads/avg")
def get_statistics_avg():
    return jsonify({"average loads per year": average_load})

# GET /statistics/loads/stddev
@app.route("/statistics/loads/stddev") 
def get_statistics_sttdev():
    return jsonify({"standard deviation of loads per year": standard_dev_loads})

# GET /statistics/loads/min
@app.route("/statistics/loads/min")
def get_statistics_min():
    return jsonify({"min load per year": year_min})

# GET /statistics/loads/max
@app.route("/statistics/loads/max")
def get_statistics_max():
    return jsonify({"max per year": year_max})

# GET /statistics/loads/<string:name>   # returns message that the desired calculation does not exist
@app.route('/statistics/loads/<string:name>')
def get_not_performed_message(name):
    if name not in ("loads", "avg", "min", "max"):
        return jsonify({"message": "calculation not performed"})

app.run(port=5000)