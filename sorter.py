import os
import shutil

folder_path = input("Введите путь к папке: ")
folder_path = folder_path.strip()

image_extensions = [".jpg",".jpeg",".png"]
video_extensions = [".mp4",".avi",".mov", ".mp4.mov", ".mov.mp4"]

#Создаем папки в папке с файлами( если их нет чтоб в них добалялись сортированные файлы)
images_folder = os.path.join(folder_path,"Images")
video_folder = os.path.join(folder_path,"Videos")

try:
    if not os.path.exists(images_folder):
        os.makedirs(images_folder)
    if not os.path.exists(video_folder):
        os.makedirs(video_folder)
except Exception as e:
    print(f"Ошибка при создании папки : {e}")

for item in os.listdir(folder_path):
    full_path = os.path.join(folder_path,item)
    if os.path.isfile(full_path):
        ext = os.path.splitext(full_path)[1].lower()
        if ext in image_extensions:
            dest_folder = images_folder
        elif ext in video_extensions:
            dest_folder = video_folder
        else:
            continue


        #Формируем путь для перемещения
        dest_path = os.path.join(dest_folder,item)

        #Если файл есть то добавить к имени 1
        if os.path.exists(dest_path):
            name,extn = os.path.splitext(item)
            dest_path = os.path.join(dest_folder,f"{name}1{extn}")

        #Перемещаем файл
        try:
            shutil.move(full_path,dest_path)
        except Exception as e:
            print(f" Не удалось переместить {item} в папке {e}")