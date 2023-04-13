import os
import requests
from PIL import Image
from io import BytesIO

# Create a directory to save the downloaded images
output_dir = "nekos_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

thumbnail_dir = "nekos_thumbnails"
if not os.path.exists(thumbnail_dir):
    os.makedirs(thumbnail_dir)

thumbnail_width = 200

# Iterate through the 4-digit numbers between 0001 and 0913
for i in range(1, 914):
    # Format the number with leading zeros
    number = f"{i:04d}"
    
    # Build the URL
    url = f"https://nekos.best/api/v2/neko/{number}.png"
    
    # Download the image
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Downloading image {number}...")

        # Open the image using the PIL library
        img = Image.open(BytesIO(response.content))
        
        # Save the original image
        img.save(f"{output_dir}/{number}.png")
        
        # Calculate the new height while maintaining the aspect ratio
        aspect_ratio = img.height / img.width
        thumbnail_height = int(thumbnail_width * aspect_ratio)
        
        # Create the thumbnail
        thumbnail = img.resize((thumbnail_width, thumbnail_height), Image.ANTIALIAS)
        
        # Save the thumbnail
        thumbnail.save(f"{thumbnail_dir}/{number}-thumbnail.png")
    else:
        print(f"Error downloading image {number}: {response.status_code}")

print("Download and thumbnail generation complete.")
