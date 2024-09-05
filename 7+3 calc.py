import tkinter as tk

#functions

#счетчик площади поверхности тела
def get_value_bsa():
    bodyheight = int(rost_entry.get())
    bodyweight = int(ves_entry.get())
    return bodyweight, bodyheight
def bsa_calc():
    body_height, body_weight = get_value_bsa()
    result_surface = round(0.007184 * (body_weight ** 0.425) * (body_height ** 0.725), 2)
    insert_bsa(result_surface)
def insert_bsa(result_surface):
    bsa_result.delete(0, 'end')
    bsa_result.insert(0, result_surface)

#калькулятор доз препаратов (АРА-С 200 мг на метр, даунорубицин 60 мг на метр)
def course_doses(resultr_surface):
    dose_ara_c = reslut_surface * 200
    dose_dauno = result_surface * 60
    return dose_ara_c, dose_dauno

#счетчики дней. Курс длится 7 дней: цитарабин каждый день. Даунорубицин 3 дня: дни 1-3 если ротации == нет, дни 5-7 если ротация == нет
def course_dates_ara_c(date_entry):
    n = 0
    dates_ara_c = []
    while n < 6:
        date_entry += n
        dates_ara_c.append(date_entry)
        n += 1
    return dates_ara_c

def course_dates_daunorybicin(date_entry):
    dates_dauno = []
    if str(rotation_entry.get().lower()) == 'нет':
        n = 0
        while n < 2:
            date_entry += n
            dates_dauno.apeend(dates_entry)
    elif str(rotation_entry.get().lower()) == 'да':
        date_5_day = date_entry + 5
        while n < 2:
            date_5_day += n
            dates_dauno.apeend(dates_entry)
            n += 1
    return dates_dauno


#window
window = tk.Tk()
window.title('7+3')
window.geometry('350x500')
window.resizable(False, False)

#instructions_intro
instruction1 = tk.Label(window, text = 'Ф.И.О. вводить словами, все остальное только числами!')
instruction1.place(x = 20, y  = 10)

#instructions_date
instruction2 = tk.Label(window, text = 'Формат даты: дд.мм.гггг. Время: чч:мм')
instruction2.place(x = 65, y  = 30)

#passport
name_entry = tk.Entry(window, width = 28)
name_entry.place(x = 100, y = 50)
name_surname = tk.Label(window, text = 'Ф.И.О:')
name_surname.place(x = 25, y = 50)

#rost
rost_entry = tk.Entry(window, width = 28)
rost_entry.place(x = 100, y = 75)
rost = tk.Label(window, text = 'Рост, см:')
rost.place(x = 25, y = 75)

#ves
ves_entry = tk.Entry(window, width = 28)
ves_entry.place(x =100, y = 100)
ves = tk.Label(window, text = 'Вес, кг:')
ves.place(x = 25, y = 100)

#data nachala
date_entry = tk.Entry(window, width = 20)
date_entry.place(x = 250, y = 125)
start_course = tk.Label(window, text = 'Дата начала курса:')
start_course.place(x = 25, y = 125)

#time nachala kyrsa
time_entry = tk.Entry(window, width = 28)
date_entry.place(x = 150, y = 150)
date_text = tk.Label(window, text = 'Время начала курса:')
date_text.place(x = 25, y = 150)

#rotazia antracyclinov
rotation_entry = tk.Entry(window, width = 9)
rotation_entry.place(x = 215, y = 175)
rotation_string = tk.Label(window, text = 'Ротация антрациклинов (да/нет)?')
rotation_string.place(x = 25, y = 175)

#BSA
#body_surface = tk.Label(window, text = 'BSA')
#body_surface.place(x = 25, y = 125)
#bsa_result = tk.Entry(window, width = 28)
#bsa_result.place(x = 100, y = 125)

#button_calc
button_calc = tk.Button(window, text = 'Расчитать', width = 15, height = 1, command = bsa_calc)
button_calc.place(x = 100, y = 200)

window.mainloop()