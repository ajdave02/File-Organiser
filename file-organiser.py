import os 
import tkinter as tk
import shutil
from tkinter import filedialog, messagebox


app = tk.Tk()
app.geometry("600x500")
app.title("File Organiser")
app.configure(bg="#1e1e1e")


selected_path ="" #stores the selected folder path globally

title = tk.Label(
    app,
    text="File Organiser",
    font=("Arial", 24, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=30)


File_types = {
    'images' : ['.jpg', '.png'],
    'videos' : ['.mp4', '.mov'],
    'documents' : ['.doc', '.pdf', '.txt'],
    'music' : ['.mp3', '.wav' ]
}
def choose_folder():
    global selected_path
    folder = filedialog.askdirectory() # Opens system folder picker
    if folder:
        selected_path = folder
        browse_btn.config(text="Folder Selected ✔️", fg="#ffffff") # button used to show thatt a folder has been selected

browse_btn = tk.Button (
    app,
    text="Browse",
    font=("Arial", 22),
    bg="#333",
    fg="white",
    relief="flat",
    command=choose_folder
)

browse_btn.pack(pady=5)



def organiser():
    if not selected_path:  # Ensures a folder has been selected
        messagebox.showwarning("Error", "Please browse and select a folder first!")
        return

    for filename in os.listdir(selected_path):     #loops through all files in selected directory
        file_path = os.path.join(selected_path, filename)

    #Only process files and ensures that folders are not selected
        if os.path.isfile(file_path): 
            file_extension = os.path.splitext(filename)[1].lower()
            for folder_name, ext_list in File_types.items():
                if file_extension in ext_list:
                    folder_path = os.path.join(selected_path, folder_name)
                    os.makedirs(folder_path, exist_ok=True)
                    #
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    break
    messagebox.showinfo("Success", "Files organised successfully!") #Notifies the user when done



organiser_btn = tk.Button(
    app,
    text="ORGANISE",
    font=("Arial", 20),
    width=15,
    height=2,
    relief="flat",
    command=organiser,
)
organiser_btn.pack(pady=20)


app.resizable (False, False)
app.mainloop()