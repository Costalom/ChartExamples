# Примеры построения графиков 

import tkinter as tk

# Импорт внешних файлов
import chart1 
import chart2
import chart3

# Функция закрытия программы
def do_close():
    window.destroy()

# Создание главного окна
window = tk.Tk()
window.geometry("550x550")
window.title("Примеры построения графиков")

#  Добавление метки заголовка
lblTitle = tk.Label(text = "Примеры построения графиков", font = ('Tahoma', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=50, y=40)

# Добавление кнопки и метки для графика 1
btnChart1 = tk.Button(window, text="График 1 ", font = ('Tahoma', 11, 'bold'), command= chart1.plot_chart)
btnChart1.place(x=60, y=120, width=90, height=30)

lblChart1 = tk.Label (text = "График синуса matplotlib", font = ('Tahoma', 11, 'bold'))
lblChart1.place(x=180, y=120)
 
# Добавление кнопки и метки для графика 2
btnChart2 = tk.Button(window, text="График 2 ", font = ('Tahoma', 11, 'bold'), command=chart2.plot_chart)
btnChart2.place(x=60, y=159, width=90, height=30)

lblChart2 = tk.Label (text = "Нормальное распределение", font = ('Tahoma', 11, 'bold'))
lblChart2.place(x=180, y=159)

# Добавление кнопки и метки для графика 3
btnChart3 = tk.Button(window, text="График 3 ", font = ('Tahoma', 11, 'bold'), command=chart3.plot_chart)
btnChart3.place(x=60, y=198, width=90, height=30)

lblChart3 = tk.Label (text = "Заполнить между", font = ('Tahoma', 11, 'bold'))
lblChart3.place(x=180, y=198)

# Добавление кнопки и метки для графика 4
btnChart2 = tk.Button(window, text="График 4 ", font = ('Tahoma', 11, 'bold'), fg = '#CC0000' , command=chart2.plot_chart2)
btnChart2.place(x=60, y=237, width=90, height=30)

lblChart2 = tk.Label (text = "Нормальное распределение - 3 графика", font = ('Tahoma', 11, 'bold'), fg = '#CC0000')
lblChart2.place(x=180, y=237)

# Добавление кнопки и метки для графика 5
btnChart2 = tk.Button(window, text="График 5 ", font = ('Tahoma', 11, 'bold'), command=chart2.plot_chart)
btnChart2.place(x=60, y=276, width=90, height=30)

lblChart2 = tk.Label (text = "")
lblChart2.place(x=180, y=276)

# Добавление кнопки и метки для графика 6
btnChart2 = tk.Button(window, text="График 6 ", font = ('Tahoma', 11, 'bold'), command=chart2.plot_chart)
btnChart2.place(x=60, y=315, width=90, height=30)

lblChart2 = tk.Label (text = "")
lblChart2.place(x=180, y=315)

# Добавление кнопки и метки для графика 7
btnChart2 = tk.Button(window, text="График 7 ", font = ('Tahoma', 11, 'bold'), command=chart2.plot_chart)
btnChart2.place(x=60, y=354, width=90, height=30)

lblChart2 = tk.Label (text = "")
lblChart2.place(x=180, y=354)

# Добавление кнопки закрытия программы 
btnClose = tk.Button(window, text="Закрыть", font = ('Tahoma', 11, 'bold'), command=do_close)
btnClose.place(x=410, y=490, width=90, height=30)

# Запуск цикла mainloop
window.mainloop()

