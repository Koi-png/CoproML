

#import JSON file
import json

# Specify the file path. Use just the filename if it's in the same directory.
file_path = 'C:/Users/asusr/Desktop/Projects/Parasitology ML/CoproML/Coprology ML/parasitoBank/parasitoBank/ParasitoBank.json' 



try:
    # Open the file in read mode ('r') using a context manager
    with open(file_path, 'r') as file:
        # Use json.load() to parse the file content into a Python object
        data = json.load(file)

    # You can now work with the data, which is likely a Python dictionary or list
    print("Data successfully loaded:")
    print(data)
    print(f"Type of data: {type(data)}")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from the file '{file_path}'. Check if the file is valid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


#Create cropped images
from PIL import Image

image_path = "C:/Users/asusr/Desktop/Projects/Parasitology ML/CoproML/Coprology ML/parasitoBank/parasitoBank/images"
annotations = data["annotations"]
images = data["images"]
output_path = "C:/Users/asusr/Desktop/Projects/Parasitology ML/CoproML/Coprology ML/Cropped Images"
arr_image = []
arr_image_index = []
#Create image array
for index,value in enumerate(images):
    image_join = [image_path, "/", images[index]["file_name"]]
    image = "".join(image_join)
    image_id = images[index]["id"]
    arr_image.append(image)
    arr_image_index.append(image_id)

#scan each image. for each image find the image indexes that match


