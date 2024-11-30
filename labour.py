import os
from PIL import Image
import csv


def list_files_in_folder(folder_path):
    try:
        # Get the list of all files and directories in the specified folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        return files
    except FileNotFoundError:
        print(f"The folder '{folder_path}' does not exist.")
        return []
    except PermissionError:
        print(f"Permission denied to access the folder '{folder_path}'.")
        return []


input_folder = "/Users/nishchayaroy/Desktop/ML_final_sub/Dataset2/arc"
output_folder = "/Users/nishchayaroy/Desktop/ML_final_sub/Dataset2/arc_png"
csv_file_path = "/Users/nishchayaroy/Desktop/ML_final_sub/Dataset2/converted_files.csv"


files = list_files_in_folder(input_folder)

if files:
    print("Files in the folder:")
    for file in files:
        print(file)
else:
    print("No files found or an error occurred.")


def convert_jpg_to_png(input_folder, output_folder, csv_file_path):

    os.makedirs(output_folder, exist_ok=True)


    with open(csv_file_path, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        

        csv_writer.writerow(["filename", "class0", "class6"])
        

        for file_name in os.listdir(input_folder):
            if file_name.lower().endswith(".jpg") or file_name.lower().endswith(".jpeg"):
                input_path = os.path.join(input_folder, file_name)
                output_filename = os.path.splitext(file_name)[0] + ".png"
                output_path = os.path.join(output_folder, output_filename)

                with Image.open(input_path) as img:
                    img.save(output_path, "PNG")
                    print(f"Converted: {file_name} -> {output_filename}")

                
                csv_writer.writerow([output_filename, 0, 0])


convert_jpg_to_png(input_folder, output_folder, csv_file_path)
