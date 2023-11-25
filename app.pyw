import tkinter as tk
import random
import string

def generate_passwords():
    try:
        size = int(size_entry.get())
        quantity = int(quantity_entry.get())
    except ValueError:
        result_text.config(state="normal")
        result_text.delete(1.0, "end")
        result_text.insert("end", "Tamanho e quantidade devem ser números válidos.")
        result_text.config(state="disabled")
        return

    passwords = []

    for _ in range(quantity):
        password = ''.join(random.choice(password_chars) for _ in range(size))
        passwords.append(password)

    result_text.config(state="normal")
    result_text.delete(1.0, "end")

    # Display passwords in a tabular format
    result_text.insert("end", "Senhas Geradas:\n")
    for i, password in enumerate(passwords, start=1):
        result_text.insert("end", f"Senha {i}: {password}\n") 

    result_text.config(state="disabled")



# Inicialização
dark_mode = False
password_chars = string.ascii_letters + string.digits + string.punctuation

root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry('400x400')

root.configure(bg='white')

# Tema escuro
def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

def apply_theme():
    if dark_mode:
        root.configure(bg='black')
        label.configure(bg='black', fg='white')
        button.configure(bg='gray', fg='black')
        toggle_button.configure(bg='gray', fg='black')
        result_text.configure(bg='black', fg='white')
    else:
        root.configure(bg='white')
        label.configure(bg='white', fg='black')
        button.configure(bg='lightgray', fg='black')
        toggle_button.configure(bg='lightgray', fg='black')
        result_text.configure(bg='white', fg='black')

label = tk.Label(root, text="GERADOR DE SENHA", font=("Arial", 14))
label.pack(pady=20)

tk.Label(root, text="Quantidade de senhas").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Label(root, text="Tamanho da senha").pack()
size_entry = tk.Entry(root)
size_entry.pack()


button = tk.Button(root, text="Gerar Senha(s)", command=generate_passwords)
button.pack()

result_text = tk.Text(root, wrap="none")
result_text.config(state="disabled")
result_text.pack(fill="both", expand=True)

# Barra de rolagem
scrollbar = tk.Scrollbar(result_text)
scrollbar.pack(side="right", fill="y")
scrollbar.config(command=result_text.yview)
result_text.config(yscrollcommand=scrollbar.set)

toggle_button = tk.Button(root, text="Modo Escuro", font=("Arial", 7), command=toggle_dark_mode)
toggle_button.place(x=1, y=1)

apply_theme()

# Iniciar o loop de eventos da GUI
root.mainloop()


print ("""\033[1m  Lorem Ipsum \033[0m is simply dummy text of the printing and typesetting industry.
   Has as been the industry's standard dummy text ever since the 1500s""")