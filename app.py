from flask import Flask, render_template
# import folium

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='home')
    # start_coords = (46.9540700, 142.7360300)
    # folium_map = folium.Map(location=start_coords, zoom_start=14)
    # folium_map.save('templates/map.html')
    # return render_template('index.html')

@app.route('/map-view/')
def mapview():
    return render_template('map-view.html', name='map-view')

@app.route('/map/')
def map():
    return render_template('map.html', name='map')


if __name__ == '__main__':
    app.run(debug=True)