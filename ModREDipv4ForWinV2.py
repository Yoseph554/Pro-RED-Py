import os
import tkinter as tk
from tkinter import messagebox

def apply_settings():
    selected_ip = listbox_ips.get(listbox_ips.curselection())
    ip, subnet, gateway, dns1, dns2 = ip_settings[selected_ip]

    # Construir los comandos para cambiar la configuración de red en macOS
    command_ip = f'sudo ifconfig en0 inet {ip} netmask {subnet}'
    command_gateway = f'sudo route add default {gateway}'
    command_dns = f'sudo networksetup -setdnsservers Wi-Fi {dns1} {dns2}'

    try:
        os.system(command_ip)
        os.system(command_gateway)
        os.system(command_dns)
        messagebox.showinfo("Éxito", "Configuración de red aplicada correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al aplicar la configuración de red: {e}")

# Configuraciones de IP predefinidas
ip_settings = {
    "Caja1": ("192.168.10.10", "255.255.255.0", "192.168.10.1", "8.8.8.8", "8.8.4.4"),
    "Credito1": ("192.168.20.10", "255.255.255.0", "192.168.20.1", "8.8.8.8", "8.8.4.4"),
    "RRHH1": ("192.168.30.10", "255.255.255.0", "192.168.30.1", "8.8.8.8", "8.8.4.4"),
    "Servidor1": ("192.168.40.10", "255.255.255.0", "192.168.40.1", "8.8.8.8", "8.8.4.4")
}

# Crear la ventana principal
root = tk.Tk()
root.title("Configuración de Red")

# Crear y colocar el Listbox para seleccionar la configuración de IP
tk.Label(root, text="Selecciona la configuración de IP").grid(row=0, column=0, padx=10, pady=5)
listbox_ips = tk.Listbox(root)
listbox_ips.grid(row=0, column=1, padx=10, pady=5)

# Añadir las opciones al Listbox
for key in ip_settings.keys():
    listbox_ips.insert(tk.END, key)

# Crear y colocar el botón de Aplicar
apply_button = tk.Button(root, text="Aplicar", command=apply_settings)
apply_button.grid(row=1, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()