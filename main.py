import tkinter as tk
from tkinter import messagebox
import os

#criar janela principal
root = tk.Tk()
root.title("lista de tarefas")
root.geometry("300x400")

#entrada de texto para nova tarefa
task_entry = tk.Entry(root, width=20)
task_entry.pack(pady=10)

#listbox para exibir tarefas
tasks_listbox = tk.Listbox(root, height=10, width=30)
tasks_listbox.pack(pady=10)

#carregar tarefas de um arquvio
def load_tasks():
  if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
      tasks = file.readlines()
      for task in tasks:
        tasks_listbox.insert(tk.END, task.strip())

#salvar tarefas em um arquivo
def save_tasks():
  with open("tasks.txt", "w") as file:  
    for task in tasks_listbox.get(0, tk.END):
      file.write(task + "\n")
      
#salvar tarefas em um capítulo
def save_tasks():
    tasks = tasks_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

#função para adicionar tarefa
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Aviso", "Por favor, insira uma tarefa.")

#botão adicionar tarefa
add_button = tk.Button(root, text="Adicionar tarefa", command=add_task)
add_button.pack(pady=5)

#funçao para excluir tarefa
def delete_task():
  try:
    selected_task_index = tasks_listbox.curselection()[0]
    tasks_listbox.delete(selected_task_index)
    save_tasks()
  except IndexError:  
    messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa.")

#botão remover tarefa
remove_button = tk.Button(root, text="remover tarefa", command = delete_task)
remove_button.pack(pady=5)

#carregar tarefas ao iniciar programa
load_tasks()

root.mainloop()