import tkinter as tk

# Funktion, die das Fenster in der Mitte des Bildschirms positioniert
def center_window(root, width, height):

    # Bildschirmabmessungen abrufen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # X- und Y-Koordinaten berechnen, um das Fenster in der Mitte zu platzieren
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Fenstergröße und Position festlegen
    root.geometry(f"{width}x{height}+{x}+{y}")

# Hauptfenster erstellen
root = tk.Tk()
root.title("GUI")  # Titel des Fensters festlegen

window_width = 400  # Breite des Fensters
window_height = 300  # Höhe des Fensters

# Funktion aufrufen, um das Fenster in der Mitte zu positionieren
center_window(root, window_width, window_height)

# Hauptereignisschleife starten
root.mainloop()
