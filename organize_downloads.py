
from pathlib import Path
import shutil
import argparse


# 1. Define the file categories and their extensions
FOLDERS = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".webp", ".gif",
        ".svg", ".bmp", ".tiff", ".tif", ".heic",
        ".heif", ".raw", ".cr2", ".nef",".avif", ".odg"
    ],

    "Documents": [
        ".pdf", ".doc", ".docx", ".xls", ".xlsx",
        ".ppt", ".pptx", ".txt", ".csv", ".rtf",
        ".odt", ".ods", ".odp", ".md",".xltx", ".ics"
    ],

    "Videos": [
        ".mp4", ".mov", ".avi", ".mkv", ".wmv",
        ".webm", ".mpeg", ".mpg", ".m4v"
    ],

    "Audio": [
        ".mp3", ".wav", ".flac", ".aac", ".ogg",
        ".m4a", ".wma", ".opus"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz",
        ".bz2", ".xz", ".tgz"
    ],
    "Apk" :[".apk"],
    "HTML" :[".html", ".xml"],
    "Text" : [".txt", ".json", ""],
    "Subtitles" :[".srt"],
    "Others" : [".exe", ".gs", ".crdownload"]

}


# 2. Find an available filename without overwriting anything
def get_unique_target(target):

    if not target.exists() and not target.is_symlink():
        return target

    counter = 1

    while True:
        new_name = (
            f"{target.stem}_{counter}{target.suffix}"
        )

        new_target = target.with_name(new_name)

        if not new_target.exists() and not new_target.is_symlink():
            return new_target

        counter += 1


# 3. Organise the Downloads folder
def organise_downloads(downloads, apply_changes):

    if not downloads.exists() or not downloads.is_dir():
        print(f"Error: Downloads folder not found: {downloads}")
        return 1

    try:
        files = list(downloads.iterdir())
    except OSError as error:
        print(f"Could not read Downloads folder: {error}")
        return 1

    moved = 0
    planned = 0
    skipped = 0
    failed = 0

    print("\n" + "=" * 50)
    print("          DOWNLOADS FILE ORGANISER")
    print("=" * 50)

    if apply_changes:
        print("MODE: ACTUAL FILE MOVEMENT")
    else:
        print("MODE: DRY RUN (NOTHING WILL BE MOVED)")

    print(f"\nFolder: {downloads}\n")

    # 4. Examine each item in Downloads
    for file in files:

        try:
            # Ignore folders and symbolic links
            if file.is_symlink() or not file.is_file():
                skipped += 1
                continue

            # Identify the file extension
            ext = file.suffix.lower()

            # Find the matching category
            category = None

            for name, extensions in FOLDERS.items():

                if ext in extensions:
                    category = name
                    break

            # Leave unsupported files untouched
            if category is None:
                skipped += 1
                continue

            # Construct the destination
            folder = downloads / category
            target = folder / file.name

            # Protect against duplicate filenames
            target = get_unique_target(target)

            # Preview mode
            if not apply_changes:

                print(
                    f"WOULD MOVE: {file.name} "
                    f"-> {category}/{target.name}"
                )

                planned += 1
                continue

            # Actual movement
            folder.mkdir(exist_ok=True)

            shutil.move(str(file), str(target))

            print(
                f"MOVED: {file.name} "
                f"-> {category}/{target.name}"
            )

            moved += 1

        except OSError as error:

            print(f"ERROR: {file.name}: {error}")
            failed += 1

    # 5. Display the final report
    print("\n" + "=" * 50)
    print("                 SUMMARY")
    print("=" * 50)

    if apply_changes:
        print(f"Files moved:       {moved}")
    else:
        print(f"Files ready to move: {planned}")

    print(f"Files skipped:     {skipped}")
    print(f"Files with errors: {failed}")

    print("=" * 50)

    if not apply_changes:
        print("\nNothing has been moved.")
        print("To execute the organisation, run with --apply.")

    else:
        print("\nOrganisation completed.")

    return 1 if failed else 0


# 6. Set up programme execution
def main():

    parser = argparse.ArgumentParser(
        description="Safely organise files in your Downloads folder."
    )

    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually move files. Without this, only preview changes."
    )

    parser.add_argument(
        "--source",
        type=Path,
        default=Path.home() / "Downloads",
        help="Folder to organise. Defaults to your Downloads folder."
    )

    args = parser.parse_args()

    return organise_downloads(
        args.source,
        args.apply
    )


if __name__ == "__main__":
    raise SystemExit(main())


'''
Inspecting the filess before organizing them:
python3 organize_downloads.py
'''

'''
executing the program after organizing the files:
python3 organize_downloads.py --apply
'''