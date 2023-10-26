#импорт нужных библиотек

import sqlite3
import pandas as pd

#подключение к бд
con = sqlite3.connect('C:/Users/User/Desktop/project_sql_Pavlova', timeout=10)
cur = con.cursor()

#подготовка таблицы с данными в формате pandas dataframe

df = pd.read_csv('C:/Users/User/Desktop/titanic.csv')

#проверка датасета
df.info()
#вся числовая информация (int, float) представлена в необходимых типах данных.


#поиск пропусков
print(df.isnull().mean() * 100)
#вся числовая информация (int, float) представлена полностью, пропуски отсутствуют.

#поиск дубликатов
doubles = df[df.duplicated()]
print(doubles)

# naming_convention
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('/', '_')
df.columns = df.columns.str.lower()

#загрузка таблицы в бд
df.to_sql(con=con, name='titanic_table', if_exists='replace', index=False)

#считывание данных из таблицы
data_test = cur.execute('select * from titanic_table')
con.commit()
cur.fetchall()
