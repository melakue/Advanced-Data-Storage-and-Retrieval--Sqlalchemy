# Advanced-Data-Storage-and-Retrieval--Sqlalchemy

### Step 1 - Climate Analysis and Exploration

Python and SQLAlchemy are used to do basic climate analysis and data exploration of climate database. All of the following analysis is completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

### Precipitation Analysis

* Design a query to retrieve the last 12 months of precipitation data.
* Select the date and prcp values.
* Load the query results into a Pandas DataFrame and set the index to the date column.
* Sort the DataFrame values by date.
* Plot the results using the DataFrame plot method.

### Station Analysis

* Design a query to calculate the total number of stations.
* Design a query to find the most active stations.
  * List the stations and observation counts in descending order.
  * Which station has the highest number of observations?

* Design a query to retrieve the last 12 months of temperature observation data (tobs).
  * Filter by the station with the highest number of observations.
  * Plot the results as a histogram with bins=12.

### Step 2 - Climate App

Design a Flask API based on the queries that you have just developed.
* Use FLASK to create your routes.
#### Routes
* /
  * Home page.
  * List all routes that are available.
* /api/v1.0/precipitation
  * Convert the query results to a Dictionary using date as the key and prcp as the value.
  * Return the JSON representation of your dictionary.
* /api/v1.0/stations
  * Return a JSON list of stations from the dataset.
* /api/v1.0/tobs
  * query for the dates and temperature observations from a year from the last data point.
  * Return a JSON list of Temperature Observations (tobs) for the previous year.
* /api/v1.0/<start> and /api/v1.0/<start>/<end>
  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  * When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
  * When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
 
 ### Some Screenshot from the final analysis
 ![Image description](https://github.com/melakue/Advanced-Data-Storage-and-Retrieval-Sqlalchemy/blob/master/Pic1.JPG)
 ![Image description](https://github.com/melakue/Advanced-Data-Storage-and-Retrieval-Sqlalchemy/blob/master/pic2.JPG)
 ![Image description](https://github.com/melakue/Advanced-Data-Storage-and-Retrieval-Sqlalchemy/blob/master/pic3.JPG)
 ![Image description](https://github.com/melakue/Advanced-Data-Storage-and-Retrieval-Sqlalchemy/blob/master/pic4.JPG)






