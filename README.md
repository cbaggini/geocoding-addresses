
<p align="center">

  <h3 align="center">Geocoding addresses </h3>

  <p align="center">
    Small Django app to get coordinates of addresses as soon as they are written to database using Google Maps API.
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)


<!-- ABOUT THE PROJECT -->
## About The Project

This Django app automatically adds an address' coordinates to the corresponding database table after a new address is saved.
It uses a post-save signal to send a request to Google Maps Geocoding API and writes the coordinates to database if the API returns a unique address. In this case, the "status" column in the database will read "Success".
Otherwise, the "status" column of the table is "No address found" (if no results returned) or "More than one address" (if the API returns more than one possible address).
The app needs to be connected to a local or remote instance of a PostGIS database.


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Python >= 3.7

A PostGIS database

A Google Maps API key [(instructions on how to get one here)](https://developers.google.com/maps/documentation/javascript/get-api-key)


### Installation

1. Clone the repo
```sh
git clone https://github.com/cbaggini/geocoding-addresses.git
```
2. Install the necessary Python packages
```sh
pip install requirements.txt
```
3. Add params.py to the django_project folder. The file should contain the following variables:

GOOGLE_API_KEY: Your API key for Google Maps
RDS_DB_NAME: The database name
RDS_USERNAME: The database admin username
RDS_PASSWORD: The database admin password
RDS_HOSTNAME: Link to remote database or IP for local database instance
RDS_PORT: The database port

<!-- USAGE EXAMPLES -->
## Usage

The start page has an address form where the user can insert their address.
The output page tells the user what the address they entered is and shows a map of the location if the Google Maps API call has been successful.

#### User input page

![alt text](https://github.com/cbaggini/geocoding-addresses/blob/master/user_input.png?raw=true)

#### Output page

![alt text](https://github.com/cbaggini/geocoding-addresses/blob/master/output.png?raw=true)
