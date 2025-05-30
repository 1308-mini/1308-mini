import tkinter as tk
from tkinter import ttk, messagebox

class SimpleGUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Tkinter App")
        self.root.geometry("400x300")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title label
        title_label = ttk.Label(main_frame, text="Welcome to Tkinter!", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Name input
        ttk.Label(main_frame, text="Enter your name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_var = tk.StringVar()
        name_entry = ttk.Entry(main_frame, textvariable=self.name_var, width=20)
        name_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        greet_button = ttk.Button(button_frame, text="Greet", command=self.greet_user)
        greet_button.pack(side=tk.LEFT, padx=(0, 10))
        
        clear_button = ttk.Button(button_frame, text="Clear", command=self.clear_fields)
        clear_button.pack(side=tk.LEFT)
        
        # Text area for output
        ttk.Label(main_frame, text="Output:").grid(row=3, column=0, sticky=(tk.W, tk.N), pady=(10, 5))
        
        self.output_text = tk.Text(main_frame, height=8, width=40)
        self.output_text.grid(row=3, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0), padx=(10, 0))
        
        # Scrollbar for text area
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.output_text.yview)
        scrollbar.grid(row=3, column=2, sticky=(tk.N, tk.S), pady=(10, 0))
        self.output_text.configure(yscrollcommand=scrollbar.set)
        
        # Configure grid weights for resizing
        main_frame.rowconfigure(3, weight=1)
    
    def greet_user(self):
        name = self.name_var.get().strip()
        if name:
            greeting = f"Hello, {name}! Welcome to the tkinter app.\n"
            self.output_text.insert(tk.END, greeting)
            self.output_text.see(tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter your name first!")
    
    def clear_fields(self):
        self.name_var.set("")
        self.output_text.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    app = SimpleGUIApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
