import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static

st.set_page_config(layout="wide")
st.title('Анализ преступлений в Алматы 🚔')

# Загрузка данных
@st.cache_data
def load_data():
    return pd.read_csv('data/almaty_crime_data.csv')

data = load_data()

# Сайдбар с фильтрами
st.sidebar.header("Фильтры")
selected_district = st.sidebar.multiselect('Район', options=data['district'].unique())
selected_crime = st.sidebar.multiselect('Тип преступления', options=data['crime_type'].unique())
viz_type = st.sidebar.radio("Тип визуализации", ["Тепловая карта", "Точки на карте"])

# Применение фильтров
filtered_data = data[
    (data['district'].isin(selected_district) if selected_district else True) &
    (data['crime_type'].isin(selected_crime) if selected_crime else True)
]

# Статистика
st.subheader("Основная статистика")
col1, col2, col3 = st.columns(3)
col1.metric("Всего преступлений", filtered_data.shape[0])
col2.metric("Самый частый тип", filtered_data['crime_type'].mode()[0])
col3.metric("Самый опасный район", filtered_data['district'].mode()[0])

# Карта
st.subheader('Карта преступлений')
m = folium.Map(location=[43.238949, 76.889709], zoom_start=11)

# Тепловая карта или точки
if viz_type == "Тепловая карта":
    heat_data = [[row['latitude'], row['longitude']] for _, row in filtered_data.iterrows()]
    HeatMap(heat_data, radius=15, blur=10).add_to(m)
else:
    for _, row in filtered_data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"Тип: {row['crime_type']}",
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)

folium_static(m, width=1200)

# Графики
st.subheader('Аналитика')
col1, col2 = st.columns(2)

with col1:
    fig1 = px.histogram(filtered_data, x='district', title='Распределение по районам')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.pie(filtered_data, names='crime_type', title='Доля типов преступлений')
    st.plotly_chart(fig2, use_container_width=True)
