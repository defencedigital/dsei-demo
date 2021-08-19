# DSEI exposition demo



# Script/approach


## Branches/changes

1. `main` branch is the basic build with no improvements made
2. `menu-fix` branch builds on `main` but fixes the `active` class on the navigation bar
3. `pin-colours` branch builds on `menu-fix` branch and makes enemy pins red
4. `pin-icons` branch builds on `pin-colours` branch and uses meaningful icons instead of generic pins

# How to use this repo

## Getting set up locally

To get set up locally, with the app running, follow the following steps (if you're running Windows, you're on your own if this doesn't work):

1. Clone this repository and change directory into the top-level folder

2. [Optional but recommended] Set up a virtual environment

`python3 -m venv venv`

3. Install requirements

`pip install --upgrade pip` (optional)
`pip install -r requirements.txt`

4. Run the server (and then navigate to the localhost port it provides)

`export FLASK_APP=app.py`
`export FLASK_ENV=development` (optional, if you want debug mode on)
`flask run`
As any Python app, you can press `ctrl + c` to end the processs / stop the server.

## Editing the map

If you want to add, remove or edit pins or other parts of the map, you'll need to edit `maps.py`. This file uses a library called [folium](http://python-visualization.github.io/folium/quickstart.html), whose docs explain how to use it. 

Once you edited that file, you'll need to run `python maps.py` to generate a new `maps.html` file locally (this will be done automatically by the deployment pipeline, in case you forget). This html file is what's presented by the Flask app when you go to the "map view" page. 

## The deployment pipeline



## Instigating a build

