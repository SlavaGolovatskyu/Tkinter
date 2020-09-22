import tkinter
from tkinter import *
from tkinter import messagebox

on = False
width = 380
height = 420

class Window:
	def __init__(self, width, height, title = 'MyApp', resizable = (True, True)):
		self.root = Tk()
		self.root.title(title)
		self.root['bg'] = '#ccc'
		self.root.geometry(f"{width}x{height}+200+200")
		self.root.resizable(resizable[0], resizable[1])

		self.label = Label(self.root, text = 'Ваш путь в км : ', bg = '#09d96a') # bg = background
		self.km = Entry(self.root, font = 'Consolas 15', fg = '#eff5c9', bg = '#48494f', relief = 'solid', justify = 'center')
		self.label2 = Label(self.root, text = 'Укажите цену на бензин (руб) : ', bg = '#09d96a') # bg = background
		self.price = Entry(self.root, font = 'Consolas 15', fg = '#eff5c9', bg = '#48494f', relief = 'solid', justify = 'center')
		self.label3 = Label(self.root, text = 'Разход бензина на 100 км : ', bg = '#09d96a')
		self.ganz = Entry(self.root, font = 'Consolas 15', fg = '#eff5c9', bg = '#48494f', relief = 'solid', justify = 'center')
		self.label4 = Label(self.root, text = 'Результат : ', bg = '#09d96a')
		self.result = Entry(self.root, font = 'Consolas 15', fg = '#eff5c9', bg = '#48494f', relief = 'solid', justify = 'center', width = '40')
		self.enterbut = Button(text = 'Рассчитать', font = 'Consolas 13', fg = '#eff5c9', bg = '#48494f', relief = 'solid', activebackground = '#6e6f73', activeforeground = '#eff5c9', width = '20')
		self.enterbut.bind('<Button-1>', self.check)

	def result_program(self):
		try:
			klm     = float(self.kms)
			pruce   = float(self.pric)
			benz    = float(self.gan)
			result = (benz * pruce / 100) * (klm * 2)
			self.result.delete(0, 100000000)
			self.result.insert(0, '{0:.2f}'.format(result) + ' руб в обе стороны.')
		except ValueError:
			messagebox.showerror('Error 1x2', 'Вы указали вместо цифр буквы в поле для ввода.')

	def check(self, event):
		self.kms   = self.km.get()
		self.pric  = self.price.get()
		self.gan   = self.ganz.get()

		if self.kms and self.pric and self.gan:
			self.result_program()

		if not self.kms and self.pric and self.gan:
			messagebox.showerror('Error 0x1', 'Вы не указали путь в км.')

		elif not self.pric and self.kms and self.gan:
			messagebox.showerror('Error 0x2', 'Вы не указали цену за 1л бензина.')

		elif not self.gan and self.pric and self.kms:
			messagebox.showerror('Error 0x3', 'Вы не указали разход бензина на 100 км.')

		if not self.kms and not self.pric and not self.gan:
			messagebox.showerror('Error 1x1', 'Вы не указали данные.')

	def run(self):
		self.draw_window()
		self.root.mainloop()

	def draw_window(self):   # padx pady можно изменять отступы лейбла
		self.label.pack(padx = 5, pady = 5) # Тут можна задати параметр anchor = center і тд скрін в папці ткінтер тобто в цій ПИСАТИ БЕЗ СКОБОК
		self.km.pack(padx = 1, pady = 1)	# Параметр в цій команді яка прорисовує лейбл потрібна для положення лейбла. Тобто в краю чи центрі і т.д
		self.label2.pack(padx = 10, pady = 10)
		self.price.pack(padx = 5, pady = 5)
		self.label3.pack(padx = 15, pady = 15)
		self.ganz.pack(padx = 10, pady = 10)
		self.label4.pack(padx = 15, pady = 15)
		self.result.pack(padx = 10, pady = 10)
		self.enterbut.pack(padx = 20, pady = 20)


if __name__ == '__main__':
	window = Window(width, height)
	window.run()


#iconbitmap задает приложению иконку.
