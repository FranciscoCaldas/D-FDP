import gdown
import os

# Google Drive file ID (from your share link)
FOLDER_URL = "https://drive.google.com/drive/folders/1w34_dURxzX44ehFyG6Fyd6WM6WXPfsXQ?usp=drive_link"
OUTPUT_PATH = "datasets/"

def get_data():
    """Download dataset from Google Drive."""
    os.makedirs("datasets", exist_ok=True)
    
    
    print("Downloading dataset...")
    gdown.download_folder(url=FOLDER_URL, output=OUTPUT_PATH, quiet=False)
    print("Download complete!")

if __name__ == "__main__":
    get_data()