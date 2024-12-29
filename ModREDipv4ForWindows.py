import os
import tkinter as tk
from tkinter import messagebox

def apply_settings():
    ip = entry_ip.get()
    subnet = entry_subnet.get()
    gateway = entry_gateway.get()
    dns1 = entry_dns1.get()
    dns2 = entry_dns2.get()

    # Construir el comando netsh para cambiar la configuración de IP
    command_ip = f'netsh interface ip set address name="Ethernet" static {ip} {subnet} {gateway}'
    command_dns = f'netsh interface ip set dns name="Ethernet" static {dns1} primary'
    command_dns2 = f'netsh interface ip add dns name="Ethernet" {dns2} index=2'

    try:
        os.system(command_ip)
        os.system(command_dns)
        os.system(command_dns2)
        messagebox.showinfo("Éxito", "Configuración de red aplicada correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al aplicar la configuración de red: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Configuración de Red")

# Crear y colocar las etiquetas y campos de entrada para cada campo
tk.Label(root, text="Dirección IP").grid(row=0, column=0, padx=10, pady=5)
entry_ip = tk.Entry(root)
entry_ip.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Máscara de Subred").grid(row=1, column=0, padx=10, pady=5)
entry_subnet = tk.Entry(root)
entry_subnet.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Puerta de Enlace Predeterminada").grid(row=2, column=0, padx=10, pady=5)
entry_gateway = tk.Entry(root)
entry_gateway.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Servidor DNS Preferido").grid(row=3, column=0, padx=10, pady=5)
entry_dns1 = tk.Entry(root)
entry_dns1.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Servidor DNS Alternativo").grid(row=4, column=0, padx=10, pady=5)
entry_dns2 = tk.Entry(root)
entry_dns2.grid(row=4, column=1, padx=10, pady=5)

# Crear y colocar el botón de Aplicar
apply_button = tk.Button(root, text="Aplicar", command=apply_settings)
apply_button.grid(row=5, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()