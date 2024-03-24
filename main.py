import os
from transliterate import translit

def find_folders(directory):
    folders = []
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            folders.append(os.path.join(root, dir))
            ru_text = dir
            text = translit(ru_text, language_code='ru', reversed=True)
            os.chdir(root)
            os.rename(dir, text)
            print(text)
    return folders, root

directory_path = 'D:\Test'
folders = find_folders(directory_path)
print("Found folders:")
for folder in folders:
    print(folder)

