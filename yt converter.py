import tkinter as tk
from tkinter import filedialog
from pytubefix import YouTube

# Function to download YouTube video
def download_video():
    video_url = url_entry.get()
    if not video_url:
        status_label.config(text="Please enter a valid URL.")
        return

# Ask for directory to save video
    save_path = filedialog.askdirectory()

    if not save_path:
        status_label.config(text="Download canceled.")
        return

    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

        
        status_label.config(text=f"Downloading {yt.title}...")
        video_stream.download(output_path=save_path)
        status_label.config(text=f"Downloaded successfully: {yt.title}")
    except Exception as e:
        status_label.config(text=f"Error: {e}")

# GUI Setup
root = tk.Tk()
root.title("YouTube Video Downloader")

# tinketer GUI Input
url_label = tk.Label(root, text="YouTube Video URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Tinkiter Download Button
download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=20)

# Status Label
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Run the GUI loop
root.geometry("400x200")
root.mainloop()
