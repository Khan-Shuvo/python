import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")

        self.expression = ""

        self.display = ttk.Entry(root, font=("Arial", 24), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(self.root, text=text, command= lambda t=text:self.on_button_click(t))
            button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

        clear_button = ttk.Button(self.root, text='C', command=self.clear)
        clear_button.grid(row=5, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

        # Configure the rows and columns to expand with window resizing
        for i in range(1, 5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i - 1, weight=1)
        self.root.grid_rowconfigure(5, weight=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
