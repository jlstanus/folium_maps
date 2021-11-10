import os
import folium

m = folium.Map(location=[50.4739, 4.8587], tiles="Stamen Terrain", zoom_start=13)

folium.Marker([50.47433, 4.86478], popup="Hello World").add_to(m)

m.add_child(folium.ClickForMarker(popup="Waypoint"))

m.add_wms_layer(wms_name="LIDAX",
                wms_url="https://geoservices.wallonie.be/arcgis/services/EAU/ALEA_INOND/MapServer/WMSServer?request=GetCapabilities&service=WMS",
                wms_format="image/png",
                wms_layers='1')

m.save(os.path.join('html_maps', 'bomel.html'))