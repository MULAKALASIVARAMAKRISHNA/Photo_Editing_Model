Load Image: Users can browse and upload an image using a file dialog; the app displays it in a resized form.

Display Image: The uploaded image is shown in the UI with aspect ratio maintained using PIL and ImageTk.

Apply Filters: Users can apply basic image filters like Blur, Contour, Sharpen, etc., which update the displayed image.

Reset Image: Resets the edited image back to the original uploaded version.

Add Tags & Description: Users can enter custom tags and descriptions for the image using input fields.

Save Image: Saves the edited image along with its tags and description (as a .txt file) to a user-specified folder.

Delete Image: Deletes the currently loaded image file and its associated metadata text file from the system.

Organize in Folders: Users can manually organize saved images into folders — the app works with the system file structure.

Simple GUI: The interface is built using tkinter with clearly labeled buttons for loading, saving, editing, and deleting.

No Database Required: All images and metadata are stored in the file system — no database or server setup needed.
