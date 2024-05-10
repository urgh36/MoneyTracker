import tkinter as tk
import pickle

transactions = []

def add_transaction():
    description = description_entry.get()
    amount = float(amount_entry.get())
    transaction_type = transaction_variable.get()

    if transaction_type == "Доход":
        transactions.append((description, amount))
    else:
        transactions.append((description, -amount))

    update_transaction_list()
    update_balance()
    clear_entries()
    save_data()

def update_transaction_list():
    transaction_list.delete(0, tk.END)
    for i, transaction in enumerate(transactions, start=1):
        transaction_list.insert(tk.END, f"{i}. {transaction[0]}: {transaction[1]}")

def update_balance():
    total_balance = sum(transaction[1] for transaction in transactions)
    balance_label.config(text=f"Общий баланс: {total_balance}", fg='blue')

def clear_entries():
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def delete_transaction():
    selected_transaction = transaction_list.curselection()
    if selected_transaction:
        index = selected_transaction[0]
        transactions.pop(index)
        update_transaction_list()
        update_balance()
        save_data()

def save_data():
    with open("transactions_data.pkl", "wb") as file:
        pickle.dump(transactions, file)

def load_data():
    global transactions
    try:
        with open("transactions_data.pkl", "rb") as file:
            transactions = pickle.load(file)
    except FileNotFoundError:
        transactions = []

root = tk.Tk()
root.title("Учет денежных транзакций")
root.configure(bg='#add8e6')  # устанавливаем светло-голубой цвет фона

load_data()

description_label = tk.Label(root, text="Описание:", fg='purple')
description_label.pack()

description_entry = tk.Entry(root)
description_entry.pack()

amount_label = tk.Label(root, text="Сумма:", fg='purple')
amount_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

transaction_variable = tk.StringVar()
transaction_variable.set("Доход")

transaction_type_label = tk.Label(root, text="Тип транзакции:", fg='purple')
transaction_type_label.pack()

transaction_type_menu = tk.OptionMenu(root, transaction_variable, "Доход", "Расход")
transaction_type_menu.pack()

add_button = tk.Button(root, text="Добавить транзакцию", bg='green', fg='white', command=add_transaction)
add_button.pack()

transaction_list = tk.Listbox(root, height=10)
transaction_list.pack()

delete_button = tk.Button(root, text="Удалить выбранную транзакцию", bg='red', fg='white', command=delete_transaction)
delete_button.pack()

balance_label = tk.Label(root, text="Общий баланс: 0.0", fg='blue')
balance_label.pack()

update_transaction_list()
update_balance()

root.mainloop()
