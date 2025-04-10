import pandas as pd
from faker import Faker
import random

fake = Faker()
crime_types = ['Кража', 'ДТП', 'Грабеж', 'Мошенничество', 'Вандализм']
districts = ['Алатауский', 'Ауэзовский', 'Бостандыкский', 'Жетысуский', 'Медеуский', 'Наурызбайский']

data = {
    'date': [fake.date_between(start_date='-2y', end_date='today') for _ in range(1000)],
    'district': [random.choice(districts) for _ in range(1000)],
    'crime_type': [random.choice(crime_types) for _ in range(1000)],
    'latitude': [fake.latitude() for _ in range(1000)],  # Замените на реальные координаты
    'longitude': [fake.longitude() for _ in range(1000)]
}
df = pd.DataFrame(data)
df.to_csv('data/almaty_crime_data.csv', index=False)
