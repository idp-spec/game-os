import tkinter as tk
from tkinter import messagebox
import subprocess

class CustomOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom OS Launcher")
        self.root.geometry("800x600")
        self.root.configure(bg="lightgrey")
        self.setup_taskbar()

    def setup_taskbar(self):
        taskbar = tk.Frame(self.root, bg="darkgrey", height=30)
        taskbar.pack(side="top", fill="x")

        start_button = tk.Button(taskbar, text="Launcher", command=self.show_launcher)
        start_button.pack(side="left", padx=10)

        time_label = tk.Label(taskbar, text="12:00 PM", bg="darkgrey", fg="white")
        time_label.pack(side="right", padx=10)

    def show_launcher(self):
        launcher = tk.Toplevel(self.root)
        launcher.title("Launcher")
        launcher.geometry("200x400")
        launcher.configure(bg="lightgrey")

        tk.Button(launcher, text="App Store", command=self.show_app_store).pack(pady=10)
        tk.Button(launcher, text="Game Store", command=self.show_game_store).pack(pady=10)
        tk.Button(launcher, text="Command", command=self.show_command).pack(pady=10)

    def show_app_store(self):
        messagebox.showinfo("App Store", "App Store coming soon!")

    def show_game_store(self):
        game_store = tk.Toplevel(self.root)
        game_store.title("Game Store")
        game_store.geometry("400x400")
        game_store.configure(bg="lightgrey")

        search_label = tk.Label(game_store, text="Search Game")
        search_label.pack(pady=5)

        search_entry = tk.Entry(game_store)
        search_entry.pack(pady=5)

        search_button = tk.Button(game_store, text="Search", command=lambda: self.search_game(search_entry.get()))
        search_button.pack(pady=10)

        self.results_frame = tk.Frame(game_store, bg="white")
        self.results_frame.pack(pady=10, fill="both", expand=True)

    def search_game(self, game_name):
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        game_info = {
            "title": "Sample Game",
            "description": "A fun and exciting game!",
            "image": "https://via.placeholder.com/150"
        }

        game_label = tk.Label(self.results_frame, text=game_info["title"], font=("Helvetica", 14))
        game_label.pack(pady=5)

        game_desc = tk.Label(self.results_frame, text=game_info["description"])
        game_desc.pack(pady=5)

        game_image = tk.Label(self.results_frame, text=f"Image URL: {game_info['image']}")
        game_image.pack(pady=5)

        download_button = tk.Button(self.results_frame, text="Download", command=lambda: self.download_game(game_name))
        download_button.pack(pady=10)

    def download_game(self, game_name):
        messagebox.showinfo("Download", f"Downloading {game_name}!")

    def show_command(self):
        command_window = tk.Toplevel(self.root)
        command_window.title("Command")
        command_window.geometry("400x200")
        command_window.configure(bg="lightgrey")

        command_label = tk.Label(command_window, text="Enter Command")
        command_label.pack(pady=5)

        command_entry = tk.Entry(command_window)
        command_entry.pack(pady=5)

        command_button = tk.Button(command_window, text="Execute", command=lambda: self.execute_command(command_entry.get()))
        command_button.pack(pady=10)

        self.command_output = tk.Text(command_window, height=6, width=50)
        self.command_output.pack(pady=10)

    def execute_command(self, command):
        if command == "install emulator":
            self.command_output.insert(tk.END, "Installing emulator...\n")
            # Simulate installation
            self.command_output.insert(tk.END, "Emulator installed.\n")
        elif command.startswith("get."):
            app_name = command.split(".")[1]
            self.command_output.insert(tk.END, f"Downloading and installing {app_name}...\n")
            # Simulate download and installation
            self.command_output.insert(tk.END, f"{app_name} installed.\n")
        else:
            self.command_output.insert(tk.END, "Unknown command.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomOS(root)
    root.mainloop()
