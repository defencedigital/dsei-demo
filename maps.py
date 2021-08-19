import folium

location = [51.502124, -0.117457] # London
m = folium.Map(location=location, zoom_start=14)
# m = folium.Map(location=location, tiles='Mapbox Bright', zoom_start=13)

tooltip = "Click for info!"

# Downing Street
folium.Marker(
    [51.503200, -0.126910], 
    popup='<strong>Friendly tank</strong><br />Type: Challenger 2', 
    tooltip=tooltip
).add_to(m)

# King Charles Street
folium.Marker(
    [51.502220, -0.127520], 
    popup='<strong>Friendly tank</strong><br />Type: Challenger 2', 
    tooltip=tooltip
).add_to(m)

# Parliament Street
folium.Marker(
    [51.501720, -0.126150], 
    popup='<strong>Friendly tank</strong><br />Type: Challenger 2', 
    tooltip=tooltip
).add_to(m)

# Westminster Bridge
folium.Marker(
    [51.500958, -0.124205], 
    popup='<strong>Friendly jet</strong><br />Type: Typhoon FGR4', 
    tooltip=tooltip
).add_to(m)

# Embankment station
folium.Marker(
    [51.506698, -0.122803], 
    popup='<strong>Friendly jet</strong><br />Type: Typhoon FGR4', 
    tooltip=tooltip
).add_to(m)

# St James' Park
folium.Marker(
    [51.503250, -0.133400], 
    popup='<strong>Friendly troops</strong><br />Type: Light infantry', 
    tooltip=tooltip
).add_to(m)

# Parliament Square
folium.Marker(
    [51.500627, -0.126840], 
    popup='<strong>Friendly troops</strong><br />Type: Light infantry', 
    tooltip=tooltip
).add_to(m)

# Westminster Bridge East
folium.Marker(
    [51.500785, -0.118805], 
    popup='<strong>Enemy tank</strong><br />Type: T-14 Armata', 
    tooltip=tooltip
).add_to(m)

# Waterloo Station Car Park
folium.Marker(
    [51.502349, -0.116394], 
    popup='<strong>Enemy tank</strong><br />Type: T-14 Armata', 
    tooltip=tooltip
).add_to(m)

# St Thomas' Hospital
folium.Marker(
    [51.498493, -0.117331], 
    popup='<strong>Enemy tank</strong><br />Type: T-14 Armata', 
    tooltip=tooltip
).add_to(m)

# Imperial War Museum
folium.Marker(
    [51.496663, -0.108802], 
    popup='<strong>Enemy jet</strong><br />Type: Sukhoi Su-57', 
    tooltip=tooltip
).add_to(m)

# Southwark Station
folium.Marker(
    [51.503625, -0.105697], 
    popup='<strong>Enemy jet</strong><br />Type: Sukhoi Su-57', 
    tooltip=tooltip
).add_to(m)

# Lambeth Bridge
folium.Marker(
    [51.494361, -0.121365], 
    popup='<strong>Enemy troops</strong><br />Type: Light infantry', 
    tooltip=tooltip
).add_to(m)

# Elephant and Castle
folium.Marker(
    [51.495117, -0.100385], 
    popup='<strong>Enemy troops</strong><br />Type: Light infantry', 
    tooltip=tooltip
).add_to(m)

m.save('templates/map.html')


# Custom markers (tank, etc.)