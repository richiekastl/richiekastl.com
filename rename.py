import os
import re

def rename_files(folder_path):
    # Compile a regular expression pattern to match the old file names and extract parts
    pattern = re.compile(r'(\d{2})-(\d{2})-(\d{4})-(.*)\.md$')
    
    for file_name in os.listdir(folder_path):
        match = pattern.match(file_name)
        if match:
            # Extract parts of the old file name
            month, day, year, rest_of_name = match.groups()
            # Construct the new file name by keeping the original year
            new_file_name = f"{year}-{month}-{day}-{rest_of_name}.md"
            # Full paths for the old and new file names
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, new_file_name)
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{file_name}' to '{new_file_name}'")
            
# Example usage, replace 'your_folder_path' with the actual path to your directory
folder_path = './src/content/blog/'
rename_files(folder_path)
