import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static

st.title('Анализ преступлений в Алматы 🚔')
data = pd.read_csv('data/almaty_crime_data.csv')

# Фильтры
selected_district = st.sidebar.multiselect('Район', options=data['district'].unique())
selected_crime = st.sidebar.multiselect('Тип преступления', options=data['crime_type'].unique())

# Применение фильтров
filtered_data = data[
    (data['district'].isin(selected_district) if selected_district else True) &
    (data['crime_type'].isin(selected_crime) if selected_crime else True)
]

# Карта
st.subheader('Карта преступлений')
m = folium.Map(location=[43.238949, 76.889709], zoom_start=11)
for _, row in filtered_data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['crime_type']
    ).add_to(m)
folium_static(m)

# Графики
st.subheader('Распределение по типам преступлений')
fig = px.pie(filtered_data, names='crime_type')
st.plotly_chart(fig)
