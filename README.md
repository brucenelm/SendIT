About

SendIT is a courier service that helps users deliver parcels to different destinations. SendIT
provides courier quotes based on weight categories.

The goal of this project is to provide a uniform API for both web and mobile frontend SendIT applications.
## Features
With this API;
- You can create a user account - Registration
- You can login and log out - Authorization and Authentication
- You can create, view, update, and cancel delivery orders
## API Documentation
Documentation for this API can be found at http://127.0.0.1:5000.
## Tools
Tools used during the development of this API are;
- [Flask](http://flask.pocoo.org/) - this is a python micro-framework

## Requirements
- Python 2.7.1x+. preferably use Python 3.x.x+
## Tests
   $ cd SendIT 
   $ python test.py

## Running the application
To run this application on a linux box, execute the following command.

    $ cd SendIT
    $ source virtenv/bin/activate
    
#### Endpoints 
HTTP Method|End point | Action
-----------|----------|-----------------------------------------
GET | /v1/parcels |  Fetch all parcel delivery orders
GET | /v1/parcels/<parcelid> | Fetch a specific parcel delivery order
GET | /v1/users/<userid>/parcels  | Fetch all parcel delivery orders by a specific user
PUT | /v1/parcels/<parcelid>/cancel | Cancel the specific parcel delivery order
POST| /v1/parcels | Create a parcel delivery order
