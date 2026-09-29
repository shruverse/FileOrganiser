# FileOrganiser
A terminal based python scrapping program that organises the downloads (or any desired folder) into 4 categorised folders. 

# 🗂️ File Organizer

A beginner-friendly Python automation tool that automatically organizes
files into categorized folders based on their file extensions.

## ✨ Features

- Automatically organizes files into categories
- Supports images, documents, audio/video and other file types
- Creates category folders automatically
- Handles duplicate file names
- Supports custom directories
- Provides a summary of files moved and skipped
- Uses Python's built-in `pathlib` and `shutil` modules
- No external dependencies required

## 📁 Categories

| File Types | Folder |
|------------|--------|
| `.png`, `.jpg`, `.jpeg` | `images/` |
| `.pdf`, `.docx` | `files/` |
| `.mp4`, `.mp3` | `media/` |
| Other extensions | `extra/` |

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd FileOrganizer
```
### 2. Run Program

1. Download the required libraries
Either by clicking on the 💡 icon in the pycharm editor or vs code
Or by the terminal commands
```bash
pip install shutil, Path
```

2. Run the program
```bash
python file_organizer.py
```

The program will ask whether you want to organize your default
Downloads folder or provide a custom directory.

## 💡 Example
Before:
Downloads/
├── photo.jpg
├── resume.pdf
├── song.mp3
├── movie.mp4
└── notes.txt

After:
Downloads/
├── images/
│   └── photo.jpg
├── files/
│   └── resume.pdf
├── media/
│   ├── song.mp3
│   └── movie.mp4
└── extra/
    └── notes.txt

## 🛠️ Technologies
- Python
- pathlib
- shutil
- os
- 
## 🎯 What I Learned
- File and directory handling
- Python functions and modules
- Path manipulation
- File extensions and categorization
- Exception handling
- Automation using Python
- Handling duplicate filenames
- 
## 📌 Future Improvements
(that I might do later or You might wanna try)
- Add more file categories
- Add a dry-run mode
- Add command-line arguments
- Add logging
- Add recursive folder organisation
- Add a GUI
