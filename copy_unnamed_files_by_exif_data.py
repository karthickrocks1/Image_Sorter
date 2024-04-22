from get_date_taken_exifread import get_date_taken_exifread
from check_and_create_folder import check_and_create_folder
from copy_file import copy_file

def copy_unnamed_files_by_exif_data(image_path, image_name, destination_folder):
    
    """
    This function is used to copy the unnamed files from the source folder to destination folder.
    This file uses the exif data read from the image properties and puts in the respective folder of year and month.
    """
    
    date_taken = str(get_date_taken_exifread(image_path))
        
    try:
                
        if (len(date_taken[:4]) < 4) and (len(date_taken[4:6]) < 2):                                      #if the exif data has no date_time feature, this will filter
            new_path_for_OtherPhotos = check_and_create_folder(destination_folder, "OtherPhotos")         # Creating a new folder 'Other Photos'
            new_file_name = new_path_for_OtherPhotos +"/"+ image_name                                    # Creating file name with the path
            copy_file(image_path, new_file_name)                                                          # copying file to folder named 'Other folder'
                              
        else:
            year = int(date_taken[:4])          #coverting yyyy to integer for comparision
            if 1950 < year < 2099:              #checking year for cancelling unwanted numbers
                new_folder_path = check_and_create_folder(destination_folder, (date_taken[:4] + "/"+ date_taken[4:6]))       #new folder path with year and month
                new_folder_file_name = new_folder_path + "/" + image_name                                                   # creating path with filename
                copy_file(image_path, new_folder_file_name)                                                                  #copying file to respective folder
                    
            else:
                new_path_for_OtherPhotos = check_and_create_folder(destination_folder, "OtherPhotos")
                new_file_name = new_path_for_OtherPhotos +"/"+ image_name
                copy_file(image_path, new_file_name)
                    
    except ValueError:
        new_path_for_OtherPhotos = check_and_create_folder(destination_folder, "OtherPhotos")
        new_file_name = new_path_for_OtherPhotos +"/"+ image_name
        copy_file(image_path, new_file_name)
            