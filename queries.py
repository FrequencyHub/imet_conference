def get_day(day):
    # Функция возвращает текст запроса, запрос вернет расписание докладов на конкретный день
    return f'''SELECT report, reporter, section, start_hour, start_minutes 
    FROM report WHERE day_of_conference = {day}'''

def get_reporers():
    # Функция возвращает текст запроса, запрос вернет всех докладчиков
    return 'SELECT reporer, scientific_degree FROM reporter'

def get_report_by_reporter(reporter):
    # Функция возвращает текст запроса, запрос вернет расписание докладов у докладчика
    return f'''SELECT report, section, day_of_conference, start_hour, start_minutes 
    FROM report WHERE reporter = "{reporter}"'''

def get_section(section):
    # Функция возвращает текст запроса, запрос вернет расписание докладов по секциям
    return f'''SELECT report, reporter, day_of_conference, start_hour, start_minutes 
    FROM report WHERE section = "{section}"'''

def insert_reporer(reporer, scientific_degree):
    return f'''INSERT INTO reporter (reporer, scientific_degree)
    VALUES ('{reporer}', '{scientific_degree}')'''

def delete_reporter(reporter):
    return f'''DELETE FROM reporter WHERE reporer = "{reporter}"'''

def insert_report(new_report, new_reporter, new_section, new_day_of_conference, new_hour, new_minutes):
    return f'''
    INSERT INTO report (report, reporter, section, day_of_conference, start_hour, start_minutes)
    VALUES ('{new_report}', '{new_reporter}', '{new_section}', '{new_day_of_conference}', '{new_hour}', '{new_minutes}')'''

def get_all_reports():
    return 'SELECT report FROM report'

def delete_report(report):
    return f'''DELETE FROM report WHERE report = "{report}"'''