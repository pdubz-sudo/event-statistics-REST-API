# event-statistics-REST-API
Generate and return event statistics through HTTP with REST API

Programming language: Python

The purpose of this assignment was to generate statistics from a user log that gave ratings of movies between January 9, 1995 and 
March 31, 2015 and return that data through HTTP in JSON using a REST API which was built using Flask. The generated statistics tracked 
the events and returned standard deviation, average load per year, minimum year, and maximum year.

The data was collected from MovieLens which is a movie recommendation service https://grouplens.org/datasets/movielens/. 
However, due to size restrictions of github, a smaller version called rating_small.csv is attached to this reposoitory.
The full dataset can be download from either http://files.grouplens.org/datasets/movielens/ml-20m.zip or 
https://www.kaggle.com/grouplens/movielens-20m-dataset. 

*Note: there is a pop-up chart that MUST be closed in order to continue the code and make the API. 
Additionally, years 1995 and 2015 were taken out of the generated statistics because the data was not collected for the whole year and 
year 1995 had almost no data entries; evident when the code is run againg the full dataset.

The code is written in Python. To run the program you can use must install pandas, matplotlib, collections, and Flask
with the following commands:

    pip install pandas
    pip install matplotlib
    pip install collections
    pip install flask


Run the code with the following command

    python code_stas_API.py


Requests will return the generated data to the following endpoints:

http://127.0.0.1:5000/statistics

http://127.0.0.1:5000/statistics/loads

http://127.0.0.1:5000/statistics/loads/stddev

http://127.0.0.1:5000/statistics/loads/min

http://127.0.0.1:5000/statistics/loads/max


Cite: F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive 
Intelligent Systems (TiiS) 5, 4, Article 19 (December 2015), 19 pages. DOI=http://dx.doi.org/10.1145/2827872
