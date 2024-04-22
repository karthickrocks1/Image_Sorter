import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import askdirectory


from check_and_create_folder import check_and_create_folder
from get_filenames import get_filenames
from copy_file import copy_file
from copy_unnamed_files_by_exif_data import copy_unnamed_files_by_exif_data

 
def image_main_cycle (folder_path, destination_path):

    #folder_path = askdirectory(title='Select Source folder') # shows dialog box and return the path
    filenames, file_count= get_filenames(folder_path)
    destination_folder= destination_path + "/"

    
    n=0
    
    # Print the filenames (optional)
    for filename in filenames:

        n += 1    # for seeing whether all files are covered.
        if len(filename[1][:4]) < 4:
            copy_unnamed_files_by_exif_data(filename[0], filename[2], destination_folder)  #If there is no year data in filename, then go for exif
            continue
        elif len(filename[1][4:6]) < 2:
            copy_unnamed_files_by_exif_data(filename[0], filename[2], destination_folder)  #If there is no month data in filename, then go for exif
            continue
        else:
            #print(filename[0], filename[1][:4])
            year = int(filename[1][:4])                                #convert string of YYYY in to int
            if 2005 < year < 2099:
                check_and_create_folder(destination_folder, filename[1][:4])        # create year folder
                month = int(filename[1][4:6])                                       # get month from string
                if month < 13:
                    new_folder_path = check_and_create_folder(destination_folder, (filename[1][:4] + "/" +filename[1][4:6]))    #month folder
                    new_folder_file_name = new_folder_path + "/" + filename[2]        #destination name with path, for next step
                    copy_file(filename[0], new_folder_file_name)                      # copying from src to destination
                    
                else:                
                    copy_unnamed_files_by_exif_data(filename[0], filename[2], destination_folder)         #anything wrong, go to exif data
                    
            else:
                copy_unnamed_files_by_exif_data(filename[0], filename[2], destination_folder)             #anything wrong, go to exif data
        
        percent_progress = int(n/file_count*100)      
        label_status.config(text=f"Total {n} files copied and arranged out of {file_count} files ({percent_progress}%)")
        progress_bar.config(value=percent_progress)
        root.update()
        print(f"Total {n} files copied and arranged out of {file_count} files")
        
    print (f"Job Complete. {n} files are copied and arranged")
    return n



source_folder_path=[]
destination_folder_path=[]
percent_progress=0

def browse_directory_1():
  """
  Opens a file dialog to choose a source directory and updates the label for directory 1.
  """
  directory = filedialog.askdirectory()
  if directory:
    label_directory_1.config(text=f"{directory}")
    source_folder_path.append(directory)
    filenames, file_count= get_filenames(directory)
    label_status.config(text=f"   Total {file_count} files found in the Source Folder")

def browse_directory_2():
  """
  Opens a file dialog to choose a destination directory and updates the label for directory 2.
  """
  directory = filedialog.askdirectory()
  if directory:
    label_directory_2.config(text=f"{directory}")
    destination_folder_path.append(directory)


def coordinate_function():
    
    try:
        n = image_main_cycle(source_folder_path[0], destination_folder_path[0])
        label_status.config(text=f"Job Completed! Total {n} files copied and arranged")
    except:
        label_status.config(text="Select the Source and Destination folders")
        



# Create the main window
root = tk.Tk()
root.title("Sort images in to a new Folder")
root.geometry("782x440")
root.minsize(782, 440)
root.maxsize(782, 440)

# Create text for the description of the application

text_app_desc = tk.Text(root, wrap='word', height = 11, width = 95, bg='sky blue', fg= 'black')

app_desc = """This app sorts your large volumes of photos and videos into Year and Monthwise Folders.

Step 1: Choose the Source folder of your photos and videos.

Step 2: Choose the Destination Folder where you want to arrange the copied photos in Year and month wise.

Step 3: Click Copy and Sort button.

Files without any time taken data will be moved to a folder named 'Other Photos'"""

text_app_desc.insert(tk.END, app_desc)
text_app_desc.place(x=10, y=10)

# Create buttons for browsing directories
button_directory_1 = tk.Button(root, text="Browse Source Folder", command=browse_directory_1, bd =2 , relief = 'ridge' , bg='sky blue', fg='black')
button_directory_1.place(x=10, y=220)

# Create labels for displaying chosen directories
label_directory_1 = tk.Label(root, text="Source Folder:")
label_directory_1.place(x=200, y=220)

button_directory_2 = tk.Button(root, text="Browse Destination Folder", command=browse_directory_2, bd =2 , relief = 'ridge' , bg='sky blue', fg='black')
button_directory_2.place(x=10, y=270)

label_directory_2 = tk.Label(root, text="Destination Folder:")
label_directory_2.place(x=200, y=270)


button_copy = tk.Button(root, text="Copy and Sort", command=coordinate_function, bd =2 , relief = 'ridge' , bg='sky blue', fg='black')
button_copy.place(x=350, y=320)

label_status = tk.Label(root, text="")
label_status.place(x=150, y=360)

progress_bar = ttk.Progressbar(root, value = percent_progress, length=500)
progress_bar.place(x=150, y=400)


# Start the main event loop
root.mainloop()
