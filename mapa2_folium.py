import json
import folium
import requests

#Importando dados estatístico
url = ("https://raw.githubusercontent.com/python-visualization/folium/master/examples/data")

#Separando os dados em variaveis
vis1 = json.loads(requests.get(f"{url}/vis1.json").text)
vis2 = json.loads(requests.get(f"{url}/vis2.json").text)
vis3 = json.loads(requests.get(f"{url}/vis3.json").text)


mapa = folium.Map(
    #latitude e longitude
    location=[-23.2797570, -45.8959299],
    tiles="OpenStreetMap",
    zoom_start=5
)

#Legenda do marcador
tooltip = "Nome do lugar!!"

#É possível alterar a cor do ícone e o tipo

folium.Marker(
    [-23.2797570, -45.8959299],
   #Atribuindo os dados estatisticos no marcador
    popup=folium.Popup(max_width=600).add_child(folium.Vega(vis1, width=600, height=300)
    ),
).add_to(mapa)


folium.Marker(
    [-23.2767570, -45.8959799],
    popup=folium.Popup(max_width=600).add_child(folium.Vega(vis2, width=600, height=300)
    ),
    icon=folium.Icon(color="green", icon_color="white", icon="info-sign")
).add_to(mapa)


folium.Marker(
    [-20.2767570, -40.8959799],
    popup=folium.Popup(max_width=600).add_child(folium.Vega(vis3, width=600, height=300)
    ),
    icon=folium.Icon(color="green", icon_color="white", icon="info-sign")
).add_to(mapa)

#Adiciona um marcador a cada clique
mapa.add_child(folium.ClickForMarker(popup="Waypoint"))



mapa.save("index.html")

