import os
import yaml
from datetime import datetime

def convert_header(old_header_str):
    old_header = yaml.safe_load(old_header_str)
    
    if 'date' not in old_header:
        print("Missing 'date' field in header. Skipping file.")
        return None, None  # Returning None to indicate that this file should be skipped

    pub_datetime = datetime.strptime(old_header['date'], '%Y-%m-%d').isoformat() + 'Z'
    new_header = {
        'author': 'Richard Kastl',
        'pubDatetime': pub_datetime,
        'title': old_header.get('title', 'Untitled'),
        'slug': old_header.get('slug', '').replace('/', '').replace(' ', '-').lower(),
        'featured': False,
        'tags': old_header.get('tags', []),
        'description': old_header.get('description', ''),
    }
    return yaml.dump(new_header, sort_keys=False, allow_unicode=True), pub_datetime

def process_markdown_files(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.md'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                parts = content.split('---', 2)
                if len(parts) < 3:
                    print(f"Skipping {file_name}, does not contain a valid header.")
                    continue
                old_header_str = parts[1]
                new_header_str, pub_datetime = convert_header(old_header_str)
                if new_header_str is None:  # Check if conversion was successful
                    print(f"Skipping {file_name} due to missing or incorrect header fields.")
                    continue
                new_content = '---\n' + new_header_str + '---\n' + parts[2]
                
                # Constructing new file name
                date_str = datetime.strptime(pub_datetime, "%Y-%m-%dT%H:%M:%SZ").strftime("%m-%d-%Y")
                new_file_name = f"{date_str}-{file_name}"
                new_file_path = os.path.join(folder_path, new_file_name)
                
                # Write the new content to the renamed file
                with open(new_file_path, 'w', encoding='utf-8') as new_file:
                    new_file.write(new_content)
                
                # Optionally delete the old file if you want to only keep the renamed ones
                # os.remove(file_path)

                print(f"Processed and renamed {file_name} to {new_file_name}")

# Example usage, replace 'your_folder_path' with the actual path
folder_path = './src/content/blog/'
process_markdown_files(folder_path)
