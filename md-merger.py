import os


def merge_markdown_files(folder_path: str) -> None:
    """
    Merges all Markdown files in a folder into a single Markdown file.

    :param folder_path: Path to the folder containing Markdown files
    :return: None
    """

    markdown_files = [f for f in os.listdir(folder_path) if f.endswith(".md")]
    parent_folder = os.path.dirname(folder_path)
    merged_file_path = os.path.join(parent_folder, "merged.md")
    with open(merged_file_path, "w") as merged_file:
        for file in markdown_files:
            with open(os.path.join(folder_path, file), "r") as md_file:
                merged_file.write(md_file.read() + "\n\n")


def main() -> None:
    """
    Main function.

    :return: None
    """

    folder_path = input("Enter the path to the folder containing Markdown files: ")
    merge_markdown_files(folder_path)
    print("Merged Markdown file 'merged.md' has been created.")


if __name__ == "__main__":
    main()
