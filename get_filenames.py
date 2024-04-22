import os
from find_first_numbers import find_first_numbers

def get_filenames(folder):
    
    """
      This function walks through a directory and its subdirectories,
      returning a list of filenames and a count of the files found.

      Args:
          folder: The path to the directory to start searching from.

      Returns:
          A tuple containing:
              - filenames: A list containing 3 items [filename_with_its_path, date_extract_in_YYYYMMDD, filename].
              - file_count: The total number of files found.
              
    """
    
    filenames = []
    file_count = 0
    
    for root, _, files in os.walk(folder):
        for filename in files:
                        
            #match = re.findall(r'\d+', filename)
            #file_taken_date = match[0]
            photo_date = find_first_numbers(filename)
            filenames.append([os.path.join(root, filename), photo_date, filename])
            file_count += 1              
                        
    return filenames, file_count
