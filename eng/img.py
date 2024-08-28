import os
from PIL import Image, ImageFilter

def blur_images_in_folder(folder_path, blur_radius):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return
    
    # Create an output folder if it doesn't exist
    output_folder = os.path.join(folder_path, "blurred_images")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the folder
    for filename in os.listdir(folder_path):
        # Skip non-image files
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            continue
        
        # Open the image
        image_path = os.path.join(folder_path, filename)
        with Image.open(image_path) as img:
            # Apply the blur filter
            blurred_img = img.filter(ImageFilter.GaussianBlur(blur_radius))
            
            # Save the blurred image to the output folder
            blurred_img.save(os.path.join(output_folder, filename))
            print(f"Blurred {filename} and saved to {output_folder}")

if __name__ == "__main__":
    # Define the folder path and blur radius
    folder_path = "/Users/olusegunzaccheaus/Documents/assign/WebAss/eng/img"
    blur_radius = 5  # Adjust this value to control the blur intensity

    # Blur all images in the folder
    blur_images_in_folder(folder_path, blur_radius)
