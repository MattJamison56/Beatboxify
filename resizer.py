from PIL import Image
import os

def resize_and_center_image(input_path, output_path, target_size=(1280, 720)):
    # Open the original image
    with Image.open(input_path) as img:
        img = img.convert("RGBA")  # Ensure image has an alpha channel for transparency
        original_width, original_height = img.size
        target_width, target_height = target_size

        # Calculate the new size keeping the aspect ratio
        if original_height > original_width:
            # If the image is taller than wide, resize based on height
            new_height = target_height
            new_width = int((new_height / original_height) * original_width)
        else:
            # Otherwise, resize based on width
            new_width = target_width
            new_height = int((new_width / original_width) * original_height)

        # Resize the image while maintaining the aspect ratio
        img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Create a new image with the target size and a transparent background
        new_image = Image.new("RGBA", target_size, (0, 0, 0, 0))

        # Calculate position to paste the resized image on the canvas
        x_offset = (target_width - new_width) // 2
        y_offset = (target_height - new_height) // 2

        # Paste the resized image onto the center of the new image
        new_image.paste(img_resized, (x_offset, y_offset), img_resized)

        # Save the new image
        new_image.save(output_path, "PNG")

def process_images_in_folder(folder_path, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for index, filename in enumerate(sorted(os.listdir(folder_path))):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, f"{index}.png")
            resize_and_center_image(input_path, output_path)

if __name__ == "__main__":
    input_folder = "images"
    output_folder = "resized_images"
    process_images_in_folder(input_folder, output_folder)