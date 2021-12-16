import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from sklearn.cluster import KMeans

def model(kelurahan,kecamatan) :
    data = pd.read_csv('data_rs.csv')

    kel = kelurahan 
    kec = kecamatan
    query = kel + " " + kec

    geolocator = Nominatim(user_agent="my_request")
    
    try :
        location = geolocator.geocode(query)
        Lat = location.latitude
        Lon = location.longitude
        Loc = location.address
    except :
        Lat = None
        Lon = None
        Loc = None

    data.loc[-1] = [None, None, None, None, kel, kec, None, query, Loc, Lat, Lon]

    X = data.loc[:,"Lat":"Lon"]
    kmeans = KMeans (20)
    kmeans.fit(X)  

    y = kmeans.fit_predict(X)
    y

    data['cluster'] = y
    result = data[data['cluster'] == data['cluster'][-1]]
    result.drop(-1,axis=0,inplace=True)
    result.reset_index(inplace=True)
    return result
