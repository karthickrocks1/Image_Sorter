import os

def check_and_create_folder(destination_folder, year_or_month):
        
    """
    This function checks if a folder exists at the given path.
    If it doesn't exist, it creates the folder.

    Args:
      folder_path: The path to the folder to check and create (if necessary).
    """
    new_folder_path =""
    new_folder_path = destination_folder + year_or_month
    if not os.path.exists(new_folder_path):
        try:
            os.makedirs(new_folder_path)     
        except OSError as e:
            print(f"Error creating folder: {e}")

    return new_folder_path
