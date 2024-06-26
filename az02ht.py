import pandas as pd
#Создадим словарь  наборами данных 10 учеников с оценками по 5 предметам

data = { 'Олег': [3, 4, 5, 5, 5],
'Володя': [4, 4, 5, 3, 3],
'Лена': [3, 4, 5, 5, 3],
'Оксана': [3, 4, 5, 5, 4],
'Аня': [3, 4, 5, 5, 5],
'Дима': [3, 5, 5, 5, 3],
'Женя': [3, 4, 5, 5, 5],
'Света': [3, 3, 5, 5, 3],
'Коля': [3, 4, 4, 5, 4],
'Витя': [3, 4, 3, 5, 5]
}

#Создаём датафрейм:
df = pd.DataFrame(data)
print(df)

#Вычислим стандартное отклонение в данных наборах, чтобы увидеть,
# насколько сильно значения в наборе данных отличаются от среднего
# значения. Для этого используем функцию std. Для начала создадим
# переменные для наборов данных:
stdO = df["Олег"].std()
stdV = df['Володя'].std()
stdL = df['Лена'].std()
stdOk = df['Оксана'].std()
stdA = df['Аня'].std()
stdD = df['Дима'].std()
stdG = df['Женя'].std()
stdS = df['Света'].std()
stdK = df['Коля'].std()
stdVi = df['Витя'].std()

#Когда мы найдём отклонение в этих наборах, это сохранится в отдельные
# переменные.
#Чтобы посмотреть на результат, прописываем:
print(f"Стандартное отклонение 1 набор - {stdO}")
print(f"Стандартное отклонение 2 набор - {stdV}")
print(f"Стандартное отклонение 3 набор - {stdL}")
print(f"Стандартное отклонение 4 набор - {stdOk}")
print(f"Стандартное отклонение 5 набор - {stdA}")
print(f"Стандартное отклонение 6 набор - {stdD}")
print(f"Стандартное отклонение 7 набор - {stdG}")
print(f"Стандартное отклонение 8 набор - {stdS}")
print(f"Стандартное отклонение 9 набор - {stdK}")
print(f"Стандартное отклонение 10 набор - {stdVi}")

#Создадим тематический набор информации:

data = {'Возраст': [23, 22, 21, 27, 23, 20, 29, 28, 22, 25],
    'Зарплата': [54000, 58000, 60000, 52000, 55000, 59000, 51000, 49000, 53000, 61000]
}

#2. Создаём датафрейм:
df = pd.DataFrame(data)

#3. Посмотрим, как выглядит этот датафрейм, через функцию describe,
print(df.describe())

print(f"Средний возраст - {df['Возраст'].mean()}")

print(f"Медианный возраст - {df['Возраст'].median()}")

print(f"Стандартное отклонение возраста -{df['Возраст'].std()}")

print(f"Средняя зарплата - {df['Зарплата'].mean()}")

print(f"Медианная зп - {df['Зарплата'].median()}")

print(f"Стандартное отклонение зп - {df['Зарплата'].std()}")
