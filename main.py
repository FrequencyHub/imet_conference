import sqlite3
import streamlit as st
import pandas as pd
import queries

if 'run_button' in st.session_state and st.session_state.run_button == True:
    st.session_state.running = True
else:
    st.session_state.running = False

if 'run_report' in st.session_state and st.session_state.run_report == True:
    st.session_state.report = True
else:
    st.session_state.report = False

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')

# Определяем страницы
page = st.sidebar.radio("Выбрать страницу", ["Главная", 'Докладчики', 'Секции', 'Управление расписанием'])

st.title('Первая свободная научная конференция ИПМЭиТ')

if page == "Главная":
    # Определяем поведение приложение на главной странице
    st.header('Главная')

    # 1 день
    st.write('1 день - 29 февраля 2025')
    df = pd.read_sql_query(queries.get_day(1), connection)
    df.rename(columns={
        'report': 'Доклад',
        'reporter': 'Докладчик',
        'section': 'Секция'
    }, inplace=True)
    df['Время начала'] = df['start_hour'].astype(str) + ':' + df['start_minutes'].astype(str).str.zfill(2)
    df.drop(columns=['start_hour', 'start_minutes'], inplace=True)
    df = df.sort_values(by='Время начала')
    df.reset_index(drop=True, inplace=True)
    st.table(df)

    # 2 день
    st.write('2 день - 30 февраля 2025')
    df = pd.read_sql_query(queries.get_day(2), connection)
    df.rename(columns={
        'report': 'Доклад',
        'reporter': 'Докладчик',
        'section': 'Секция'
    }, inplace=True)
    df['Время начала'] = df['start_hour'].astype(str) + ':' + df['start_minutes'].astype(str).str.zfill(2)
    df.drop(columns=['start_hour', 'start_minutes'], inplace=True)
    df = df.sort_values(by='Время начала')
    df.reset_index(drop=True, inplace=True)
    st.table(df)

    # 3 день
    st.write('3 день - 31 февраля 2025')
    df = pd.read_sql_query(queries.get_day(3), connection)
    df.rename(columns={
        'report': 'Доклад',
        'reporter': 'Докладчик',
        'section': 'Секция'
    }, inplace=True)
    df['Время начала'] = df['start_hour'].astype(str) + ':' + df['start_minutes'].astype(str).str.zfill(2)
    df.drop(columns=['start_hour', 'start_minutes'], inplace=True)
    df = df.sort_values(by='Время начала')
    df.reset_index(drop=True, inplace=True)
    st.table(df)

elif page == 'Докладчики':
    # Определяем поведение приложение на странице докладчиков
    st.header('Докладчики')

    reporters = pd.read_sql_query(queries.get_reporers(), connection)
    for id, reporter in reporters.iterrows():
        st.write(reporter[1], reporter[0])

        reports = pd.read_sql_query(queries.get_report_by_reporter(str(reporter[0])), connection)
        reports.rename(columns={
            'report': 'Доклад',
            'section': 'Секция',
            'day_of_conference': 'День конференции'
        }, inplace=True)
        reports['Время начала'] = reports['start_hour'].astype(str) + ':' + reports['start_minutes'].astype(str).str.zfill(2)
        reports.drop(columns=['start_hour', 'start_minutes'], inplace=True)
        reports = reports.sort_values(['День конференции', 'Время начала'])
        reports.reset_index(drop=True, inplace=True)
        st.table(reports)

elif page == 'Секции':
    # Определяем поведение приложение на странице секций
    st.header('Секции')

    # 1 секция
    st.write('Информатика для бизнеса')
    df = pd.read_sql_query(queries.get_section('Информатика для бизнеса'), connection)
    df.rename(columns={
        'report': 'Доклад',
        'reporter': 'Докладчик',
        'day_of_conference': 'День конференции'
    }, inplace=True)
    df['Время начала'] = df['start_hour'].astype(str) + ':' + df['start_minutes'].astype(str).str.zfill(2)
    df.drop(columns=['start_hour', 'start_minutes'], inplace=True)
    df = df.sort_values(['День конференции', 'Время начала'])
    df.reset_index(drop=True, inplace=True)
    st.table(df)

    # 2 секция
    st.write('Экономика России')
    df = pd.read_sql_query(queries.get_section('Экономика России'), connection)
    df.rename(columns={
        'report': 'Доклад',
        'reporter': 'Докладчик',
        'day_of_conference': 'День конференции'
    }, inplace=True)
    df['Время начала'] = df['start_hour'].astype(str) + ':' + df['start_minutes'].astype(str).str.zfill(2)
    df.drop(columns=['start_hour', 'start_minutes'], inplace=True)
    df = df.sort_values(['День конференции', 'Время начала'])
    df.reset_index(drop=True, inplace=True)
    st.table(df)

    # 3 секция
    st.write('Искусственный интеллект')
    df = pd.read_sql_query(queries.get_section('Искусственный интеллект'), connection)
    df.rename(columns={
        'report': 'Доклад',
        'reporter': 'Докладчик',
        'day_of_conference': 'День конференции'
    }, inplace=True)
    df['Время начала'] = df['start_hour'].astype(str) + ':' + df['start_minutes'].astype(str).str.zfill(2)
    df.drop(columns=['start_hour', 'start_minutes'], inplace=True)
    df = df.sort_values(['День конференции', 'Время начала'])
    df.reset_index(drop=True, inplace=True)
    st.table(df)

else:
    st.header('Управление расписанием')

    # Добавление докладчика
    st.write('Добавление докладчика')
    new_reporter_fio = st.text_input('Фамилия И.О.')
    new_reporter_sd = st.text_input('Учёная степень')

    reporters = pd.read_sql_query(queries.get_reporers(), connection)
    reporters_fio = []
    for id, reporter in reporters.iterrows():
        reporters_fio.append(reporter[0])
    button_do = st.button('Добавить участника')
    if button_do and new_reporter_fio and new_reporter_sd:
        if new_reporter_fio in reporters_fio:
            st.write("Такой докладчик уже есть!")
        else:
            cursor = connection.cursor()
            cursor.execute(queries.insert_reporer(new_reporter_fio, new_reporter_sd))
            connection.commit()
            st.write('Участник добавлен!')
    elif button_do:
        st.write('Добавьте данные')

    st.write('')
    st.write('')
    st.write('')

    # Удаление докладчика
    st.write('Удаление докладчика')

    deleting_reporter = st.selectbox('Выберите участника', reporters_fio)

    button_do = st.button('Удалить участника', disabled=st.session_state.running, key='run_button')
    if button_do:
        connection.execute("PRAGMA foreign_keys = ON;")
        cursor = connection.cursor()
        cursor.execute(queries.delete_reporter(deleting_reporter))
        connection.commit()
        st.write('Участник удален!')

    st.write('')
    st.write('')
    st.write('')

    # Добавление доклада
    st.write('Добавление доклада')
    new_report = st.text_input('Название доклада')

    new_reporter = st.selectbox('Выберите докладчика', reporters_fio)

    new_section = st.selectbox('Выберите секцию', ['Информатика для бизнеса', 'Экономика России', 'Искусственный интеллект'])
    new_day_of_conference = st.selectbox('Выберите день конференции', [1, 2, 3])
    new_time = st.time_input("Выберите время", value=None, step=1800)
    button_do = st.button('Добавить доклад')

    reports = pd.read_sql_query(queries.get_all_reports(), connection)
    all_reports = []
    for id, report in reports.iterrows():
        all_reports.append(report[0])

    if button_do and new_report and new_reporter and new_section and new_day_of_conference and new_time:
        if new_report in all_reports:
            st.write('Такой доклад уже есть!')
        else:
            new_hour = new_time.hour
            new_minutes = new_time.minute
            cursor = connection.cursor()
            cursor.execute(queries.insert_report(new_report, new_reporter, new_section, new_day_of_conference, new_hour, new_minutes))
            connection.commit()
            st.write('Доклад добавлен!')
    elif button_do:
        st.write('Добавьте данные')

    st.write('')
    st.write('')
    st.write('')

    # Удаление доклада
    st.write('Удаление доклада')

    deleting_report = st.selectbox('Выберите удаляемый доклад', all_reports)

    button_do = st.button('Удалить доклад', disabled=st.session_state.report, key='run_report')
    if button_do:
        connection.execute("PRAGMA foreign_keys = ON;")
        cursor = connection.cursor()
        cursor.execute(queries.delete_report(deleting_report))
        connection.commit()
        st.write('Доклад удален!')


# Закрываем соединение
connection.close()