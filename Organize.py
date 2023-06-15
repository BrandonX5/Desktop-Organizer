import os
import shutil

desktop_path = os.path.expanduser("~/Desktop")  # Ścieżka do pulpitu

# Tworzenie folderów docelowych, jeśli nie istnieją
folders = {
    "PDF": os.path.join(desktop_path, "PDF"),
    "JPG": os.path.join(desktop_path, "Zdjęcia"),
    "PNG": os.path.join(desktop_path, "Zdjęcia"),
    "JPEG": os.path.join(desktop_path, "Zdjęcia"),
    "TXT": os.path.join(desktop_path, "TXT"),
    "DOC": os.path.join(desktop_path, "DOC"),
    "DOCX": os.path.join(desktop_path, "DOC"),
    "RTF": os.path.join(desktop_path, "DOC"),
}

for folder_path in folders.values():
    os.makedirs(folder_path, exist_ok=True)

# Przechodzenie przez pliki na pulpicie
for filename in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, filename)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1][1:].upper()  # Rozszerzenie pliku

        if file_extension in folders:
            destination_folder = folders[file_extension]
            new_file_path = os.path.join(destination_folder, filename)
            

            # Przenoszenie pliku do odpowiedniego folderu
            shutil.move(file_path, new_file_path)
            print(f"Przeniesiono plik {filename} do {destination_folder}.")
        else:
            print(f"Nieznane rozszerzenie pliku: {filename}")
            
#print(folders["JPG"])
input("Naciśnij Enter, aby zakończyć...")
