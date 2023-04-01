import numpy as np
import urllib.request
import imageio
from skimage.transform import resize as imresize

# Define the URLs file name
file_name = 'urls.txt'

# Define the video frame size and FPS
width, height = 1000*0.6, 710*0.6
fps = 30

# Create a VideoWriter object to save the video
writer = imageio.get_writer('output.mp4', fps=fps)

# Open the URLs file and iterate over the lines
with open(file_name) as f:
    for line in f:
        # Remove any leading/trailing whitespaces and line breaks
        url = line.strip()
        try:
            print("Processing", url)
            # Download the image from the URL
            with urllib.request.urlopen(url) as url_response:
                img_array = url_response.read()

            img = imageio.imread(img_array, format='GIF')
            img = imresize(img, (height, width), anti_aliasing=True)
            
            # Normalize the pixel values to the range of [0, 1]
            img = img / img.max()
            # Scale the pixel values to [0, 255] and convert to uint8 data type
            img_uint8 = (img * 255).astype(np.uint8)

            # Add the frame to the video
            writer.append_data(img_uint8)

        except:
            # If there is an error in downloading the image, skip it and continue with the next URL
            continue

# Release the VideoWriter object and destroy any remaining windows
writer.close()

print("Done")