# Координаты центров районов Алматы
district_coords = {
    'Алатауский': (43.2237, 76.8295),
    'Ауэзовский': (43.2504, 76.9453),
    'Бостандыкский': (43.2345, 76.9117),
    'Жетысуский': (43.3167, 77.0167),
    'Медеуский': (43.1678, 76.8836),
    'Наурызбайский': (43.2913, 76.9784)
}

# Генерация данных с привязкой к районам
data = {
    'date': [fake.date_between(start_date='-2y', end_date='today') for _ in range(1000)],
    'district': [random.choice(districts) for _ in range(1000)],
    'crime_type': [random.choice(crime_types) for _ in range(1000)],
    'latitude': [district_coords[row['district']][0] + random.uniform(-0.01, 0.01) for _, row in df.iterrows()],
    'longitude': [district_coords[row['district']][1] + random.uniform(-0.01, 0.01) for _, row in df.iterrows()]
}
