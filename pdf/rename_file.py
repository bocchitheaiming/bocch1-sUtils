import os

dir = "Code\data"
ls = os.listdir(dir)

for file in ls:
    # Check if the file doesn't end with .csv
    if not file.endswith('.csv'):
        # Get the file path
        old_path = os.path.join(dir, file)
        # Create new filename with .csv extension
        new_filename = os.path.splitext(file)[0] + '.csv'
        new_path = os.path.join(dir, new_filename)
        # Rename the file
        os.rename(old_path, new_path)

