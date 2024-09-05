# Instagram Image Downloader

This script allows you to download images from an Instagram profile using the `instaloader` library. 

## Features

- Downloads all images from a specified Instagram profile.
- Saves images to a directory named after the profile.

## Requirements

- Python 3.x
- `instaloader` library

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Oliver0031/Insta_image_downloader.git
    cd Insta_image_downloader
    ```

2. **Install the required library**:
    ```bash
    pip install instaloader
    ```

## Usage

1. **Run the script**:
    ```bash
    python insta_download.py <profile_name> <base_directory>
    ```

    - `<profile_name>`: The Instagram profile name from which you want to download images.
    - `<base_directory>`: The directory where you want to save the images.

    Example:
    ```bash
    python insta_download.py natgeo /path/to/save/images
    ```

2. **Output**:
    - The images will be saved in a directory named `<profile_name>_images` inside the specified base directory.

## Error Handling

- If the base directory does not exist, the script will print an error message.
- If any error occurs during the download, it will be logged and printed.

## Author

- **Oliver**

## License

This project is licensed under the MIT License - see the LICENSE file for details.
