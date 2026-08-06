import customtkinter as ctk
from customtkinter import filedialog
from PIL import Image

# Appearance settings: dark mode with a blue accent theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Image Viewer")
root.geometry("500x550")

# Placeholder label shown before any image is selected
image_label = ctk.CTkLabel(root, text="No image selected", width=350, height=350)
image_label.pack(pady=30)


def load_image():
    # Open the OS's native file picker, filtered to common image formats
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
    )
    if not file_path:
        return  # User closed the dialog without choosing a file

    # Load the image and convert it to a CustomTkinter-compatible format
    img = Image.open(file_path)
    ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(350, 350))

    # Replace the placeholder label with the actual image
    image_label.configure(image=ctk_img, text="")


select_button = ctk.CTkButton(root, text="Select Image", command=load_image)
select_button.pack(pady=10)

root.mainloop()
