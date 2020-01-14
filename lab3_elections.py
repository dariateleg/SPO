import matplotlib.pyplot as mpl_p
import numpy as np
import pandas as pd


def voters_percent_in_time(x, label):
    protocol = [10.00, 12.00, 15.00, 18.00]
    mpl_p.bar(protocol, x, width=1, color='green')
    mpl_p.title(label)
    for i in protocol:
        mpl_p.text(i - 0.8, x[protocol.index(i)] + 3.2, str(x[protocol.index(i)]) + '%')
    mpl_p.xlabel('Time')
    mpl_p.ylabel('Voters percent, %')
    mpl_p.xlim([0, 23])
    mpl_p.ylim([0, 100])
    mpl_p.yticks(np.arange(0, 101, 10))
    mpl_p.xticks(np.arange(0, 24, 1))
    mpl_p.show()


def least_sqr_method(x, y):  # y = ax + b, метод наименьших квадратов
    x = np.array(x).reshape(-1, 1)
    y = np.array(y).reshape(-1, 1)
    (x_min, x_max) = (min(x), max(x))
    (x2, xy) = (0, 0)
    ls = np.linspace(x_min, x_max)
    for i in range(0, len(x)):
        xy += x[i] * y[i]
    for i in range(0, len(x)):
        x2 += pow(x[i], 2)
    a = (len(x) * xy - np.sum(x) * np.sum(y)) / (len(x) * x2 - pow(np.sum(x), 2))
    b = (np.sum(y) - a * np.sum(x)) / len(x)
    return a, b, ls


def valid_voters_plot(x, y, label):
    mpl_p.scatter(x, y, linewidths=1, c="white", edgecolors='green')
    mpl_p.title(label)
    mpl_p.xlabel('Процент валидных бюллетеней')
    mpl_p.ylabel('Процент голосов')
    mpl_p.show()


def votes_dependencies(attendance, candidates):
    for candidate in candidates:
        a, b, ls = least_sqr_method(attendance, candidate['data'])
        mpl_p.plot(ls, a * ls + b, color=candidate['color'])
    for candidate in candidates:
        mpl_p.scatter(attendance, candidate['data'], color=candidate['color'], s=10, label=candidate['label'])
    mpl_p.title('Зависимость процента голосов за кандидатов от явки')
    mpl_p.xlabel('Процент явки по всем УИК, %')
    mpl_p.ylabel('Процент отданных голосов по всем УИК, %')
    mpl_p.legend()
    mpl_p.show()


def attendance_to_time_plot(attendance, per_time):
    mpl_p.scatter(per_time, attendance, linewidths=1, c="white", edgecolors='green')
    mpl_p.title("Зависимость явки от количества избирателей на участке")
    mpl_p.ylabel('Число явившихся')
    mpl_p.xlabel('Количество избирателей')
    mpl_p.show()


def attendance_to_uik_plot(attendance, uik):
    mpl_p.bar(uik, attendance, width=1, color='green')
    mpl_p.title("Явка к уикам")
    mpl_p.ylabel('Процент явившихся')
    mpl_p.xlabel('Уик')
    mpl_p.show()


def get_data(query):
    return pd.read_html(query, encoding='CP1251')  # читаем хтмл страницу в нужный формат пандас (датафрейм)


def main():
    page = get_data(
        'http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&type=454&vibid=27820001217420')
    summary_page = get_data(
        'http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217420&type=222')
    header = page[6].drop([0, 1, 2]).T.iloc[1].reset_index(drop=True)  # получаем список названий УИК
    per_time = page[6].drop([0, 1, 2]).T.drop([0, 1]).T.reset_index(
        drop=True)  # получаем кол-во избирателей для УИК и сколько их по времени в процентах
    per_time = np.array(per_time)
    summary = summary_page[7].drop([0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]).reset_index(
        drop=True)  # получаем 1,9,12,13,14 строки
    summary = np.array(summary)
    (attendance_array, valid_sheets) = ([], [])
    candidates_collection = [
        {'label': 'Беглов', 'color': 'red', 'data': summary[3]},
        {'label': 'Амосов', 'color': 'blue', 'data': summary[2]},
        {'label': 'Тихонова', 'color': 'green', 'data': summary[4]}
    ]
    for k in range(0, len(per_time)):
        for i in range(1, 5):
            per_time[k, i] = float(
                per_time[k, i].replace('%', ''))  # из процентов явки убираем процент и переводим из строки во флоат
    voters_percent_in_time(per_time[23, 1:], 'УИК №127 В.О.')  # строим график явки от времени для нашего УИКа
    for i in range(0, summary[1].size):
        valid_sheets.append(int(summary[1][i]) / int(
            summary[0][i]) * 100)  # переводим кол-во действительных бюллетеней из абсолютных чисел в относительныек
    for candidate in candidates_collection:
        for index, j in enumerate(candidate['data']):
            candidate['data'][index] = float(j.split(' ')[1].replace('%', ''))
        valid_voters_plot(valid_sheets, candidate['data'],
                          candidate['label'])  # строим график процент голосов/валидные бюллетени
    for i in range(0, len(per_time)):
        attendance_array.append(per_time[i, 4])  # складываем абсолютные числа явки в отдельный массив
    votes_dependencies(attendance_array,
                       candidates_collection)  # строим график отданные голоса/процент явки для всех участников на одном плоте
    per_time_total = []
    percent = []
    uik = []
    for i in range(0, len(attendance_array)):
        x = int(per_time[i][0])
        y = attendance_array[i]
        percent.append(y)
        result = x * y / 100  # считаем абсолютное число явившихся для каждого уик
        attendance_array[i] = result
        per_time_total.append(int(per_time[i][0]))  # количество избирателей в каждом уик
        uik.append(header[i].split(' №')[1])  # номер уик
    attendance_to_time_plot(attendance_array, per_time_total)  # строим график число явившихся/количество избирателей
    attendance_to_uik_plot(percent, uik)  # строим график процент явившихся/номер уик


main()
