import os

# Specify the folder path
folder_path = "/Users/nishchayaroy/Desktop/ML_final_sub/oath_v1.1/images/cropped_scaled_rotated"

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file name matches the pattern
    if "_" in filename and filename.endswith(".png"):
        # Split the filename at the underscore and take the first part
        new_name = filename.split("_")[0] + ".png"
        
        # Get the full path of the file
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {filename} -> {new_name}")
