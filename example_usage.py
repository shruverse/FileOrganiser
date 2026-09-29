#!/usr/bin/env python3
"""
Example usage of the file organizer script.
This shows different ways to use the file_organizer module.
"""

from file_organizer import organize_files, create_folders, get_file_category
from pathlib import Path


def example_basic_usage():
    """Example 1: Basic usage with default Downloads folder"""
    print("Example 1: Organizing Downloads folder")
    downloads_path = str(Path.home() / "Downloads")
    organize_files(downloads_path)


def example_custom_directory():
    """Example 2: Organizing a custom directory"""
    print("\nExample 2: Organizing a custom directory")
    custom_path = "./test_folder"  # Change this to your desired path
    organize_files(custom_path)


def example_check_file_types():
    """Example 3: Testing file categorization"""
    print("\nExample 3: Testing file type categorization")
    test_files = ['.jpg', '.png', '.pdf', '.docx', '.mp4', '.mp3', '.txt', '.zip']
    
    for file_ext in test_files:
        category = get_file_category(file_ext)
        print(f"File type {file_ext} → goes to '{category}' folder")


if __name__ == "__main__":
    # Run examples
    example_check_file_types()
    
    # Uncomment the lines below to test with actual directories
    # example_basic_usage()
    # example_custom_directory()