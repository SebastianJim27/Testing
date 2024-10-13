import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.expression = ""

        self.text_input = tk.StringVar()
        self.result_display = tk.Entry(root, textvariable=self.text_input, font=('arial', 20, 'bold'), bd=30, insertwidth=4, width=14, borderwidth=4)
        self.result_display.grid(row=0, column=0, columnspan=4)

        # Definimos los botones
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.text_input.set("")
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.text_input.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Entrada inválida")
                self.expression = ""
        else:
            self.expression += str(char)
            self.text_input.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculadora(root)
    root.mainloop()
