import os
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

# Your Flic-Token
FLIC_TOKEN = "flic_37a628e0354f719f220a86b7ab644b49c414256c4c0b9debd3dbebc6746a9e7e"
HEADERS = {
    "Flic-Token": FLIC_TOKEN,
    "Content-Type": "application/json"
}

# Function 1: Get Upload URL
def get_upload_url():
    endpoint = "https://api.socialverseapp.com/posts/generate-upload-url"
    response = requests.get(endpoint, headers=HEADERS)
    if response.status_code == 200:
        return response.json()  # Returns a dictionary with 'url' and 'hash'
    else:
        print("Failed to get upload URL:", response.text)
        return None

# Function 2: Upload Video
def upload_video(file_path, upload_url):
    with open(file_path, 'rb') as video_file:
        response = requests.put(upload_url, data=video_file)
    if response.status_code == 200:
        print("Video uploaded successfully.")
    else:
        print("Failed to upload video:", response.text)

# Function 3: Create Post
def create_post(video_title, video_hash, category_id):
    endpoint = "https://api.socialverseapp.com/posts"
    data = {
        "title": video_title,
        "hash": video_hash,
        "is_available_in_public_feed": True,  # Make post visible in Super Feed
        "category_id": category_id  # Use category ID for "Super Feed"
    }
    response = requests.post(endpoint, headers=HEADERS, json=data)
    if response.status_code == 200:
        print("Post created successfully.")
        print("Create Post Response:", response.json())  # Debugging response
    else:
        print("Failed to create post:", response.text)

# Function 4: Upload Process
def upload_process(video_path):
    # Step 1: Get Upload URL
    upload_info = get_upload_url()
    if not upload_info:
        return
    upload_url = upload_info['url']
    video_hash = upload_info['hash']

    # Step 2: Upload Video
    upload_video(video_path, upload_url)

    # Step 3: Create Post
    video_title = os.path.basename(video_path)
    create_post(video_title, video_hash, category_id=25)  # Super Feed category (ID 25)

    # Step 4: Delete Local File
    os.remove(video_path)
    print(f"Deleted local file: {video_path}")

# Function 5: Directory Monitoring
class VideoHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith('.mp4'):
            print(f"New video detected: {event.src_path}")
            upload_process(event.src_path)

def monitor_videos():
    path = "./videos"
    if not os.path.exists(path):
        os.makedirs(path)
    event_handler = VideoHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print("Monitoring /videos directory for new videos...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Main Entry Point
if __name__ == "__main__":
    monitor_videos()
