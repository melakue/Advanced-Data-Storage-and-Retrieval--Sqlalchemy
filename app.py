import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurment_data = Base.classes.measurement
station_data=Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return date and precepitation"""
   
    results = session.query(Measurment_data.date,Measurment_data.prcp).all()

    climate_data = []
    for date, prcp in results:
        cliamte_dict = {date:prcp}
        # cliamte_dict["Date"] = date
        # cliamte_dict["Precipitation"] = prcp
        
        climate_data.append(cliamte_dict)

    return jsonify(climate_data)


   

@app.route("/api/v1.0/stations")
def stations():
    # """Return a list of stations"""
    # Query all stations
    results = session.query(station_data.id,station_data.name).all()

    Station_list = []
    for id, name in results:
        Station_dict = {}
        Station_dict["Station id"] = id
        Station_dict["Station Name"] = name
        Station_list.append(Station_dict)

    return jsonify(Station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    # Query tobs for the last one year
    # print(f"dates and temperature observations from a year from the last data point:<br/>")
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurment_data.date,Measurment_data.tobs).filter(Measurment_data.date>=one_year_ago).all()

    tobs_list = []
    for date,tobs in results:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Temperature Observations"] = tobs
        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)


@app.route("/api/v1.0/<start_time>")
def temprature(start_time):
    
    
    results=session.query(func.min(Measurment_data.tobs), func.avg(Measurment_data.tobs), func.max(Measurment_data.tobs)).filter(Measurment_data.date >= start_time).all()
    
    return jsonify(results)


@app.route("/api/v1.0/<start>/<end>")
def temprature_For_start_end(start_time,end_time):
    
    
    results=session.query(func.min(Measurment_data.tobs), func.avg(Measurment_data.tobs), func.max(Measurment_data.tobs)).filter(Measurment_data.date < end_time).filter(Measurment_data.date >= start_time).all()
    
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)

