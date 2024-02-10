import os
import shutil

def organize_files (source_dir):
# gets the list of files in the source directory
    files = os.listdir(source_dir)
    # creates directories for each file extension
    for file in files:
        if os. path.isfile (os.path.join(source_dir, file)):
            file_extension = os.path.splitext(file)[1]
            if file_extension:
                # Creates directory if it does not exist
                if not os. path.exists (os.path.join(source_dir, file_extension [1:])):
                    os.makedirs(os.path.join(source_dir, file_extension[1:]))
                #Moves file to corresponding directory
                shutil.move(
                os.path.join(source_dir, file),
                os.path.join(source_dir, file_extension [1:], file)
                )
if __name__ == "__main__":
    source_directory = input("Enter the path of the directory to organize: ")
    # Checks if the specified directory exists
    if os. path.exists(source_directory) and os. path.isdir (source_directory):
        organize_files (source_directory)
        print("File organization completed.")
    else:
        print("Invalid directory path. Please provide a valid directory.")