# Downloads File Organizer

## Project Overview

Downloads File Organizer is a Python command-line utility that organises files in a Downloads folder into categories based on their file extensions.

It was developed as a practical Python project to explore file handling, directory management, command-line arguments and exception handling.

## Features

- Automatically categorises files by extension.
- Supports images, documents, videos, audio, archives and other file types.
- Provides a dry-run mode to preview proposed changes without moving files.
- Requires an explicit `--apply` argument to move files.
- Prevents existing files from being overwritten by generating unique filenames.
- Allows users to specify a custom source directory.
- Reports skipped files and file-operation errors.

## Requirements

- Python 3.9 or later
- No external Python packages required.

## How to Run

### 1. Preview the proposed organisation

Open a terminal in the project directory and run:

```bash
python3 organize_downloads.py
```

By default, the program examines the user's Downloads folder and displays the files it would move.

**No files are moved in preview mode.**

### 2. Apply the organisation

After reviewing the preview, run:

```bash
python3 organize_downloads.py --apply
```

This executes the file movements.

### 3. Organise a different directory

To specify another source directory:

```bash
python3 organize_downloads.py --source "/path/to/folder"
```

To preview that directory, omit `--apply`. To actually organise it, include `--apply`.

## Safety Notes

- Always review the dry-run output before applying changes.
- The `--apply` argument performs actual file movements.
- Duplicate filenames are handled by generating alternative filenames.
- Unsupported files, directories and symbolic links are skipped.

## Python Concepts Practised

- `pathlib` for filesystem paths and directory operations.
- `shutil` for moving files.
- Dictionaries and lists for file categorisation.
- Functions and loops.
- Conditional statements.
- Exception handling.
- Command-line argument parsing with `argparse`.
- File extensions and string methods.

## Project Structure

```text
downloads-organizer/
├── README.md
└── organize_downloads.py
```

## Project Status

Completed — OPERATION SPONGE practical project.

*Built through experimentation, debugging and practical application of Python.*
