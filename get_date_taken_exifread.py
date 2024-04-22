import exifread

def get_date_taken_exifread(image_path):
  """
  This function attempts to retrieve the date taken from the Exif data
  of an image using the exifread library.
  
  This function is used only when the filename doesn't provide the date of picture.
  This function uses to shift all the pictures to respective year.

  Args:
      image_path: The path to the image file.

  Returns:
      A string representing the date taken (e.g., "2024:01:01") or None
      if the date information is not found.
  """
  try:
    with open(image_path, 'rb') as f:
      tags = exifread.process_file(f)
      #print(tags)
      if 'Image DateTime' in tags:
        date_taken_full_string = tags['Image DateTime'].values[:11]                #First 10 digits gets the YYYY:MM:DD from the datetime tag
        date_taken_YYYYMMDD = date_taken_full_string.replace(":","")               # Removing the semicolon and making the datetime to YYYYMMDD
        return str(date_taken_YYYYMMDD)
    
  except (IOError, OSError) as e:
    print(f"Error opening or reading image: {e}")
  return None
