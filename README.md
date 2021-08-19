# DSEI Demo

[![Build and Push Image](https://github.com/defencedigital/dsei-demo/actions/workflows/buildah-build.yaml/badge.svg)](https://github.com/defencedigital/dsei-demo/actions/workflows/buildah-build.yaml)

[![GitHub Pages](https://github.com/defencedigital/dsei-demo/actions/workflows/ghpages.yml/badge.svg)](https://github.com/defencedigital/dsei-demo/actions/workflows/ghpages.yml)

This is the Defence Digital Foundry demo app for the [DSEI 21](https://www.dsei.co.uk/welcome) event. This is a completely dumb demonstration for the DSEI event. There is no real-life application for this tool and it is not demonstrative of any existing or intended capability. 

[FIXME] Please see the site how to https://defencedigital.github.io/dsei-demo/howto/ 

# Script / approach

The scenario here is one in which there is a team "on the ground" using a command and control (C2) tool to manage an on-going conflict/operation. The tool is relatively new, so there are a few bugs in place and optimisations that could be made. The demonstration shows how bugs and optimisations identified "on the ground" can be conveyed back to a development team, prioritised, implemented, and then made available back to the original team, in a reasonably quick time. 

There are several built-in steps here that demonstrate this. They must be demonstrated in the following order, and reset to number 1 at the end.

1. Basic build. This is the basic build of the tool with no improvements made. This is the starting point for the demo and the presenter should reset to this at the end of the demo.
2. Menu fix. There is a slightly annoying bug that exists, wherein the "Dashboard" item in the left-hand navigation shows as "active", even when you're looking at the "Live map view". This branch/fix changes this so that the page you have navigated to is the one that shows as "active".
3. Pin colours. This is a more useful change: the basic build shows all map pins as blue, irrespective of them being friendly or enemy. This change makes enemy pins red, making it easier to differentiate. 
4. Pin icons. A similar optimisation to the last, this makes it even easier to see what's going on, by changing the defaul pin icons to being item-specific (i.e. tanks have a tank icon, jets a jet icon, troops a people icon).

## Branches / changes

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

TODO

## Instigating a build

TODO
