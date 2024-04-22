import shutil

def copy_file(source_file, destination_file):
  """
  This function copies a file from the source location to the destination.

  Args:
      source_file: The path to the source file (including filename).
      destination_file: The path to the destination file (including filename).
  """
  try:
    shutil.copy(source_file, destination_file)
    print(f"File copied successfully: {source_file} -> {destination_file}")
  except Exception as e:
    print(f"Error copying file: {e}")
    