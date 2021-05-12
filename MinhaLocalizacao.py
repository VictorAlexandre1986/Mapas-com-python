import requests
import folium

resposta = requests.get('https://ipinfo.io/')

dados = resposta.json()

localizacao = dados['loc'].split(',')

latitude = float(localizacao[1])
longitude = float(localizacao[0])



fg = folium.FeatureGroup("Mapa")

fg.add_child(folium.GeoJson(data=(open('geojs-SaoPaulo.json','r',encoding='utf-8-sig').read())))

fg.add_child(folium.Marker(location=[longitude,latitude], popup='Estou aqui'))

mapa = folium.Map(localizacao=[latitude,longitude], zoom_start=7)

mapa.add_child(fg)
mapa.save('Localizacao.html')

