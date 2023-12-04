import psycopg2

try:
    conn = psycopg2.connect(
        dbname = "phone_book",
        user = "postgres",
        password = "12345678",
        host = "localhost"
    )
    if not conn.closed:
        print("Успешное подключение к базе данных PostgreSQL!")
        # Создание курсора для выполнения запросов
        cur = conn.cursor()

        # Выполнение запроса на извлечение данных из таблицы main
        cur.execute("""select u_id, fam.fam, nam.nam, otc.otc,
                       street.street, building, appartment, phone from main
                       join fam on main.fam = fam_id
                       join nam on main.nam = nam_id
                       join otc on main.otc = otc_id
                       join street on main.street = street_id""")

        # Получение результатов запроса
        rows = cur.fetchall()

        for row in rows:
            cleaned_row = [str(item).strip() for item in row]
            print(cleaned_row)

        # Вывод данных
        # for row in rows:
        #     print(row)

        # Закрытие курсора
        cur.close()
    else:
        print("Не удалось установить соединение с базой данных.")
except psycopg2.Error as e:
    print("Ошибка при подключении к базе данных PostgreSQL:", e)