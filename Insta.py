import instaloader
import os
import sys
import logging

def print_author_banner():
    print("""
    **********************************
    *  Script created by Oliver  *
    **********************************
    """)

def download_instagram_images(profile_name, base_directory):
    print_author_banner()
    
    # Create the directory name as 'profile_name_images'
    save_directory = os.path.join(base_directory, f"{profile_name}_images")

    # Ensure the base directory exists
    if not os.path.exists(base_directory):
        print(f"Error: Base directory '{base_directory}' does not exist.")
        return

    # Create the save directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)

    # Create an instance of Instaloader
    loader = instaloader.Instaloader(download_pictures=True, download_videos=False, download_video_thumbnails=False, download_geotags=False, download_comments=False, save_metadata=False, compress_json=False)

    # Set the download directory
    loader.dirname_pattern = save_directory

    try:
        # Download the profile
        print(f"Starting download for profile: {profile_name}")
        loader.download_profile(profile_name, profile_pic=False)
        print(f"Download complete. Images saved to {save_directory}.")
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error("Error occurred", exc_info=True)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python insta_download.py <profile_name> <base_directory>")
        sys.exit(1)

    profile_name = sys.argv[1]
    base_directory = sys.argv[2]

    download_instagram_images(profile_name, base_directory)
