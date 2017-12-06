# event-statistics-REST-API
Generate and return event statistics through HTTP with REST API

The purpose of this assignment was to generate statistics from a log of users that gave ratings of movies 
between January 9, 1995 and March 31, 2015 and return that data through HTTP. The data was collected 
from MovieLens which is a movie recommendation service which is included as rating.csv
and can additionally be found at https://grouplens.org/datasets/movielens/. 
The generated statistics tracked the events and returned standard deviation, average load per year, minimum year, and maximum year.
The results were then returned through HTTP using a REST API which was built using Flask. 

The code is written in Python. To run the program you can use the attached virtual environment named REST_venv. Use the virtual 
environment and run the code with the following command

    python stas_API.py


To return the results you just have to open a web browser (preferably Chrome) and write one of the following in the address bar:

http://127.0.0.1:5000/statistics
http://127.0.0.1:5000/statistics/loads
http://127.0.0.1:5000/statistics/loads/stddev
http://127.0.0.1:5000/statistics/loads/min
http://127.0.0.1:5000/statistics/loads/max

This will return the desired result in JSON format.

Note: Years 1995 and 2015 were taken out of the generated statistics because they data was not collected for the whole year and year 1995 
had almost no data entries.



Cite: F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive 
Intelligent Systems (TiiS) 5, 4, Article 19 (December 2015), 19 pages. DOI=http://dx.doi.org/10.1145/2827872
