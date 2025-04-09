import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk, ImageFilter
import os
import shutil

class PhotoLibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Library Application")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f0f0")

        self.original_image = None
        self.image = None
        self.image_tk = None
        self.current_path = None

        self.create_widgets()

    def create_widgets(self):
        # Buttons
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Upload Photo", command=self.upload_image, bg="#007bff", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete Photo", command=self.delete_image, bg="#dc3545", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Reset", command=self.reset_image, bg="#ffc107").pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Save Edited", command=self.save_image, bg="#28a745", fg="white").pack(side=tk.LEFT, padx=5)

        # Directory Entry
        dir_frame = tk.Frame(self.root, bg="#f0f0f0")
        dir_frame.pack()
        tk.Label(dir_frame, text="Directory:", bg="#f0f0f0").pack(side=tk.LEFT)
        self.dir_entry = tk.Entry(dir_frame, width=40)
        self.dir_entry.pack(side=tk.LEFT, padx=5)

        # Description & Tags
        meta_frame = tk.Frame(self.root, bg="#f0f0f0")
        meta_frame.pack(pady=5)

        tk.Label(meta_frame, text="Description:", bg="#f0f0f0").pack(side=tk.LEFT)
        self.desc_entry = tk.Entry(meta_frame, width=30)
        self.desc_entry.pack(side=tk.LEFT, padx=5)

        tk.Label(meta_frame, text="Tags:", bg="#f0f0f0").pack(side=tk.LEFT)
        self.tags_entry = tk.Entry(meta_frame, width=30)
        self.tags_entry.pack(side=tk.LEFT, padx=5)

        # Filters
        filter_frame = tk.Frame(self.root, bg="#f0f0f0")
        filter_frame.pack(pady=5)

        filters = [
            ("BLUR", ImageFilter.BLUR),
            ("CONTOUR", ImageFilter.CONTOUR),
            ("DETAIL", ImageFilter.DETAIL),
            ("SHARPEN", ImageFilter.SHARPEN),
            ("EMBOSS", ImageFilter.EMBOSS),
        ]

        for name, f in filters:
            tk.Button(filter_frame, text=name, command=lambda f=f: self.apply_filter(f)).pack(side=tk.LEFT, padx=5)

        # Image Display
        self.image_label = tk.Label(self.root, bg="#ffffff")
        self.image_label.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if file_path:
            self.original_image = Image.open(file_path)
            self.image = self.original_image.copy()
            self.current_path = file_path
            self.display_image()

    def display_image(self):
        if self.image:
            aspect = self.image.width / self.image.height
            w = 600
            h = int(w / aspect)
            img_resized = self.image.resize((w, h), Image.LANCZOS)
            self.image_tk = ImageTk.PhotoImage(img_resized)
            self.image_label.config(image=self.image_tk)

    def apply_filter(self, filter_type):
        if self.image:
            self.image = self.image.filter(filter_type)
            self.display_image()

    def reset_image(self):
        if self.original_image:
            self.image = self.original_image.copy()
            self.display_image()

    def save_image(self):
        if self.image:
            save_dir = self.dir_entry.get().strip()
            desc = self.desc_entry.get().strip()
            tags = self.tags_entry.get().strip()

            if not save_dir:
                messagebox.showerror("Error", "Please enter a directory name.")
                return

            os.makedirs(save_dir, exist_ok=True)
            filename = os.path.basename(self.current_path)
            save_path = os.path.join(save_dir, filename)
            self.image.save(save_path)

            with open(os.path.join(save_dir, filename + ".meta.txt"), "w") as f:
                f.write(f"Description: {desc}\nTags: {tags}\n")

            messagebox.showinfo("Saved", f"Image saved to {save_path} with metadata.")

    def delete_image(self):
        if self.current_path and os.path.exists(self.current_path):
            try:
                os.remove(self.current_path)
                self.image_label.config(image='')
                messagebox.showinfo("Deleted", "Original image deleted successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete image: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoLibraryApp(root)
    root.mainloop()
