import os
import folium

m = folium.Map(location=[50.4739, 4.8587], tiles="Stamen Terrain", zoom_start=15)

folium.Marker([50.47433, 4.86478], popup="Hello World").add_to(m)

m.add_child(folium.ClickForMarker(popup="Waypoint"))


m.save(os.path.join('html_maps', 'bomel.html'))