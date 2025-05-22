import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        # Entry field for display
        self.display = ttk.Entry(root, justify="right", font=('Arial', 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # Calculator buttons
        self.create_buttons()
        
        # Configure grid
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
            
        self.current = ""
        
    def create_buttons(self):
        button_layout = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]
        
        for (text, row, col) in button_layout:
            button = ttk.Button(self.root, text=text, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            
    def button_click(self, value):
        if value == '=':
            try:
                result = eval(self.current)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.current = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.current = ""
        elif value == 'C':
            self.display.delete(0, tk.END)
            self.current = ""
        else:
            self.current += value
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current)

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
