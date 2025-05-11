import os
import shutil

# You can change this to any folder you want
folder_path = input("Enter the full path of the folder to organize: ").strip()

if not os.path.isdir(folder_path):
    print("❌ This is not a valid folder path.")
    exit()

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Video": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "Others": []
}

def organize():
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    moved = True
                    break
            if not moved:
                target_folder = os.path.join(folder_path, "Others")
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))

organize()
print("✅ Files organized successfully!")
