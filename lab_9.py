import rawpy 
from PIL import Image 
import os 
import matplotlib.pyplot as plt 
def convert_arw_to_jpg(arw_path, jpg_path, quality=85): 
    with rawpy.imread(arw_path) as raw: 

        # Convert the raw image to RGB 
        rgb = raw.postprocess() 
 
        # Save the RGB image as a JPEG 
        img = Image.fromarray(rgb) 
        img.save(jpg_path, 'JPEG', quality=quality, optimize=True) 
 
def plot_images(original_path, compressed_path): 
    # Plot the original .ARW image 
    plt.subplot(1, 2, 1) 
    plt.imshow(rawpy.imread(original_path).postprocess()) 
    plt.title('Original Image (.ARW)') 
 
    # Plot the compressed .JPG image 
    plt.subplot(1, 2, 2) 
    plt.imshow(Image.open(compressed_path)) 
    plt.title('Compressed Image (.JPG)') 
 
    # Show the plot 
    plt.show() 
 
def get_file_size(file_path): 
    # Get the file size in bytes 
    return os.path.getsize(file_path) 
 
def main(): 
    # Input and output file paths 
    input_arw_path = '/Users/monusiddiki/Desktop/arw.arw' 
    output_jpg_path = '/Users/monusiddiki/Desktop/New_arw.jpg' 
 
    # Set the compression quality (0-100, higher is better quality) 
    compression_quality = 85 
 
    # Convert .ARW to .JPG 
    convert_arw_to_jpg(input_arw_path, output_jpg_path, quality=compression_quality) 
 
    # Get file sizes 
    original_size = get_file_size(input_arw_path) 
    compressed_size = get_file_size(output_jpg_path) 
 
    # Display file sizes 
    print(f'Original Image Size (.ARW): {original_size} bytes') 
    print(f'Compressed Image Size (.JPG): {compressed_size} bytes') 
 
    # Plot the images 
    plot_images(input_arw_path, output_jpg_path) 
 
if __name__ == "__main__": 
    main()

