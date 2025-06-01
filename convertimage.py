import os
from PIL import Image, UnidentifiedImageError

# Use raw string to handle Windows backslashes correctly
input_folder = r"/home/yash/Downloads/NewImage"
output_folder = os.path.join(input_folder, "converted_images")
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    base_name, _ = os.path.splitext(filename)

    try:
        # Attempt to open any file as an image
        with Image.open(file_path) as img:
            img = img.convert("RGB")  # Remove alpha channel if needed

            # Save as WebP
            webp_path = os.path.join(output_folder, base_name + ".webp")
            img.save(webp_path, "WEBP", quality=85)
            print(f"✅ Converted to WebP: {webp_path}")

            # Save as AVIF
            avif_path = os.path.join(output_folder, base_name + ".avif")
            img.save(avif_path, "AVIF", quality=85)
            print(f"✅ Converted to AVIF: {avif_path}")

    except UnidentifiedImageError:
        print(f"❌ Skipped (not an image): {filename}")
    except Exception as e:
        print(f"❌ Error converting {filename}: {e}")
