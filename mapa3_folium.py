import json
import folium
import requests



url = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
)
antarctic_ice_edge = f"{url}/antarctic_ice_edge.json"
antarctic_ice_shelf_topo = f"{url}/antarctic_ice_shelf_topo.json"


mapa = folium.Map(
    #latitude e longitude
    location=[-59.1759, -11.6016],
    tiles="cartodbpositron",
    zoom_start=5
)

folium.GeoJson(antarctic_ice_edge, name="geojson").add_to(mapa)

folium.TopoJson(
    json.loads(requests.get(antarctic_ice_shelf_topo).text),
    "objects.antarctic_ice_shelf",
    name="topojson",
).add_to(mapa)

folium.LayerControl().add_to(mapa)

mapa.save("index.html")

