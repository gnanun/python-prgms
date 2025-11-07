import os  

def rename_files_in_directory(directory, old_extension, new_extension):
    if not os.path.exists(directory):
        print("Error: Directory not found!")
        return

    files = os.listdir(directory)
    count = 0

    for filename in files:
        if filename.endswith(old_extension):
            base = os.path.splitext(filename)[0]
            new_filename = base + new_extension
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed: {filename} → {new_filename}")
            count += 1

    if count == 0:
        print(f"\nNo files found with '{old_extension}' extension.")
    else:
        print(f"\nAll {count} file(s) renamed successfully!")

if __name__ == "__main__":
    dir_path = input("Enter the directory path: ").strip()
    old_ext = input("Enter the old file extension (e.g., .txt): ").strip()
    new_ext = input("Enter the new file extension (e.g., .md): ").strip()
    rename_files_in_directory(dir_path, old_ext, new_ext)

