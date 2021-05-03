#folium torna mais fácil visualizar dados que foram manipulados em Python em um mapa de
# folheto interativo. Ele permite a vinculação de dados a um mapa para

#A biblioteca possui vários tilesets integrados de OpenStreetMap, Mapbox e Stamen, e suporta tilesets
# personalizados com Mapbox ou Cloudmade API keys. foliumsuporta sobreposições de imagem, vídeo, GeoJSON e
# TopoJSON.
import folium


mapa = folium.Map(
    #latitude e longitude
    location=[-23.2797570, -45.8959299],
    #Tipos do mapa
    #OpenStreetMap
    #Stamen Terrain
    #Stamen Toner
    #Mapbox Bright
    #Mapbox Control Room
    tiles="OpenStreetMap",
    zoom_start=5
)

#É possível passar mapas personalizados
#mapa = folium.Map(
#    #latitude e longitude
#    location=[-23.2797570, -45.8959299],
     #Tipos do mapa
#    tiles='http://{s}.tiles.yourtiles.com/{z}/{x}/{y}.png',
#    attr='My Data Attribution'
#)


#Legenda do marcador
tooltip = "Nome do lugar!!"

#É possível alterar a cor do ícone e o tipo

folium.Marker(
    [-23.2797570, -45.8959299],
    popup="Camp Muir",
    tooltip=tooltip,
    icon=folium.Icon(color="blue", icon_color="white", icon="cloud")
).add_to(mapa)

folium.Marker(
    [-23.2767570, -45.8959799],
    popup="Camp Muir",
    tooltip=tooltip,
    icon=folium.Icon(color="green", icon_color="white", icon="info-sign")
).add_to(mapa)

folium.Circle(
    radius=100,
    location=[-21.2797570, -49.8959299],
    popup="The Warterfront",
    color="#3186cc",
    fill=False,
).add_to(mapa)

#Adiciona um marcador a cada clique
mapa.add_child(folium.ClickForMarker(popup="Waypoint"))

#Captura a latitude e longitude
mapa.add_child(folium.LatLngPopup())

mapa.save("index.html")

