#!/usr/bin/env python3
"""
File Organizer Script
A beginner-friendly automation tool to organize files in the Downloads folder by type.

This script automatically sorts files into categorized folders:
- Downloads/images - for .png, .jpg files
- Downloads/files - for .pdf, .docx files  
- Downloads/media - for .mp4, .mp3 files
- Downloads/extra - for all other file types
"""

import os
import shutil
from pathlib import Path


def create_folders(base_path):
    """
    Create the target folders if they don't exist.
    
    Args:
        base_path (Path): The base directory where folders will be created
    """
    folders = ['images', 'files', 'media', 'extra']
    
    for folder in folders:
        folder_path = base_path / folder
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)
            print(f"✓ Created folder: {folder_path}")
        else:
            print(f"✓ Folder already exists: {folder_path}")


def get_file_category(file_extension):
    """
    Determine which category a file belongs to based on its extension.
    
    Args:
        file_extension (str): The file extension (e.g., '.jpg', '.pdf')
        
    Returns:
        str: The category folder name ('images', 'files', 'media', or 'extra')
    """
    # Convert to lowercase for case-insensitive matching
    ext = file_extension.lower()
    
    # Define file type categories
    image_types = {
        '.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'
    }

    document_types = {
        '.pdf', '.doc', '.docx', '.txt', '.xlsx', '.xls', '.ppt', '.pptx'
    }

    media_types = {
        '.mp4', '.mkv', '.avi', '.mov', '.mp3', '.wav', '.flac'
    }
    
    # Return appropriate category
    if ext in image_types:
        return 'images'
    elif ext in document_types:
        return 'files'
    elif ext in media_types:
        return 'media'
    else:
        return 'extra'


def organize_files(directory_path):
    """
    Main function to organize files in the specified directory.
    
    Args:
        directory_path (str): Path to the directory to organize
    """
    # Convert string path to Path object for easier handling
    base_path = Path(directory_path)
    
    # Check if the directory exists
    if not base_path.exists():
        print(f"❌ Error: Directory '{directory_path}' does not exist!")
        return
    
    if not base_path.is_dir():
        print(f"❌ Error: '{directory_path}' is not a directory!")
        return
    
    print(f"🔍 Organizing files in: {base_path}")
    print("-" * 50)
    
    # Create target folders
    create_folders(base_path)
    print("-" * 50)
    
    # Counter for statistics
    moved_files = 0
    skipped_items = 0
    
    # Scan all items in the directory
    for item in base_path.iterdir():
        # Skip if item is a directory (we only want to move files)
        if item.is_dir():
            print(f"⏭️  Skipping directory: {item.name}")
            skipped_items += 1
            continue
        
        # Skip if item is not a file (e.g., symbolic links)
        if not item.is_file():
            print(f"⏭️  Skipping non-file item: {item.name}")
            skipped_items += 1
            continue
        
        # Get file extension and determine category
        file_extension = item.suffix
        category = get_file_category(file_extension)
        
        # Create destination path
        destination_folder = base_path / category
        destination_path = destination_folder / item.name
        
        # Handle file name conflicts
        counter = 1
        original_destination = destination_path
        while destination_path.exists():
            # Add number suffix if file already exists
            stem = original_destination.stem
            suffix = original_destination.suffix
            destination_path = destination_folder / f"{stem}_{counter}{suffix}"
            counter += 1
        
        try:
            # Move the file
            shutil.move(str(item), str(destination_path))
            print(f"📁 Moved '{item.name}' → {category}/{destination_path.name}")
            moved_files += 1
            
        except Exception as e:
            print(f"❌ Error moving '{item.name}': {e}")
            skipped_items += 1
    
    # Print summary
    print("-" * 50)
    print(f"✅ Organization complete!")
    print(f"📊 Files moved: {moved_files}")
    print(f"⏭️  Items skipped: {skipped_items}")


def main():
    """
    Main entry point of the script.
    """
    print("🗂️  File Organizer - Downloads Folder Cleanup")
    print("=" * 50)
    
    # Default directory (you can change this or make it configurable)
    downloads_path = str(Path.home() / "Downloads")
    
    # Ask user for confirmation or custom path
    print(f"Default directory: {downloads_path}")
    user_input = input("Press Enter to use default, or type a different path: ").strip()
    
    if user_input:
        downloads_path = user_input
    
    # Start organizing
    organize_files(downloads_path)


if __name__ == "__main__":
    main()