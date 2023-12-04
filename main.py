import tkinter as tk
import psycopg2

def insert_data(entry_fam=None, entry_nam=None, entry_otc=None, entry_street=None, entry_building=None,
                entry_apartment=None, entry_phone=None):
    # Получаем данные из полей ввода
    fam_value = entry_fam
    nam_value = entry_nam
    otc_value = entry_otc
    street_value = entry_street
    building_value = entry_building
    apartment_value = entry_apartment
    phone_value = entry_phone

    # Подключение к базе данных
    # conn = psycopg2.connect(
    #     dbname="имя_вашей_бд",
    #     user="ваш_пользователь",
    #     password="ваш_пароль",
    #     host="localhost"
    # )

    # Создание курсора для выполнения SQL-запросов
    # cur = conn.cursor()

    # Пример добавления записи в таблицу
    query = """
        INSERT INTO main (fam, nam, otc, street, building, apartment, phone)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data = (fam_value, nam_value, otc_value, street_value, building_value, apartment_value, phone_value)

    # cur.execute(query, data)
    # conn.commit()

    # Закрытие курсора и соединения
    # cur.close()
    # conn.close()
    return query

def create_window():
    window = tk.Tk()
    window.title("Пример клиентского приложения")

    # Функциональные поля для ввода данных
    label_fam = tk.Label(window, text="Фамилия:")
    label_fam.pack()
    entry_fam = tk.Entry(window)
    entry_fam.pack()

    label_nam = tk.Label(window, text="Имя:")
    label_nam.pack()
    entry_nam = tk.Entry(window)
    entry_nam.pack()

    label_otc = tk.Label(window, text="Отчество:")
    label_otc.pack()
    entry_otc = tk.Entry(window)
    entry_otc.pack()

    label_street = tk.Label(window, text="Улица:")
    label_street.pack()
    entry_street = tk.Entry(window)
    entry_street.pack()

    label_building = tk.Label(window, text="Здание:")
    label_building.pack()
    entry_building = tk.Entry(window)
    entry_building.pack()

    label_apartment = tk.Label(window, text="Квартира:")
    label_apartment.pack()
    entry_apartment = tk.Entry(window)
    entry_apartment.pack()

    label_phone = tk.Label(window, text="Телефон:")
    label_phone.pack()
    entry_phone = tk.Entry(window)
    entry_phone.pack()

    # Кнопка для добавления данных в БД
    button_insert = tk.Button(window, text="Добавить данные",
                              command=insert_data(entry_fam.get(), entry_nam.get(), entry_otc.get(),
                                                  entry_street.get(), entry_building.get(),
                                                  entry_apartment.get(), entry_phone.get()))
    button_insert.pack()

    button_update = tk.Button(window, text="Изменить")#, command=update_data)
    button_update.pack()

    button_delete = tk.Button(window, text="Удалить")#, command=delete_data)
    button_delete.pack()

    button_show = tk.Button(window, text="Показать")#, command=show_data)
    button_show.pack()

    window.mainloop()

create_window()

