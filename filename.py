import os

def replace_spaces_in_filenames(root_dir: str):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for name in filenames + dirnames:
            if ' ' in name:
                old_path = os.path.join(dirpath, name)
                new_name = name.replace(' ', '_')
                new_path = os.path.join(dirpath, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")

# Example usage:
if __name__ == "__main__":
    target_directory = "/media/yash/Development/WebProject/bankfinderproject/bankfindernexui/public/cardimages"
    replace_spaces_in_filenames(target_directory)
