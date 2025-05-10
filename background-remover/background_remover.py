import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from rembg import remove

def select_input_file():
    """
    Open a file dialog to select an input image.
    
    Returns:
        str: Path to the selected file or None if canceled
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    file_path = filedialog.askopenfilename(
        title="Select Image File",
        filetypes=[
            ("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff"),
            ("All files", "*.*")
        ]
    )
    
    return file_path if file_path else None

def select_output_file(default_filename):
    """
    Open a file dialog to select where to save the output image.
    
    Args:
        default_filename (str): Default filename to suggest
        
    Returns:
        str: Path for the output file or None if canceled
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    file_path = filedialog.asksaveasfilename(
        title="Save Processed Image As",
        defaultextension=".png",
        initialfile=os.path.basename(default_filename),
        filetypes=[
            ("PNG files", "*.png"),
            ("All files", "*.*")
        ]
    )
    
    return file_path if file_path else None

def remove_background(input_path, output_path=None):
    """
    Remove the background from an image.
    
    Args:
        input_path (str): Path to the input image
        output_path (str, optional): Path for the output image. If None, will use input filename with '_no_bg' suffix.
    
    Returns:
        str: Path to the processed image
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Create output path if not provided
    if output_path is None:
        file_name, file_ext = os.path.splitext(input_path)
        output_path = f"{file_name}_no_bg.png"
    
    # Open image
    input_image = Image.open(input_path)
    
    # Remove background
    output_image = remove(input_image)
    
    # Save result
    output_image.save(output_path)
    
    return output_path

def main():
    # Create a simple GUI
    root = tk.Tk()
    root.title("Background Remover")
    
    # Set window size and position
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    # Create and configure frame
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True, fill='both')
    
    # Add label
    label = tk.Label(frame, text="Click the button below to select an image and remove its background.")
    label.pack(pady=10)
    
    def process_image():
        # Select input file
        input_path = select_input_file()
        if not input_path:
            return  # User canceled
        
        # Select output file
        file_name, _ = os.path.splitext(input_path)
        default_output = f"{file_name}_no_bg.png"
        output_path = select_output_file(default_output)
        if not output_path:
            return  # User canceled
        
        try:
            # Process the image
            remove_background(input_path, output_path)
            messagebox.showinfo("Success", f"Background removed successfully!\nSaved to: {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    # Add button
    button = tk.Button(frame, text="Select Image & Remove Background", command=process_image)
    button.pack(pady=10)
    
    # Add exit button
    exit_button = tk.Button(frame, text="Exit", command=root.destroy)
    exit_button.pack(pady=5)
    
    # Start main loop
    root.mainloop()

if __name__ == "__main__":
    main()