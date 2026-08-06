import customtkinter as ctk
from customtkinter import filedialog
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Image Viewer")
root.geometry("500x550")

image_label = ctk.CTkLabel(root, text="No image selected", width=350, height=350)
image_label.pack(pady=30)


def load_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
    )
    if not file_path:
        return

    img = Image.open(file_path)
    ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(350, 350))
    image_label.configure(image=ctk_img, text="")


select_button = ctk.CTkButton(root, text="Select Image", command=load_image)
select_button.pack(pady=10)

root.mainloop()
