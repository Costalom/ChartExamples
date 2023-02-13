# Примеры построения графиков 

import tkinter as tk

# Импорт внешних файлов
import chart1 
import chart2

# Функция закрытия программы
def do_close():
    window.destroy()

# Создание главного окна
window = tk.Tk()
window.geometry("450x450")
window.title("Примеры построения графиков")

#  Добавление метки заголовка
lblTitle = tk.Label(text = "Примеры построения графиков", font = ('Tahoma', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=50, y=40)

# Добавление кнопки и метки для графика 1
btnChart1 = tk.Button(window, text="График 1 ", font = ('Tahoma', 11, 'bold'), command= chart1.plot_chart)
btnChart1.place(x=60, y=120, width=90, height=30)

lblChart1 = tk.Label (text = "График синуса matplotlib")
lblChart1.place(x=180, y=120)
 
# Добавление кнопки и метки для графика 2
btnChart2 = tk.Button(window, text="График 2 ", font = ('Tahoma', 11, 'bold'), command=chart2.plot_chart)
btnChart2.place(x=60, y=170, width=90, height=30)

lblChart2 = tk.Label (text = "Нормальное распределение")
lblChart2.place(x=180, y=170)

# Добавление кнопки закрытия программы 
btnClose = tk.Button(window, text="Закрыть", font = ('Tahoma', 11, 'bold'), command=do_close)
btnClose.place(x=330, y=400, width=90, height=30)

# Запуск цикла mainloop
window.mainloop()

